# 9-21

import glob
import zipfile
import os

pyfiles = glob.glob('*.py')   # find all py files in current dir.
zip_file_name = 'python.zip'
txtfile = glob.glob('*.txt')
out_dir = '9-21'

def compress_all_py(file_list):
    f_out = zipfile.ZipFile(zip_file_name,'w',zipfile.ZIP_DEFLATED )
    for f in file_list:
        f_out.write(f)
    f_out.close()

def append_arch(filename):
    f_out = zipfile.ZipFile(zip_file_name,'a',zipfile.ZIP_DEFLATED )
    f_out.write(filename)
    f_out.close()

def extract_arch(filename):
    f_in = zipfile.ZipFile(zip_file_name)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    f_in.extract(filename,out_dir)
    f_in.close()

if __name__=='__main__':
    compress_all_py(pyfiles)    # compress all py files
    
    for txt in txtfile:         # compress txt files into zip
        append_arch(txt)

    extract_arch('9-21.py')
