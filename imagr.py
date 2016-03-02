import Tkinter
from imghandler import *

win = Tkinter.Tk()
win.title('Apple Test ImageR')
win.geometry('300x400')

imager = {
    0: Cloner().gfxarun,
    1: Cloner().gfxbrun
}

gfxar = Tkinter.Button(win, text ="GFXA Runnin", command = imager[0]).pack()
gfxbr = Tkinter.Button(win, text ="GFXB Runnin", command = imager[1]).pack()

if __name__ == '__main__':
    win.mainloop()
