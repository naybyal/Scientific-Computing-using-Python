from tkinter import *
from tkinter import ttk

class ImageDemo(frame):
    def __init__(self):
        frame.__init__(self)
        self.master.title("Image Demo")
        self.grid()
        self._image = PhotoImage(file='strsd.png')
        self._imageLabel = Label(self, image=self._image)
        self._imageLabel.grid()
        self._textLabel = Label(self, text="anime wallpaper")
        self._textLabel.grid()


root = Tk()
frame = ttk.Frame()
image = ImageDemo(frame)


