# 9-22

import zipfile
import time

zip_filename = 'python.zip'
zip_file = zipfile.ZipFile(zip_filename)

def list_header():
    print "name\t\tsize(byte)\tratio\t create time"
    print '-'*50

def list_info(membername):
    info = zip_file.getinfo(membername)
    name = info.filename
    size = info.compress_size
    try:
        ratio = float(size)/info.file_size
    except ZeroDivisionError:
        ratio = 1.0
    
    date_time = list(info.date_time)
    date_time.append(0)
    date_time.append(1)
    date_time.append(-1)
    date_time_tuple = tuple(date_time)
    ctime = time.strftime("%b %d %Y %H:%M:%S ",date_time_tuple) 

    print "%s\t\t%d\t\t%.3f\t%s"%(name, size, ratio, ctime)

if __name__=='__main__':
    list_header()
    for f in zip_file.namelist():
        list_info(f)
