import sys
import re


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from sympy import symbols, sympify, Eq, solve


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Solver')
        self.setGeometry(200, 200, 200, 200)

        self.__init__ui()


    def __init__ui(self):
        self.equation = QLineEdit(self)
        self.equation.setPlaceholderText('Equiption')

        self.solve_btn = QPushButton(self)
        self.solve_btn.setText('Solve')
        self.solve_btn.clicked.connect(self.solve)

        self.resault = QLabel(self)
        self.resault.setText('x = None')

        layout = QVBoxLayout()
        layout.addWidget(self.equation)
        layout.addWidget(self.solve_btn)
        layout.addWidget(self.resault)

        self.setLayout(layout)


    def solve(self):
        try:
            tmp_left, tmp_right = self.equation.text().split('=')
        except ValueError:
            self.resault.setText('ERROR: Invalid syntax')
            return

        try:
            left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
            right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
            equ = Eq(left, right)
            x = symbols('x')
            solution = solve(equ, x)
            self.resault.setText(f'x = {solution[0]}')
        except:
            self.resault.setText('ERROR: Invalid equation')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
