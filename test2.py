from tkinter import *

class blah:
    def startMoveWindow(self, event):
## When the movement starts, record current root coordinates
        self.__lastX, self.__lastY = event.x_root, event.y_root

    def MoveWindow(self, event):
        self.root.update_idletasks()
## Use root coordinates to compute offset for inside window coordinates
        self.__winX += event.x_root - self.__lastX
        self.__winY += event.y_root - self.__lastY
## Remember last coordinates
        self.__lastX, self.__lastY = event.x_root, event.y_root
## Move inside window
        self.root.place_configure(x=self.__winX, y=self.__winY)

    def __init__(self):
        self.root = Tk()
        self.root.title("...")
        self.root.resizable(0,0)
        self.root.geometry("%dx%d%+d%+d"%(640, 480, 0, 0))

## Record coordinates for window to avoid asking them every time
        self.__winX, self.__winY = 0, 0
        # self.f = Frame(self.root, bd=1, relief=SUNKEN)
        # self.root.place(x=self.__winX, y=self.__winY, width=200, height=200)
        #
        # self.l = Label(self.f, bd=1, relief=RAISED, text="Test")
        # self.l.pack(fill=X, padx=1, pady=1)

## When the button is pressed, make sure we get the first coordinates
        self.root.bind('<ButtonPress-1>', self.startMoveWindow)
        self.root.bind('<B1-Motion>', self.MoveWindow)
        self.root.bind('<ButtonPress-1>', self.startMoveWindow)
        self.root.bind('<B1-Motion>', self.MoveWindow)

        self.root.mainloop()

x = blah()