from tkinter import *
from tkinter import ttk

def ceasarEncrypt():
    # Your Caesar Cipher encryption logic here
    pass

root = Tk()
root.title("Caesar Cipher!")  # Fixed the typo in the title

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(N, W, E, S))  # Placed the frame in the root window

message_label = ttk.Label(frame, text='Enter your message ')
message_entry = ttk.Entry(frame)  # Placed the entry widget inside the frame

distance_label = ttk.Label(frame, text='Enter the distance ')
distance_entry = ttk.Entry(frame)  # Placed the entry widget inside the frame

submit_btn = ttk.Button(frame, text='Encrypt', command=ceasarEncrypt)

message_label.grid(column=0, row=0, sticky=W)  # Used 'sticky' to align the widgets to the left
message_entry.grid(column=1, row=0, sticky=(W, E))  # Used 'sticky' to expand the entry widget horizontally
distance_label.grid(column=0, row=1, sticky=W)  # Used 'sticky' to align the widgets to the left
distance_entry.grid(column=1, row=1, sticky=(W, E))  # Used 'sticky' to expand the entry widget horizontally
submit_btn.grid(column=2, row=2, sticky=W)  # Changed row number to match the row where the other widgets are placed

root.mainloop()
