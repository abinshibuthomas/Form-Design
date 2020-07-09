import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QLineEdit,QLabel,QTextEdit,QFormLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Details")
        self.setWindowIcon(QtGui.QIcon("hacker.png"))
        self.resize(350,350)
        self.move(250,250)

        layout = QFormLayout(self)
        self.setLayout(layout)

        label =QLabel("Name", self)
        edit =QLineEdit(self)
        layout.addRow(label,edit)

        labe2 = QLabel("Address", self)
        edit2 = QTextEdit(self)
        layout.addRow(labe2, edit2)

        labe3 = QLabel('Phone Number',self)
        edit3 = QLineEdit(self)
        layout.addRow(labe3,edit3)

        labe4=QLabel('Email id')
        edit4 = QLineEdit(self)
        layout.addRow(labe4,edit4)


        button = QPushButton("Submit",self)
        button.clicked.connect(QApplication.instance().quit)
        # layout.addRow('',button)
        layout.addRow(button)

        button1= QPushButton("Cancel",self)
        button1.clicked.connect(QApplication.instance().quit)
        layout.addRow(button1)

        self.show()
















def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()