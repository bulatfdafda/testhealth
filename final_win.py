from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
class FinalWin(QWidget):
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
        self.h_line = QHBoxLayOut()
        self.heart = QLabel(txt_workheart)
        self.python = QLabel(txt_index)
        self.l_line.addWidget(self.python, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.heart, alignment= Qt.AlignCenter)
    