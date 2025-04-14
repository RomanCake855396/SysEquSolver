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
        self.equation1.setPlaceholderText('Equiption1')

        self.equation2 = QLineEdit(self)
        self.equation2.setPlaceholderText('Equiption2')
        
        self.equation3 = QLineEdit(self)
        self.equation3.setPlaceholderText('Equiption3')

        self.solve_btn = QPushButton(self)
        self.solve_btn.setText('Solve')
        self.solve_btn.clicked.connect(self.solve)

        self.resault = QLabel(self)
        self.resault.setText('x = None')

        layout = QVBoxLayout()
        layout.addWidget(self.equation1)
        layout.addWidget(self.equation2)
        layout.addWidget(self.equation3)
        layout.addWidget(self.solve_btn)
        layout.addWidget(self.resault)

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
            if len(equations) == 1:
                solution = solve(equations[0], x)
                self.resault.setText(f'x = {solution[0]}')
            elif len(equations) == 2:
                solution = solve(equations[0:1], (x, y))
                self.resault.setText(f'x = {solution[x]}; y = {solution[y]}')
            elif len(equations) == 3:
                solution = solve(equations[0:2], (x, y, z))
                self.resault.setText(f'x = {solution[x]}; y = {solution[y]}; z = {solution[z]}')
            elif len(equations) == 0:
                self.resault.setText('ERROR: Empty input!')

        except:
            self.resault.setText('ERROR: Invalid syntax!')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
