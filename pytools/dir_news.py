
# -- coding: utf-8 --

# 获取子目录更新内容
# 
# TODO:
# 1. 正则表达式实现忽略文件名单
# 2. 日期指定更灵活，相对天数指定
# 

from os import listdir
import os.path
import time

start_dir = '.'          # 起始搜索目录
last_date = '2013-8-1'      # 起始匹配日期
ignore_list = ['Thumbs.db'] # 忽略文件列表
out_filename = 'news.txt'   # 输出文件

date_fmt = '%Y-%m-%d'
last_date_struct = time.strptime(last_date, date_fmt)
lst_time = time.mktime(last_date_struct)    # last date to float since epoch
           
def get_newly_modified_files(out_file, filelist):
    isPrintDirname = False
    isPrintEOL = False
    
    for i,f in enumerate(sorted(filelist)):     
        dirname, filename = os.path.split(f)
        
        # 忽略文件处理
        if filename in ignore_list:
            continue

        if os.path.isfile(f):
            # s = time.ctime( os.path.getmtime(f) )

            # 保留较新文件信息
            s = os.path.getmtime(f) # 获取文件的上次修改时间
            if s > lst_time:
                # 有满足条件文件，则打印目录
                if not isPrintDirname:
                    isPrintDirname = True
                    out_file.write(' [' + dirname + '\\ ]: \n')
                    print dirname   # 同时输出到屏幕
                
                fmt = '  [{}] {} ' + '\t'*4 + '{}\n'
                # time_out_fmt = date_fmt + '%H:%M'
                out_file.write(fmt.format(i+1, f, time.ctime(s)))

                isPrintEOL = True

    # 如有满足条件的文件，则打印空行分隔
    if isPrintEOL:
        out_file.write('\n')

with open(out_filename, 'w+') as f:
    print 'Processing...'
    f.write('目录"{}"中晚于{}更新的文件列表：\n\n'.format(start_dir, last_date))
    
    # 遍历目录
    for curdir, subdir, filenames in os.walk(start_dir):
        # print curdir
        if os.path.isdir(curdir) :
            filelist = [os.path.join(curdir, fname) for fname in filenames]
            get_newly_modified_files(f, filelist)

print 'Finished.'
