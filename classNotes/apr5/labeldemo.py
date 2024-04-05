from tkinter import *

class LabelDemo(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Label Demo")
        self.grid()
        self._label = Label(self, text="Hello World")
        self._label.grid()  

def main():
    LabelDemo().mainloop()

if __name__ == "__main__":
    main()
