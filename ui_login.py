from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 400, 300)

        # Create and set font
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

        # Create widgets
        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 50)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 100)

        self.username_input = QLineEdit(self)
        self.username_input.move(150, 50)
        self.username_input.setFixedWidth(200)

        self.password_input = QLineEdit(self)
        self.password_input.move(150, 100)
        self.password_input.setFixedWidth(200)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(150, 150)
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        # Check if credentials are valid
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            print("Login successful!")
        else:
            print("Invalid credentials.")


if __name__ == "__main__":
    app = QApplication([])
    login_page = LoginPage()
    login_page.show()
    app.exec_()
