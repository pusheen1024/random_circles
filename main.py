import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


def hex2rgb(color):
    return f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'


def except_hook(cls, exception, traceback):
    sys.__excepthook(cls, exception, traceback)
    
    
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.draw_flag = False
        
    def draw(self):
        self.draw_flag = True
        self.update()
        
    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            for _ in range(randint(5, 10)):
                color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
                color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
                qp.setBrush(QColor(hex2rgb(color1)))
                qp.setPen(QColor(hex2rgb(color2)))
                radius = randint(1, 100)
                qp.drawEllipse(randint(0, 800), randint(80, 600), radius, radius)
            qp.end()
                
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
