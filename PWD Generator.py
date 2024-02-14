import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password1 = ""
pwd = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setFixedHeight(360)
        self.setFixedWidth(480)


        button1 = QPushButton("Press Me To Generate Password", self)
        button1.setGeometry(110, 80, 250, 40)  # (x, y, width, height)
        button1.clicked.connect(self.generatepassword)

        button2 = QPushButton("Press Me To Save Password", self)
        button2.setGeometry(110, 160, 250, 40)  # (x, y, width, height)
        button2.clicked.connect(self.storepassword)

        global password1
        password1 = QLabel("Password Generated: ", self)
        password1.setGeometry(100, 300, 500, 40)  # (x, y, width, height)
        password1.setTextInteractionFlags(Qt.TextSelectableByMouse)



    def generatepassword(self):

        nr_letters = 5
        nr_symbols = 5
        nr_numbers = 5
        password_list = []

        for char in range(1, nr_letters + 1):
            password_list.append(random.choice(letters))

        for char in range(1, nr_symbols + 1):
            password_list.append(random.choice(numbers))

        for char in range(1, nr_numbers + 1):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        # convert list to string
        global pwd
        pwd = ''.join(password_list)
        password1.setText("Password Generated: " + pwd)
        print(f"Your random password to use is: {pwd}")

    def storepassword(self):
        print("Password stored")
        with open('passwords.txt', 'a') as file:
            file.write("Password: " + pwd + "\n")




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
