#   import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

#   main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Generator")
main_window.resize(600,200)

#   creating all widgets needed in the app
title = QLabel("Random Keywords...")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

my_words = [
    "kernel", "bash", "Ubuntu", "grep", "sed", "awk", "terminal", "shell", "daemon", "filesystem",
    "Orwell", "Austen", "Dickens", "Homer", "Tolstoy", "Shakespeare", "Faulkner", "Joyce", "Dostoevsky", "Fitzgerald",
    "saxophone", "bebop", "improvisation", "swing", "syncopation", "Davis", "Coltrane", "Ellington", "Mingus", "Gillespie",
    "blues", "slide", "harmonica", "shuffle", "riff", "King", "Waters", "Hooker", "Johnson", "Howlin",
    "rock", "guitar", "drums", "bass", "band", "Zeppelin", "Beatles", "Hendrix", "Jagger", "Stones",
    "computer", "software", "hardware", "algorithm", "AI", "machine", "learning", "robotics", "programming", "cybersecurity",
    "whiskey", "vodka", "rum", "beer", "wine", "cocktail", "bourbon", "tequila", "gin", "brandy",
    "Debian", "Fedora", "Slackware", "Gentoo", "Mint", "Arch", "Suse", "RedHat", "man", "vim",
    "Hemingway", "Steinbeck", "Salinger", "Kafka", "Baldwin", "Woolf", "Proust", "Eliot", "Melville", "Poe",
    "Armstrong", "Holiday", "Fitzgerald", "Basie", "Parker", "Newman", "Washington", "Rollins", "Blakey", "Smith",
    "CLI", "cron", "chmod", "chown", "ps", "top", "htop", "uptime", "ping", "ssh",
    "Joyce", "Shelley", "Conrad", "Wharton", "Tolkien", "Gaiman", "Huxley", "Lawrence", "Bronte", "Gibson",
    "Blue", "Note", "Improvisation", "Chord", "Jazz", "Club", "Swing", "Groove", "Cool", "Free",
    "Delta", "Blues", "Electric", "Acoustic", "Slide", "Bottleneck", "Shuffling", "Soul", "Funk", "Roots",
    "Rock", "Roll", "Hard", "Soft", "Punk", "Metal", "Alternative", "Grunge", "Indie", "Classic",
    "Tech", "Cyber", "Hack", "Script", "Code", "Database", "Network", "Cloud", "Server", "Client",
    "Beer", "Ale", "Lager", "Pilsner", "Stout", "Porter", "Cider", "Mead", "Sake", "Spirit",
    "KDE", "GNOME", "XFCE", "LXDE", "Mate", "Cinnamon", "Unity", "Openbox", "Fluxbox", "Awesome",
    "Dickens", "Gogol", "Nabokov", "Flaubert", "Hesse", "Zola", "Stendhal", "Eco", "Foster", "Wright",
    "Gershwin", "Miller", "Goodman", "Shaw", "Rich", "Brown", "Carter", "Roach", "Jones", "Adderley",
    "Blues", "Ragtime", "Chicago", "Memphis", "New", "Orleans", "Piedmont", "Urban", "Jump", "Texas",
    "Rock", "Riff", "Chord", "Progression", "Scale", "Solo", "Ballad", "Cover", "Gig", "Jam",
    "Java", "Python", "C++", "JavaScript", "Ruby", "Perl", "Swift", "Go", "R", "MATLAB",
    "Mojito", "Martini", "Daiquiri", "Margarita", "Cosmopolitan", "Negroni", "Manhattan", "Old", "Fashioned", "Mai",
    "Slack", "Terminal", "Package", "Manager", "Repository", "Build", "Script", "Compiler", "Interpreter", "Debugger",
    "Mitchell", "Hurston", "Wright", "O'Connor", "Morrison", "Capote", "Welty", "Ellison", "Styron", "Wolfe",
    "Baker", "Armstrong", "Ellington", "Holiday", "Fitzgerald", "Mingus", "Parker", "Blakey", "Rollins", "Smith",
    "Delta", "Country", "Electric", "Acoustic", "Chicago", "Texas", "Piedmont", "Jump", "Boogie", "Soul",
    "Alternative", "Grunge", "Metal", "Punk", "Classic", "Progressive", "Indie", "Garage", "Glam", "New",
    "Data", "Mining", "Machine", "Learning", "Deep", "Neural", "Network", "Algorithm", "Database", "Big",
    "Cocktail", "Martini", "Negroni", "Old", "Fashioned", "Margarita", "Daiquiri", "Cosmopolitan", "Mojito", "Mai"
]


button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")


#   designing the layout
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

#   setting the final layout to the main window
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

#   add functions

def generate_random_word1():
    word = choice(my_words)
    text1.setText(word)

def generate_random_word2():
    word = choice(my_words)
    text2.setText(word)

def generate_random_word3():
    word = choice(my_words)
    text3.setText(word)



#   event handling
button1.clicked.connect(generate_random_word1)
button2.clicked.connect(generate_random_word2)
button3.clicked.connect(generate_random_word3)


#   showing and executing the app
main_window.show()
app.exec_()