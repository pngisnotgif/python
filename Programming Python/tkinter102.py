'''
    Tkinter example.
'''
from Tkinter import *
from tkMessageBox import showinfo

class MyGUI(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')

if __name__=='__main__':
    window = MyGUI()
    window.pack()
    window.mainloop()

    
