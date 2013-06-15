# 13-7

import time

class mytime(object):
    '''
        mytime class
    '''

    format_dict = {'MDY':'%m/%d/%y',
                   'MDYY':'%m/%d/%y',
                   'DMY':'%d/%m/%y',
                   'DMYY':'%d/%m/%Y',
                   'MODYY':'%b %d, %Y',
                   'default':'%a %b %d, %H:%M:%S %Y',
        }   # date format dictionary

    def __init__(self, form=None, timevalue=None):       
        if timevalue is None:
            self.timestamp = time.localtime()
        else:   
            self.setTime(form, timevalue)
        
    def update(self, form=None, newtime = None):
        if newtime is None:
            self.timestamp = time.localtime()
        else:
            self.setTime(form, newtime)

    def setTime(self, form, value):
        '''
            User defined date format and time value
        '''
        if form in self.format_dict.keys():
            format_str = self.format_dict[form]
        else:
            format_str = self.format_dict['default']

        try:
            self.timestamp = time.strptime(value, format_str)
        except ValueError, msg:
            print 'Wrong time value: %s'%(msg)

    def getFormat(self, form):
        'Convert user entered format to format string.'
        
        if form in self.format_dict.keys():
            format_str = self.format_dict[form]
        else:
            format_str = self.format_dict['default']
            
        return format_str
    
    def display(self, form = None):
        format_str = self.getFormat(form)
        time_str = time.strftime(format_str, self.timestamp)
        print time_str

    @classmethod
    def show_format(cls):   # note: parameter is cls
        # print cls
        print 'format : date string'
        print '-'*20
        for i in mytime.format_dict:
            print i,':', mytime.format_dict[i]


def testDisplay(t):
    form_list = t.format_dict.keys()
    for i in form_list:
        t.display(i)

def testMytime():
    print 'Initializing mytime:'
    time1 = mytime()
    testDisplay(time1)
    print

    print 'Initializing using user defined format:'
    time2 = mytime('MDY','01/01/90')
    time2.display()
    print

    print 'Testing update():'
    time2.update(newtime = '14/6/2013', form='DMYY')
    time2.display()
    
    time2.update(form='DMY')
    time2.display()
    
    time2.update(newtime = '14/6/13', form='DMYY') # wrong format
    time2.display()
    print

    mytime.show_format()
    

if __name__=='__main__':
    testMytime()
