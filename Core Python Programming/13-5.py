# 13-5 and 13-6

class Point(object):
    '''
        point class
    '''

    points = 0    

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        print 'point ({x},{y}) created.'.format( x=self.__x, y=self.__y )
        Point.points += 1
        # print '%s.%s called.'%(self.__class__, __name__) # how to print this function's name?

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return "(%d, %d)"%(self.__x, self.__y)

    def __repr__(self):
        return "Point: (%d, %d)"%(self.__x, self.__y)

    @classmethod    # must use this decorator operator
    def countPoint(self):   # self must be explicit
        '''
        class method: calcule how many points there are
        '''
        return Point.points

    def __del__(self):
        Point.points -= 1


class Line(object):
    '''
    line class
    '''

    def __init__(self, start_point=None, end_point=None):
        print 'Line.__init__ is calling.'
        if start_point is None:
            start_point = Point()
        self.start = start_point
        if end_point is None:
            end_point = Point()
        self.end = end_point

    def __str__(self):    
        return "((%d,%d)-->(%d,%d))"%(self.start.get_x(), \
                                     self.start.get_y(), \
                                     self.end.get_x(), \
                                     self.end.get_y())

# WTF: when executing this file, definition of class Line will call Point.__init__ twice.

def test_point():
    point_a = Point(1,2)
    point_b = Point()
    point_c = Point(y=3)
    point_d = Point(x=4)
    
    print point_c

    print Point.points

def test_line():
    p1 = Point(1,1)
    p2 = Point(2,2)
    line1 = Line(p1, p2)
    print line1

    line2 = Line(Point(1,2),Point(3,4)) # Line((1,2),(3,4)) is wrong: \
                # AttributeError: 'tuple' object has no attribute 'get_x'
                # 
                # We may use collections.namedtuple() as:
                #
                # Point = collecitons.namedtuple('Point', 'x y')
                # point_a = Point(1,2)
                # 
                # Or:
                # class Point(collections.namedtuple('Point', 'x y')):
                # ...w
                 
    print line2
    
if __name__=='__main__':
    test_line()
    
