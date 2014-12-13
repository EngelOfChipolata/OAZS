from tkinter import *
import time

class SplashScreen(Frame):
    def __init__(self, master=None, width=0.2, height=0.05, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws*width) or width
        h = (useFactor and ws*height) or height
        # calculate position x, y
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.master.overrideredirect(True)
        self.lift()
        self.bind('<ButtonPress-1>', self.move())
    def move(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        self.master.geometry("+%s+%s" % (x, y))


if __name__ == '__main__':
    root = Tk()

    sp = SplashScreen(root)
    sp.config(bg="#3366ff")

    m = Label(sp, text="The sun is setting")
    m.pack(side=TOP, expand=YES)
    m.config(bg="#3366ff", justify=CENTER, font=("calibri", 19))

    root.mainloop()