# -*- coding: utf-8 -*-
# 12-6

def importAs(modulename):
    try:
        newname = __import__(modulename)
    except Exception:
        raise
    
    return newname

if __name__=='__main__':
    a = importAs('sys')
    print dir(a)
    print a.version
