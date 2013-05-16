# -*- coding: utf-8 -*-

# 12-5

try:
    del os
except NameError:
    # 导入os.path模块。 等价于：from os import path
    os = __import__('os',globals(), locals(),['path'])
    path = os.path

    # 如何更一般地执行：modulename = __import__( modulename ) ?
    
    raw_input(u'将显示path模块下的方法及属性(任意键继续)：')
    for i in dir(path):
        print i
    print
    
    raw_input(u'<按任意键继续>')
    print u"文档：\n", path.__doc__
