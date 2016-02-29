import Tkinter
import subprocess

top = Tkinter.Tk()

class Cloner:
    def __init__(self):
        pass
    def gfxarun(self):
       subprocess.call('echo "GFXA"', shell=True)
    def gfxbrun(self):
       subprocess.call('echo "GFXB"', shell=True)

imager = {
    0: Cloner().gfxarun,
    1: Cloner().gfxbrun
}

gfxar = Tkinter.Button(top, text ="GFXA Runnin", command = imager[0])
gfxbr = Tkinter.Button(top, text ="GFXB Runnin", command = imager[1])

gfxar.pack()
gfxbr.pack()
top.mainloop()
