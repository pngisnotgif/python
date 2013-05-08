from Tkinter import *
from tkinter102 import MyGUI

# main app window
mainWin = Tk()
Label(mainWin, text='I am the main window').pack()

# popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT)
mainWin.mainloop()

