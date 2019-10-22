

import sys
from time import sleep
from pprint import pprint
import sqlite3
from PyQt5 import QtSql
from PyQt5 import QtCore, QtWidgets
from Video3_base import Ui_MainWindow                                  
from PyQt5.QtGui import QColor


class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 


        #-------------------------- 
        #self.init_tabs()
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 

                       


class RunThread(QtCore.QThread):   
    counter_value = QtCore.pyqtSignal(int)             
    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True
        
    def run(self):
        while self.counter < 100 and self.is_running == True:
            sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)     
            
    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()



         
        
if __name__ == "__main__":
    MainWindow_EXEC()
