from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from random import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.editor()
        self.conects()

    def set_appear(self):
        self.resize(500, 500)
        self.setWindowTitle('Приложение')
        self.show()

    def initUI(self):
        input_question = QLineEdit('Вопрос')
        self.button = QPushButton('Отправить')
        self.result = QLabel('Результат')
        v_line = QVBoxLayout()
        v_line.addWidget(input_question, alignment=Qt.AlignCenter)
        v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        v_line.addWidget(self.result, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def editor(self):
        ramdomazir = randint(0, 3)
        if ramdomazir == 1:
            self.result.setText('Да')
        if ramdomazir == 2:
            self.result.setText('Нет')
        if ramdomazir == 3:
            self.result.setText('Не знаю')

    def conects(self):
        self.button.clicked.connect(self.editor)


app = QApplication([])
win = MainWin()
app.exec_()
