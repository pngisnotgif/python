
# 13-14

import sys
import os

# TODO: translate cmd args in DOS
def translate_args(args):
    return args

def unix_like_shell():

    unix2dos_cmd_dict = {
        'ls':'dir',
        'more':'more',
        'cat':'type',
        'cp':'copy',
        'mv':'ren',
        'rm':'del'
        }
    
    platform = sys.platform
    if platform == 'darwin':
        is_unix_shell = True
    elif platform in ('win32','dos'):
        is_unix_shell = False

    while True:
        try:
            str_in = raw_input('>>>').split()
            cmd = str_in[0]
            args = str_in[1:]
            
            if cmd=='exit':
                raise KeyboardInterrupt

            if platform in ('win32','dos'):
                dos_cmd = unix2dos_cmd_dict[cmd]
                dos_args = translate_args(args)
                cmdline = dos_cmd + dos_args
            elif is_unix_shell:
                cmdline = cmd + ' '.join(args)

            print cmdline
            os.system(cmdline)  # how to delete cmd string when executing?
            
        except (KeyboardInterrupt, EOFError):
            break

if __name__=='__main__':
    unix_like_shell()
