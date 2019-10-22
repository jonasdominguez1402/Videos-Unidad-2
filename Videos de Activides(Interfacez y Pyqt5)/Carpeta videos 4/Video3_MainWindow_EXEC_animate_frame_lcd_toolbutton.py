import sys
from time import sleep
from pprint import pprint
import sqlite3
from PyQt5 import QtSql
from PyQt5 import QtCore, QtWidgets
from Video3_base import Ui_MainWindow                                  
from PyQt5.QtGui import QColor


class MoveToolButton(QtWidgets.QToolButton):
    
    def __init__(self, parent):
        super().__init__(parent)  
        self.change_palette()
    def change_palette(self, back=QColor("#bd0000"), fore=QColor("#bd125c")):    
        palette = self.palette()
        palette.setColor(self.backgroundRole(), back)
        palette.setColor(self.foregroundRole(), fore)
        self.setPalette(palette)     
    def position_button(self, new_position):    
        self.move(new_position.x(), new_position.y())
    new_position = QtCore.pyqtProperty(QtCore.QPoint, fset=position_button)   # define a new property       
class MainWindow_EXEC():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        
        self.ui.button_stop_animation.clicked.connect(self.stop_animation)
        self.ui.button_start_animation.clicked.connect(self.animate)

        self.ui.toolButton.hide()
        self.move_toolbutton = MoveToolButton(self.ui.tab_animation)
        self.move_toolbutton.setGeometry(QtCore.QRect(330, 20, 25, 19))
        self.move_toolbutton.setAutoFillBackground(True)
        self.move_toolbutton.setText("***")
        #-------------------------- 
        self.MainWindow.show()
        sys.exit(app.exec_()) 
    #----------------------------------------------------------
    def stop_animation(self):
        try:
            self.animated_frame.stop()
            self.animated_lcd.stop()
            self.animated_toolbutton.stop()
        except: pass
        
    #----------------------------------------------------------
    def animate(self):
        self.animated_frame = QtCore.QPropertyAnimation(self.ui.frame, b'geometry')
        self.animated_frame.setDuration(10000)
        self.animated_frame.setStartValue(QtCore.QRect(10, 10, 100, 100))
        self.animated_frame.setEndValue(QtCore.QRect(10, 10, 200, 200))
        self.animated_frame.start()
        self.animated_frame.finished.connect(lambda: self.ui.frame.setFrameStyle(QtWidgets.QFrame.Box))  
        self.animated_lcd = QtCore.QPropertyAnimation(self.ui.lcdNumber_animation, b'value')
        self.animated_lcd.setDuration(9000)
        self.animated_lcd.setStartValue(0)
        self.animated_lcd.setEndValue(999)
        self.animated_lcd.start()
        self.animated_lcd.finished.connect(lambda: self.ui.lcdNumber_animation.setFrameStyle(QtWidgets.QFrame.StyledPanel))   
        self.move_toolbutton.change_palette()   # reset to default colors  
        self.animated_toolbutton = QtCore.QPropertyAnimation(self.move_toolbutton, b'new_position')
        self.animated_toolbutton.setDuration(9000)
        self.animated_toolbutton.setStartValue(QtCore.QPoint(330, 20))
        self.animated_toolbutton.setKeyValueAt(0.2, QtCore.QPoint(398, 50))
        self.animated_toolbutton.setKeyValueAt(0.5, QtCore.QPoint(152, 120))
        self.animated_toolbutton.setKeyValueAt(0.6, QtCore.QPoint(420, 240))
        self.animated_toolbutton.setKeyValueAt(0.7, QtCore.QPoint(420, 260))
        self.animated_toolbutton.setKeyValueAt(0.9, QtCore.QPoint(330, 330))
        self.animated_toolbutton.setKeyValueAt(0.99, QtCore.QPoint(330, 310))
        self.animated_toolbutton.setEndValue(QtCore.QPoint(490, 300))
        self.animated_toolbutton.start()
        self.animated_toolbutton.finished.connect(lambda: self.move_toolbutton.change_palette(QColor('#00aa00'), QColor('#00aa00')))

    
         
        
if __name__ == "__main__":
    MainWindow_EXEC()
