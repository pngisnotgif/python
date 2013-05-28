# 9-13

import sys
import getopt

def usage():
    print '''
Usage of this python script:
    
    -i filename : input file
    -o filename : output file
    -c : only compile
    -d : decode
    -h, --help : print this help.
'''

if __name__=='__main__':
    my_argv = '-i file1 -o file2 -cd a b'
    sys.argv[1:] = my_argv.split()

    # print all the arguments in 9-13
    for i,arg in enumerate(sys.argv):
        print '[%d]:'%(i) ,arg
    print

    try:
        optlist, other_args = getopt.getopt(sys.argv[1:], 'i:o:cdh', ['help'])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    # print optlist
    # print other_args

    input_file = ''
    output_file = ''
    compile_only = False
    decode = False
    for o,a in optlist:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o == '-i':
            input_file = a
        elif o == '-o':
            output_file = a
        elif o == '-c':
            compile_only = True
        elif o == '-d':
            decode = True
        else:         
            usage()
            err_str = "unhandled options: %s"%(str(o))
            assert False, err_str
            sys.exit(2)

    print 'input file: %s'%(input_file)
    print 'output file: %s'%(output_file)
    print 'compile only: %s'%(compile_only)
    print 'decode: %s'%(decode)
            
    if other_args:
        print '\nOther parameters:'
        for i in other_args:
            print i
        
