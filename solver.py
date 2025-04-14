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


    def input(self, text):
        try:
            tmp_left, tmp_right = text
        except ValueError:
            self.resault.setText('ERROR: Invalid syntax')
            return

        try:
            left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
            right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
            equation = Eq(left, right)
        except:
            self.resault.setText('ERROR: Invalid equation')
            return

        return equation


    def solve(self):
        equation = self.input(self.equation.text().split('='))
        x = symbols('x')
        try:
            solution = solve(equation, x)
        except:
            return
        
        self.resault.setText(f'x = {solution[0]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
