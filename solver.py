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
        self.equation1 = QLineEdit(self)
        self.equation1.setPlaceholderText('Equation1')

        self.equation2 = QLineEdit(self)
        self.equation2.setPlaceholderText('Equation2')
        
        self.equation3 = QLineEdit(self)
        self.equation3.setPlaceholderText('Equation3')

        self.solve_btn = QPushButton(self)
        self.solve_btn.setText('Solve')
        self.solve_btn.clicked.connect(self.solve)

        self.result = QLabel(self)
        self.result.setText('x = None')

        layout = QVBoxLayout()
        layout.addWidget(self.equation1)
        layout.addWidget(self.equation2)
        layout.addWidget(self.equation3)
        layout.addWidget(self.solve_btn)
        layout.addWidget(self.result)

        self.setLayout(layout)


    def input(self, text):
        try:
            tmp_left, tmp_right = text.split('=')
            left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
            right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
            equation = Eq(left, right)
        except:
            return

        return equation


    def equations(self):
        equations = []
        text1 = self.equation1.text()
        if len(text1):
            equation1 = self.input(text1)
            equations.append(equation1)
        text2 = self.equation2.text()
        if len(text2):
            equation2 = self.input(text2)
            equations.append(equation2)
        text3 = self.equation3.text()
        if len(text3):
            equation3 = self.input(text3)
            equations.append(equation3)
        return equations


    def solve(self):
        try:
            equations = self.equations()
            x, y, z = symbols('x y z')
            match len(equations):
                case 1:
                    solution = solve(equations[0], x)
                    self.result.setText(f'x = {solution[0]}')
                case 2:
                    solution = solve(equations[0:1], (x, y))
                    self.result.setText(f'x = {solution[x]}; y = {solution[y]}')
                case 3:
                    solution = solve(equations[0:2], (x, y, z))
                    self.result.setText(f'x = {solution[x]}; y = {solution[y]}; z = {solution[z]}')
                case _:
                    self.result.setText('ERROR: Empty input!')

        except:
            self.result.setText('ERROR: Invalid syntax!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
