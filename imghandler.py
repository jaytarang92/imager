import tkMessageBox
import subprocess

class Cloner:
    def __init__(self):
        self.run = subprocess.call
        self.ret = Retcode()

    def gfxarun(self):
        gfxar = self.run('crap.bat1', shell=True)
        self.ret.checker(gfxar)

    def gfxbrun(self):
        gfxbr = self.run('echo "GFXB"', shell=True)
        self.ret.checker(gfxbr)

class Messengers:
    def __init__(self):
        self.box = tkMessageBox

    def successer(self):
        self.box.showinfo("ImageR Success", "Done YO! Go run a test :)")

    def failure(self):
        self.box.showerror('ImageR Failure', 'Yo you broke me!')

class Retcode:
    def __init__(self):
        self.msgrs = Messengers()

    def checker(self, cmd):
        if cmd != 0:
             self.msgrs.failure()
        else:
            self.msgrs.successer()
