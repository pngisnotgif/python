# 9-20

import glob
import gzip
import os
import shutil

files = glob.glob('*.py')   # find all py files in current dir.
gz_file = 'python.py.gz'
out_dir = '9-20'

# this function will compress all the python scripts in one file
def compress_py():
    f_out = gzip.open(gz_file,'wb')
    for f in files:
        f_in = open(f,'rb')
        f_out.writelines(f_in)
        f_in.close()
    f_out.close()

def decompress_py():
    f_in = gzip.open(gz_file,'rb')
    py_file = os.path.splitext(gz_file)[0]
    f_out = open(py_file,'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
                 
    

if __name__=='__main__':
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    compress_py()
    shutil.move(gz_file, out_dir+'/'+gz_file)   # move gz files to out dir

    os.chdir(out_dir)
    decompress_py()
