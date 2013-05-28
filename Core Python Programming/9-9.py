# 9-9

import os

lib_path = r'D:\Python27\Lib'
lib_file = os.listdir(lib_path)
ext_name = '.py'
py_file = [i for i in lib_file if i[len(i)-len(ext_name):]==ext_name]

workdir = os.chdir(lib_path)

for eachFile in py_file:
    f = open(eachFile)
    lines = f.readlines()
    f.close()
    for l in lines:
        if l.find('__doc__')>=0:
            print f.name,':', l,
            # doc_content = l.split('=')[1]
            # print doc_content
            # raw_input()

