import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random
import numexpr as ne


def generate():
    operators = ['+', '-', '*', '/']
    s = ''
    s += str(random.randint(1, 9))
    s += ' '
    for i in range(random.randint(1, 4)):
        s += operators[random.randint(0, 3)]
        s += ' '
        s += str(random.randint(1, 9))
        s += ' '
    return s


m = generate()
m1 = ne.evaluate(m)

class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(20, 350)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(30)
        self.line.setFont(font)
        self.line.resize(590, 70)

        self.line1 = QLineEdit(self)
        self.line1.move(20, 20)
        self.line1.setReadOnly(True)
        self.line1.setAlignment(Qt.AlignRight)
        font = self.line1.font()
        font.setPointSize(30)
        self.line1.setFont(font)
        self.line1.resize(590, 70)
        self.line1.setText(m)

        self.line2 = QLineEdit(self)
        self.line2.move(20, 130)
        self.line2.setAlignment(Qt.AlignRight)
        font = self.line1.font()
        font.setPointSize(30)
        self.line2.setFont(font)
        self.line2.resize(590, 70)
        self.line2.setText('')

        check = QPushButton("check", self)
        check.move(20, 240)
        check.resize(590, 70)
        check.clicked.connect(self.check)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Calculator")
        self.setFixedSize(630, 350 + 20 + 70)
        self.show()

    def check(self):

        answer = self.line2.text()

        if (float(answer) > m1 - 0.01) and (float(answer) < m1 + 0.01):
            self.line.setText('True')
        else:
            self.line.setText('False')


def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
