import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 500)
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hello", self)
        self.initUI()
    
    def initUI(self):
        self.button.setGeometry(150, 100, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 200, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.label.setText("GoodBye")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())