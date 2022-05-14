from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import *
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.name = QLabel(txt_name)
        self.age = QLabel(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.stest1 = QPushButton(txt_starttest1)
        self.stest2 = QPushButton(txt_starttest2)
        self.stest3 = QPushButton(txt_starttest3)
        self.age2 = QLineEdit()
        self.name2 = QLineEdit()
        self.sendres = QPushButton(txt_sendresults)
        self.timer = QLabel(txt_time)
        self.time1 = QLineEdit(txt_hinttest1)
        self.time2 = QLineEdit(txt_hinttest2)
        self.time3 = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.name2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.age2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.stest1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.time1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.r_line.addWidget(self.timer, alignment= Qt.AlignRight)
        self.l_line.addWidget(self.stest2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.stest3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.time2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.time3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.sendres, alignment= Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.sendres.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()

app = QApplication([])
mainwin = MainWin()
app.exec_()