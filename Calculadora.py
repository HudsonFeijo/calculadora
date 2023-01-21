import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, \
    QPushButton, QLineEdit, QSizePolicy


# Definindo a classe e seu tamanho
class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(300, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

# Definição do display e cores
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('* {background: #FFF; color: #000; font-size: 30px;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

# Criação dos botoes
        self.add_btn(QPushButton('1'), 1, 0, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('2'), 1, 1, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('3'), 1, 2, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style='background: #3838c9; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, 
        lambda: self.display.setText(self.display.text()[:-1]),
        'background: #3838c9; color: #FFF; font-weight: 700;'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style='background: #3838c9; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('AC'), 2, 4, 1, 1, lambda: self.display.setText(''),
        'background: #3838c9; color: #FFF; font-weight: 700;'
        )

        self.add_btn(QPushButton('7'), 3, 0, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('8'), 3, 1, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('9'), 3, 2, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('/'), 3, 3, 1, 1, style='background: #3838c9; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton(''), 3, 4, 1, 1, style='background: #3838c9; color: #FFF; font-weight: 700;')

        self.add_btn(QPushButton('.'), 4, 0, 1, 1, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('0'), 4, 1, 1, 2, style='background: #7c7c80; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, style='background: #3838c9; color: #FFF; font-weight: 700;')
        self.add_btn(QPushButton('='), 4, 4, 1, 1, lambda: self.display.setText(
            str(eval(self.display.text()))),
            'background: #3838c9; color: #FFF; font-weight: 700;'
        )

        self.setCentralWidget(self.cw)

# Função dos botoes
    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not func:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

# Execução da calculadora
if __name__ =='__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
