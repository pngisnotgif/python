
# 13-14

import sys
import os

# TODO: translate cmd args in DOS
def trans2dos(str_in):
    unix2dos_cmd_dict = {
        'ls':'dir',
        'more':'more',
        'cat':'type',
        'cp':'copy',
        'mv':'ren',
        'rm':'del'
        }

    c_list = str_in.split()
    cmd = c_list[0]
    args = c_list[1:]

    if cmd in unix2dos_cmd_dict.keys():
        dos_cmd = unix2dos_cmd_dict[cmd]
    else:
        dos_cmd = cmd
    
    if args == '--help':
        dos_args = ' /?'
    else:
        dos_args = args # TODO: deal with every cmd
        
    cmdline = dos_cmd + ' '.join(dos_args)
   
    if cmd not in unix2dos_cmd_dict.keys():
        print 'Bad command for %s'%(str_in) 
    
    return cmdline

def unix_like_shell():
    platform = sys.platform
    if platform == 'darwin':
        is_unix_shell = True
    elif platform in ('win32','dos'):
        is_unix_shell = False

    while True:
        try:
            cmd = raw_input('>>> ')
 
            if cmd.split()[0] in ('exit', 'quit'):
                raise KeyboardInterrupt

            if platform in ('win32','dos'):
                cmdline = trans2dos(cmd)
            elif is_unix_shell:
                cmdline = cmd
            print cmdline
            
            os.system(cmdline)  # call system cmd
            
        except (KeyboardInterrupt, EOFError):
            break
        except IndexError:
            pass

if __name__=='__main__':
    unix_like_shell()
