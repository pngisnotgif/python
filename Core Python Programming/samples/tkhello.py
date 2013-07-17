
# from chapter #19

from Tkinter import *

def resize(en=None):
    label.config(font='Helvetica -%d bold'%scale.get())
    
top = Tk()
top.geometry('250x150') # lower letter x between digits

label = Label(top, text='Hello world!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=True)

b_quit = Button(top, text='QUIT', command=top.quit,
                        activebackground='red', activeforeground='yellow')  # color doesn't work in Mac.
b_quit.pack(fill=X, expand=1)   # using IDLE in Mac, this line will not respond.

mainloop()
