#   imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

#   app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("QtCalc Basic")
main_window.resize(300,350)

#   widgets
text_box = QLineEdit()
grid = QGridLayout()

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "0",".", "=", "+"
]

clear_button = QPushButton("Clear")
delete_button = QPushButton("Delete")

#   event handling
def button_click():
    button = app.sender()
    text = button.text()

    if (text == "="):
        symbol = text_box.text()
        try:
            res = eval(symbol)
            text_box.setText(str(res))
        except Exception as e:
            print("Error : ", e)

    elif (text == "Clear"):
        text_box.clear()

    elif (text == "Delete"):
        current_value = text_box.text()
        text_box.setText(current_value[:-1])
    
    else:
        current_value = text_box.text()
        text_box.setText(current_value + text)


#   design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

col = 0
row = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)

    col += 1

    if (col > 3):
        col = 0
        row += 1



clear_button.clicked.connect(button_click)
delete_button.clicked.connect(button_click)

button_row = QHBoxLayout()
button_row.addWidget(clear_button)
button_row.addWidget(delete_button)



master_layout.addLayout(button_row)
main_window.setLayout(master_layout)
#   show/execute
main_window.show()
app.exec_()