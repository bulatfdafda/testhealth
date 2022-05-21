from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from final_win import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
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
    def timertest(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer1Event)
        self.timer.start(1000)
    def timertest2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer2Event)
        self.timer.start(1500)
    def timertest3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer3Event)
        self.timer.start(1000)
    def Timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def Timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def Timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
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
        self.txt_timer = QLabel(txt_time)
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
        self.r_line.addWidget(self.txt_timer, alignment= Qt.AlignRight)
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
        self.stest1.clicked.connect(self.timertest)
        self.stest2.clicked.connect(self.timertest2)
        self.stest3.clicked.connect(self.timertest3)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.age2.text(),self.time1.text(), self.time2.text(), self.time3.text())
        self.tw = FinalWin(self.exp)


