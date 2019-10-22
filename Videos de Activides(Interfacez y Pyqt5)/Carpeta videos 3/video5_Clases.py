from PyQt5 import QtCore, QtWidgets
from video5_Main import Ui_MainWindow 

class DragDropButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())



class DragDropCombo(QtWidgets.QComboBox):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

            
  
class MainWindow_EXEC():

    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        print("Yes")

        #----------------
        self.ui.comboBox.hide()
        self.drop_combo = DragDropCombo(MainWindow)
        self.drop_combo.setMinimumSize(QtCore.QSize(141,0))
        self.ui.horizontalLayout_2.addWidget(self.drop_combo)

        #------------------
        self.ui.pushButton.hide()
        self.drop_button = DragDropButton('DropButton',MainWindow)
        self.drop_button.setMinimumSize(QtCore.QSize(161,0))
        self.ui.horizontalLayout_2.addWidget(self.drop_button)
        #-----------------------------
        #self.update_tree()
        #self.update_calendar()
        #self.update_progressbar()

        MainWindow.show()
        sys.exit(app.exec_())

    #def update_tree(self):
        #self.ui.treeWidget.headerItem().setText(1, 'Header 2')
        #self.ui.treeWidget.topLevelItem(0).setText(1, "Item 2")
        #self.ui.treeWidget.topLevelItem(0).addChild(QtWidgets.QTreeWidgetItem())
        #self.ui.treeWidget.topLevelItem(0).child(0).setText(1,"Sub-Item2")


MainWindow_EXEC()




        
        


                                           
