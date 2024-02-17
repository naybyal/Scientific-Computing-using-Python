#       Height Calculator

'''
window = Tk()                           #   Initialize/Create a basic window.
window.title("Calc+")                   #   Title of the window.
window.geometry("500x500")              #   Window size.
window.resizable(False,False)       #   Prevents user from resizing the window.

btn_frame = Frame(window, width=300, height=300, bg="grey")

btn_frame.pack()

#def buttonClick():


window.mainloop()

'''
import math
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(meter.get())
        #   meters = (0.3048 * feet * 10000.0 + 0.5) / 10000.0

        #   feet = ((meters * 10000.0) - 0.5)/(0.3045 * 10000.0)
        feet.set(round(int((value * 10000.0) - 0.5)/(0.3045 * 10000.0),6))
    except ValueError:
        pass

root = Tk()
root.title("Meters to Feet")
root.resizable(False,False)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

meter = StringVar()
meter_entry = ttk.Entry(mainframe, width=7, textvariable=meter)
meter_entry.grid(column=2, row=1, sticky=(W, E))

feet = StringVar()
ttk.Label(mainframe, textvariable=feet).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="meters").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="feet").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

meter_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()