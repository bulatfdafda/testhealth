from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.l_line = QVBoxLayout()
        self.heart = QLabel(txt_workheart + self.results())
        self.python = QLabel(txt_index + str(self.index))
        self.l_line.addWidget(self.python, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.heart, alignment= Qt.AlignCenter)
        self.setLayout(self.l_line)
    def results(self):
        self.index = (4*(int(self.exp.test1)+int(self.exp.test2)+int(self.exp.test3))-200)/10
        if self.exp.age >= 7 and self.exp.age < 9:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index < 21:
                return txt_res2
            elif self.index >= 12 and self.index < 17:
                return txt_res3
            elif self.index >= 6 and self.index < 12:
                return txt_res4
            elif self.index < 6:
                return txt_res5
        if self.exp.age >= 9 and self.exp.age < 11:
            if self.index >= 19:
                return txt_res1
            elif self.index >= 15 and self.index < 19:
                return txt_res2
            elif self.index >= 10 and self.index < 15:
                return txt_res3
            elif self.index >= 5 and self.index < 10:
                return txt_res4
            elif self.index < 5:
                return txt_res5
        if self.exp.age >= 11 and self.exp.age <=13:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index < 18:
                return txt_res2
            elif self.index >= 9 and self.index < 14:
                return txt_res3
            elif self.index >= 3 and self.index < 9:
                return txt_res4
            elif self.index <3:
                return txt_res5
        if self.exp.age >= 13 and self.exp.age < 15:
            if self.index >= 16:
                return txt_res1
            elif self.index >= 12 and self.index < 16:
                return txt_res2
            elif self.index >= 7 and self.index < 12:
                return txt_res3
            elif self.index >= 2 and self.index < 7:
                return txt_res4
            elif self.index < 2:
                return txt_rex5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index < 15:
                return txt_res2
            elif self.index >= 6 and self.index < 11:
                return txt_res3
            elif self.index >= 1 and self.index < 6:
                return txt_res4
            elif self.index < 1:
                return txt_res5
