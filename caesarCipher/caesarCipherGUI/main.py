from tkinter import *
from tkinter import ttk
global distance

def ceasarEncrypt(message):
    encryptedMessage = ""

    for ch in message:
        ordinalValue = ord(ch)
        cipherValue = ordinalValue + distance

        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordinalValue + 1)
        encryptedMessage += chr(cipherValue)
    return encryptedMessage


def ceasarDecrypt(encryptedMessage):
    message = ""
    for ch in encryptedMessage:
        cipherValue = ord(ch)
        originalValue = cipherValue - distance
        if originalValue < ord('a'):
            originalValue = ord('z') - distance + (ord('z') - cipherValue + 1)
        message += chr(originalValue)
    return message



root = Tk()
root.title("Ceasar Cipher!")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(N, W, E, S))

message_label = ttk.Label(frame, text='Enter your message ')
message_entry = ttk.Entry(frame)

distance_label = ttk.Label(frame, text='Enter the distance ')
distance_entry = ttk.Entry(frame)

submit_btn = ttk.Button(frame, text='Encrypt', command=ceasarEncrypt)

message_label.grid(column=0, row=0, sticky=W)  # Used 'sticky' to align the widgets to the left
message_entry.grid(column=1, row=0, sticky=(W, E))  # Used 'sticky' to expand the entry widget horizontally
distance_label.grid(column=0, row=1, sticky=W)  # Used 'sticky' to align the widgets to the left
distance_entry.grid(column=1, row=1, sticky=(W, E))  # Used 'sticky' to expand the entry widget horizontally
submit_btn.grid(column=1, row=2, sticky=W)  # Changed row number to match the row where the other widgets are placed


# message_label.pack()
# message_entry.pack()
# distance_label.pack()
# distance_entry.pack()

root.mainloop()

