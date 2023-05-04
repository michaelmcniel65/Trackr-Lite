import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter
import sqlite3

conn = sqlite3.connect('trackr.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not exists bug_list(
    list_item text) 
    """)

conn.commit()
conn.close()

class Ui_window2(QObject):
    submitted = QtCore.pyqtSignal(str)
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(712, 236)
        window2.setStyleSheet("background: rgb(190, 4, 23)")
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.add_task_label = QtWidgets.QLabel(self.centralwidget)
        self.add_task_label.setGeometry(QtCore.QRect(10, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("VT323")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.add_task_label.setFont(font)
        self.add_task_label.setStyleSheet("color: white")
        self.add_task_label.setObjectName("add_task_label")
        self.new_task_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.new_task_lineedit.setGeometry(QtCore.QRect(10, 100, 681, 31))
        self.new_task_lineedit.setStyleSheet("background: white")
        self.new_task_lineedit.setObjectName("new_task_lineedit")
        self.new_task_description = QtWidgets.QLabel(self.centralwidget)
        self.new_task_description.setGeometry(QtCore.QRect(10, 50, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.new_task_description.setFont(font)
        self.new_task_description.setStyleSheet("color: white\n"
"")
        self.new_task_description.setWordWrap(True)
        self.new_task_description.setObjectName("new_task_description")
        self.create_task_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.onSubmit())
        self.create_task_button.setGeometry(QtCore.QRect(10, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_task_button.setFont(font)
        self.create_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_task_button.setStyleSheet("background: rgb(52, 52, 52);\n"
"border-radius:5px;\n"
"color: white;")
        self.create_task_button.setObjectName("create_task_button")
        window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 21))
        self.menubar.setObjectName("menubar")
        window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window2)
        self.statusbar.setObjectName("statusbar")
        window2.setStatusBar(self.statusbar)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def onSubmit(self):
        self.submitted.emit(self.new_task_lineedit.text())
        self.new_task_lineedit.setText("")
        dialog = QMessageBox()
        dialog.setText('Task successfully added!')
        dialog.setWindowTitle('Task Added')
        dialog.exec_()

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "Add New Task"))
        self.add_task_label.setText(_translate("window2", "Add New Task"))
        self.new_task_description.setText(_translate("window2", "Tasks should be short and percise. Please do not use words that do not identify the problem for others such as nicknames, unknown abbreviations, etc. Please use professional language when writing tasks."))
        self.create_task_button.setText(_translate("window2", "Create Task"))

class Ui_window1(QObject):
    def setupUi(self, window1):
        window1.setObjectName("window1")
        window1.resize(930, 563)
        window1.setStyleSheet("background: rgb(190, 4, 23)")
        self.centralwidget = QtWidgets.QWidget(window1)
        self.centralwidget.setObjectName("centralwidget")
        self.bug_list_label = QtWidgets.QLabel(self.centralwidget)
        self.bug_list_label.setGeometry(QtCore.QRect(20, 0, 371, 71))
        font = QtGui.QFont()
        font.setFamily("VT323")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.bug_list_label.setFont(font)
        self.bug_list_label.setStyleSheet("color: white")
        self.bug_list_label.setObjectName("bug_list_label")
        self.add_task_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2())
        self.add_task_button.setGeometry(QtCore.QRect(740, 120, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_task_button.setFont(font)
        self.add_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_task_button.setStyleSheet("background: rgb(52, 52, 52);\n"
"border-radius:5px;\n"
"color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Users/Michael/Desktop/icons/icons/blog--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_task_button.setIcon(icon)
        self.add_task_button.setObjectName("add_task_button")
        self.complete_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.completeTask())
        self.complete_button.setGeometry(QtCore.QRect(740, 180, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.complete_button.setFont(font)
        self.complete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.complete_button.setStyleSheet("background: rgb(52, 52, 52);\n"
"border-radius:5px;\n"
"color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Users/Michael/Desktop/icons/icons/blue-document-attribute-c.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.complete_button.setIcon(icon1)
        self.complete_button.setObjectName("complete_button")
        self.export_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pdfexport())
        self.export_button.setGeometry(QtCore.QRect(740, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.export_button.setFont(font)
        self.export_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_button.setStyleSheet("background: rgb(52, 52, 52);\n"
"border-radius:5px;\n"
"color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Users/Michael/Desktop/icons/icons/blogs-stack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_button.setIcon(icon2)
        self.export_button.setObjectName("export_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save())
        self.save_button.setGeometry(QtCore.QRect(20, 90, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_button.setStyleSheet("background: rgb(52, 52, 52);\n"
"border-radius:5px;\n"
"color: white;")
        self.save_button.setObjectName("save_button")
        self.bug_list = QtWidgets.QListWidget(self.centralwidget)
        self.bug_list.setGeometry(QtCore.QRect(20, 120, 711, 391))
        self.bug_list.setStyleSheet("background: white;")
        self.bug_list.setObjectName("bug_list")
        window1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        window1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window1)
        self.statusbar.setObjectName("statusbar")
        window1.setStatusBar(self.statusbar)

        self.retranslateUi(window1)
        QtCore.QMetaObject.connectSlotsByName(window1)

        self.getItems()

    def getItems(self):
        conn = sqlite3.connect('trackr.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bug_list")
        records = cursor.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            self.bug_list.addItem(str(record[0]))

    @QtCore.pyqtSlot(str)
    def updateList(self, task):
        self.bug_list.addItem(task)

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window2()
        self.ui.setupUi(self.window)
        self.ui.submitted.connect(self.updateList)
        self.window.show()

    def completeTask(self):
        selected = self.bug_list.currentRow()
        self.bug_list.takeItem(selected)

    def save(self):
        conn = sqlite3.connect('trackr.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bug_list;",)
        items = []
        for index in range(self.bug_list.count()):
            items.append(self.bug_list.item(index))
        for item in items:
            cursor.execute("INSERT INTO bug_list VALUES (:item)",
                           {
                               'item': item.text(),
                           })
        conn.commit()
        conn.close()
        msg = QMessageBox()
        msg.setWindowTitle('Save Successful')
        msg.setText('Your Progress Has Been Saved.')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def print_widget(bug_list, filename):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QPrinter(printer)
        xscale = printer.pageRect().width() * 1.0 / bug_list.width()
        yscale = printer.pageRect().height * 1.0 / bug_list.height()
        scale = min(xscale, yscale)
        painter.translate(printer.paperRect().center())#set as center here 
        painter.scale(scale, scale)
        painter.translate(-bug_list.width()/2, -bug_list.height()/2)
        bug_list.render(painter)
        painter.end()

    def pdfexport(self):
        test = QtWidgets.QFileDialog.getSaveFileName(
            self.bug_list, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        self.print_widget(self.bug_list, test)

    def retranslateUi(self, window1):
        _translate = QtCore.QCoreApplication.translate
        window1.setWindowTitle(_translate("window1", "Trackr Lite"))
        self.bug_list_label.setText(_translate("window1", "Bug List"))
        self.add_task_button.setText(_translate("window1", "Add New Task"))
        self.complete_button.setText(_translate("window1", "Complete"))
        self.export_button.setText(_translate("window1", "Export List"))
        self.save_button.setText(_translate("window1", "Save List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window1 = QtWidgets.QMainWindow()
    ui = Ui_window1()
    ui.setupUi(window1)
    window1.show()
    sys.exit(app.exec_())
