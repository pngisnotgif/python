# 9-9

import os
import os.path
import platform

pf = platform.system()
if pf=='Darwin':
    lib_path = r'/Library/Frameworks/Python.framework/Versions/Current/lib/python2.7'
else:   # assume it is Windows
    lib_path = r'D:\Python27\Lib'
    
lib_file = os.listdir(lib_path)
ext_name = '.py'
py_file = [i for i in lib_file if os.path.splitext(i)[1]==ext_name] # split ext name from filename

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

print 'script terminated.'
