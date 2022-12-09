import sys, tkinter, pygame
import memorypuzzle, paint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QFile
from menu_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.drawButton.show()
        self.ui.drawButton.clicked.connect(self.start_paint)
        
        self.ui.guessButton.show()
        self.ui.guessButton.clicked.connect(self.start_memorypuzzle)
    
    def start_paint(self):
        root = tkinter.Tk()
        paint.main(root)
        root.title('ChildPaint')
        root.mainloop()
    
    def start_memorypuzzle(self):
        memorypuzzle.main()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())