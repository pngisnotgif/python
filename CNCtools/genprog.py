
# -- coding=utf-8 --

'''
    产生指定大小或段数的NC程序

@todo 目前产生的文件大小按照规定（至少70 bytes）,\n
但最后一段可能不能执行（直接截断中间字符）

    v1.1 - 可以指定产生程序的段数
    v1.0 - 可以产生指定大小的NC程序
'''

import argparse
import os
import sys
import random

def args_parser(default_args):   
    parser = argparse.ArgumentParser(description = 'Generate CNC Program.')
    parser.add_argument('-n', '--number', help='Program number(O number)', type=int, default=1)
    parser.add_argument('-o', '--output', help='Output file name.')

    type_group = parser.add_mutually_exclusive_group(required=True)
    type_group.add_argument('-s', '--size', help='File size of CNC prog.')
    type_group.add_argument('-p', '--paras', help='Paragraph numbers of CNC prog.')

    return parser.parse_args(default_args)

class NCFileAttr(object):
    '''
        NC程序的属性.
    '''

    def __init__(self, filename, onumber, size=None, paras=None):
        self.filename = filename
        self.onumber = onumber
        self.size = size
        self.paras = paras
    
def nc_args_parser(default_args):
    '''
        根据命令行参数，解析出输出NC程序所需的参数。
    '''
    
    if not isinstance(default_args, list):
        raise TypeError,'parameter "default_args" should be a list.'
    
    args = args_parser(default_args)

    if not args.output:
        args.output = 'O{:04d}.TXT'.format(args.number)

    if args.size:
        if args.size[-1].upper() in ('K', 'M'):
            scale = {'K':1024, 'M':1024*1024}
            args.size = int(float(args.size[:-1]) * scale[args.size[-1].upper()])
        else:
            args.size = int(args.size)
            if args.size < 70:
                print('Warning: Size of NC prog. is 70 bytes at least.')

    if args.paras:  # str ==> int
        if args.paras[-1].upper() in ('F',):    # tuple of only one element should end with comma
            PARA_PER_FRAME = 8192
            args.paras = int(args.paras[:-1]) * PARA_PER_FRAME
        else:
            args.paras = int(args.paras)

    nc_file_attr = NCFileAttr(args.output, args.number, args.size, args.paras)
    
    return nc_file_attr  

class Axis(object):
    '''
        单个轴的控制
    '''

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.pos = self.start       # current position
        self.delta = step           # delta postion
        self.isPositiveDir = True   # 初始移动方向: True为正向，False为负向
        self.isDirChanged = False   # 方向是否改变

    def __str__(self):
        return '{:.3f}'.format(self.pos)

    __repr__ = __str__    

    def step(self):
        '''
            每次走一步
        '''
        
        epsilon = 0.00001
        if self.isPositiveDir:
            if self.pos + self.delta + epsilon < self.end:
                # if no 0.00001, when the file is large(>1MB), two identical blocks are generated.
                # this is because floating computing error
                self.pos += self.delta
                self.isDirChanged = False
            else:   # come to max value, and reverse dir.
                self.pos = self.end
                self.isPositiveDir = False
                self.isDirChanged = True
        else:       # come to min value, and reverse dir.
            if self.pos - self.delta - epsilon > self.start:
                self.pos -= self.delta
                self.isDirChanged = False
            else:
                self.pos = self.start
                self.isPositiveDir = True
                self.isDirChanged = True

    def fast_step(self):
        '''
            快速移动，直接移动到终点.
        '''
        
        temp_delta = self.delta
        if self.isPositiveDir:
            self.delta = self.end - self.pos
        else:
            self.delta = self.pos - self.start
        self.step()
        self.delta = temp_delta
                
