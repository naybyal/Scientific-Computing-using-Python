from tkinter import *
from tkinter import ttk
class LabelDemo(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Button Demo")
        self.grid()
        self._label = Label(self, text="Hello")
        self._label.grid()  
        self._button = ttk.Button(self, text="Click Me")
        self._button.grid()

def main():
    LabelDemo().mainloop()

if __name__ == "__main__":
    main()
