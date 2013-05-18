# sample of closure from 11.8.4
#
# i added ww, and change clo in f1() to clo1

output = '<int> %r id=%#0x val=%d'
w=x=y=z=1
ww=0

def f1():
    x=y=z=2
    ww=1

    def f2():
        y=z=3
        ww=3

        def f3():
            z=4
            print output%('w',id(w),w)
            print output%('x',id(x),x)
            print output%('y',id(y),y)
            print output%('z',id(z),z)
            print output%('ww',id(ww),ww)

        clo = f3.func_closure
        if clo:
            print "f3 closure vars:",[str(c) for c in clo]
        else:
            print "no f3 clusure vars."

        f3()

    clo1 = f2.func_closure
    if clo1:
        print "f2 closure vars:",[str(c) for c in clo1]
    else:
        print "no f2 clusure vars."

    f2()

clo = f1.func_closure
if clo:
    print "f1 closure vars:",[str(c) for c in clo]
else:
    print "no f1 clusure vars."

f1()