class Robot(object):
    '''
        三坐标位置控制.
    '''
    
    def __init__(self, move_method='fixed', step_method='fixed', steps=None):

        if not isinstance(move_method, str) or move_method not in ('fixed','random'):
            raise TypeError, 'parameter move_method should be "random" or None'        
        
        if move_method == 'fixed': # 若不使用随机方法，能保证每次程序一致
            x_max = 200.0
            y_max = 100.0
            xy_minstep = 0.012
            dz = 0.2       
        elif move_method == 'random':
            x_max = 500 * random.random()
            y_max = 500 * random.random()
            xy_minstep = 0.001 * random.randint(5, 100)   # x或y方向每段最小进给量
            dz = 0.001 * random.randint(100, 2000)     # z向移动时每次进给量

        # print(x_max,y_max)

        x_min = 0.0
        y_min = 0.0        

        if not isinstance(step_method, str):
            print("Warning: step_method should be a string. We converted it to 'fixed'.")
            step_method = 'fixed'
            
        if step_method not in ('fixed', 'dynamic'):
            step_method = 'fixed'
            
        if step_method == 'dynamic':        # 动态进给量，根据步数steps计算每步进给量
            if not isinstance(steps, int):
                raise TypeError, '"steps" should be an integer.'
            
            dx = self.cal_delta(x_min, x_max, steps, xy_minstep)             
            dy = self.cal_delta(y_min, y_max, steps, xy_minstep)   
        else:                               # 使用固定进给量
            dx = xy_minstep
            dy = xy_minstep

        # print('steps={}, dx={}, dy={}'.format(steps, dx, dy))        

        self.x = Axis(x_min, x_max, dx)
        self.y = Axis(y_min, y_max, dy)
        self.z = Axis(0.0, 10000.0, dz)

        self.state = 1  # robot移动状态机
        

    def cal_delta(self, min, max, steps, minstep):
        '''
            根据步数计算每段进给量.

            计算并限制x,y方向每次进给量.
            当x,y终点坐标相差较大时，可能会出现最后一步某个轴需要走很远            
        '''
        delta_try = (max - min) / steps
        if delta_try < minstep:
            delta_try = minstep
        return delta_try
        
    def xy_step(self):
        '''
            处理xy方向移动
        '''

        if self.state == 3:     # Z向输出后，XY方向同时进给
            self.x.step()
            self.y.step()
            self.state = 1
        else:                   # state 1: xy step
            if (not self.x.isDirChanged) and self.y.isDirChanged:
                self.x.fast_step()  # x方向快进
            elif self.x.isDirChanged and (not self.y.isDirChanged):
                self.y.fast_step()  # y方向快进
            elif not self.x.isDirChanged and not self.y.isDirChanged:
                self.x.step()       # xy线性插补
                self.y.step()
            else:
                self.state = 2  # state 2: xy stop

    def z_step(self):
        self.z.step()

    def step(self):
        '''
            控制xyz向的运动.

            1. 从{0, 0}到{x_max, y_max}之间进行线性插值
            2. 到达最大值后，在Z向输出运动；
            3. 下一段开始，反向运动：从{x_max, y_max}到{0, 0}            
        '''
        
        while True:
            self.xy_step()
            if self.state == 2:
                self.state = 3  # state 3: z step
                self.z_step()
            yield
            

def gen_nc_para(line, filesize, paras):
    '''
        使用生成器产生NC段序列，每次一段。

        若Z向移动，修改F值；Z向移动结束，恢复F值。————模拟实际CAM软件生成的程序，同时也能产生长度不同的段
    '''

    if filesize is None:
        robot = Robot(step_method = 'fixed', move_method = 'random')
    elif paras is None:
        steps_try = filesize / 30 # 根据程序大小预估段数，30是根据一般NC段('N12345 X1.234 Y5.678 Z9.101 ;')的字符数得出
        robot = Robot(step_method = 'dynamic', steps = steps_try)
        
    move = robot.step()
    restore_f = False
    
    while(True): 
        move.next()

        if robot.state == 1:    # 生成xy向移动的程序段
            if not restore_f:   # without F
                para = 'N{:05d} X{} Y{} ;\n'.format(line, robot.x, robot.y)
            else:               # restoring F after Z movement
                para = 'N{:05d} X{} Y{} F1000;\n'.format(line, robot.x, robot.y)
                restore_f = False
        elif robot.state == 3:  # 生成z向移动的程序段. state在这里不会等于2
            para = 'N{:05d} Z{} F100. ;\n'.format(line, robot.z) # this line only outputs Z
            restore_f = True    # Prepare to restore F
   
        yield para
        line += 1

   
class PrgFinishError(GeneratorExit): pass   # 程序生成结束异常

class NCFileWriter(object):
    '''
        NC文件写入器。

        实际使用时，不根据本类进行实例化。
        有两个子类：按照文件大小生成，或者按照段数。
    '''

    def __init__(self, f, init_i, left=None, paras=None):
        self.f = f                  # file handle
        self.i = init_i             # 开始生成段数
        
    def write_para(self, para):
        '''
            每次写一段。
        '''
        self.i += 1

