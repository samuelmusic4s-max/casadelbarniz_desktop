
from PySide6.QtWidgets import QWidget, QApplication, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.resize(1200, 2000)
        titulo =QLabel("Hola",self)
        titulo.move(1000, 1900)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()