import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY First GUI")
        self.setGeometry(400, 200, 700, 500)
        self.setWindowIcon(QIcon("user.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,700,100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;")
        # label.setAlignment(Qt.AlignTop) # Vertically top
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignLeft)

        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) #  center and center
        label.setAlignment(Qt.AlignCenter) # Shortcut for the above code

        # image using label
        labelImg = QLabel(self)
        labelImg.setGeometry(0,100,400,400)

        pixmap = QPixmap("user.jpg")
        labelImg.setPixmap(pixmap)
        labelImg.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()