class NCFileWriterByFileSize(NCFileWriter):
    '''
        固定文件大小的NC文件写入器.
    '''
    
    def __init__(self, f, init_i, left):
        super(self.__class__, self).__init__(f, init_i)
        self.left = left            # 剩余生成文件大小
        self.nlength = 5            # N号长度，用于调整最后一段长度
       
    def write_para(self, para):
        '''
            Write fixed-sized NC file.
        '''
        
        super(self.__class__, self).write_para(para)
        
        if len(str(self.i))>self.nlength:   # 行号超过5位时，需要调整left。因为最后一段的N号会超过5位
            self.left -= 1
            self.nlength += 1
                
        if len(para) >= self.left:  # deal with last line
                                    # but, it may not be excuted in this way
            para = self.deal_last_para(para)
            
        self.f.write(para)     
        self.left -= len(para)+1     # every line has a '\n'
        
        if self.left <= 0:
            raise PrgFinishError

    def deal_last_para(self, para):
        '''
            Cut last one or two paras to fixed size.
        '''
        
        if self.left>3:
            para = para[:self.left-3]
        else:
            # when leftsize<3, previous NC block should be cut
            backward = 3 - self.left
            self.f.seek( -backward, os.SEEK_CUR )
            
            para = ''
            if self.left==2: # backward one more char.: 0x0d --> space
                self.f.seek( -1, os.SEEK_CUR) 
                para += ' '
                backward += 1

            # adjust self.left
            self.left += backward
            
        para += ';\n'
        return para
    
class NCFileWriterByParas(NCFileWriter):
    '''
        固定段数的NC文件写入器.
    '''
    
    def __init__(self, f, init_i, paras):
        super(self.__class__, self).__init__(f, init_i)
        self.targetparas = paras    # 目标生成段数

    def write_para(self, para):
        '''
            Write fixed-paragraphed NC file.
        '''

        super(self.__class__, self).write_para(para)        
        
        self.f.write(para)
        if self.i >= self.targetparas:
            raise PrgFinishError         

def _gen_nc_prg(filename, Onumber, filesize=None, paras=None):
    '''
        产生NC程序。

        注：参数filesize和paras只能指定其一。
        
        @parameter filesize 指定程序大小
        @parameter paras 指定生成段数
    '''

    if filesize is None and paras is None:
        raise TypeError,'filesize or paras should be given.'
    if filesize is not None and paras is not None:
        raise TypeError,'only one parameter between filesize and paras is allowed.'
    
    size = filesize
    with open(filename, 'w') as f:
        header = '%\n' + 'O{:04d} ;\n'.format(Onumber)
        G00 = 'N{:05d} G00 X0 Y0 ;\n'.format(1)
        G01 = 'N{:05d} G01 F1000. ;\n'.format(2)
        end = 'N{:05d} M30 ;\n' + '%\n'   # before adding format(), len(end)=16, but is actually 15
        # these 4 lines take 70 bytes

        f.write(header)
        f.write(G00)
        f.write(G01)

        i = 3
        if size is not None:        
            size -= len(header)
            size -= len(G00)
            size -= len(G01)
            size -= len(end)-1
            size -= 6   # six '\n's occupy 6*2 bytes in Windows
            nc_writer = NCFileWriterByFileSize(f, i, size)
        elif paras is not None:
            nc_writer = NCFileWriterByParas(f, i, paras)

        nc_gen = gen_nc_para(i, size, paras)    # start from line i
        for para in nc_gen:    
            try:
                nc_writer.write_para(para)
            except PrgFinishError:
                nc_gen.close()

        para = end.format(nc_writer.i)    # write end of NC prg.
        f.write(para)
        
    print('File generated.')

def gen_nc_prg_size(filename, Onumber, filesize):
    '''
        产生指定大小的文件
    '''
    _gen_nc_prg(filename, Onumber, filesize, paras=None)

def gen_nc_prg_para(filename, Onumber, paras):
    '''
        产生指定段数的文件
    '''
    _gen_nc_prg(filename, Onumber, filesize=None, paras=paras)
    
if __name__=='__main__':
    if len(sys.argv)==1:
        test = '-n 2 -s 1m -otest.txt'
        # test = '-p 10f -otest.txt'
        test_args = test.split()
    else:
        test_args = sys.argv[1:]
    nc_file_attr = nc_args_parser(test_args)
    
    onumber, size, filename = nc_file_attr.onumber, nc_file_attr.size, nc_file_attr.filename
    paras = nc_file_attr.paras
    
    _gen_nc_prg(filename, onumber, size, paras)
    
