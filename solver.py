import sys
import re


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from sympy import symbols, sympify, Eq, solve


app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100, 100, 100, 100)
layout = QVBoxLayout()


def solv():
    tmp_left, tmp_right = equiption.text().split('=')
    left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
    right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
    x = symbols('x')
    equ = Eq(left, right)
    solution = solve(equ, x)
    resault.setText(f'x = {solution[0]}') 



equiption = QLineEdit(window)
equiption.setPlaceholderText('Equiption')

solve_btn = QPushButton(window)
solve_btn.setText('Solve')
solve_btn.clicked.connect(solv)

resault = QLabel(window)
resault.setText('x = None')

layout.addWidget(equiption)
layout.addWidget(solve_btn)
layout.addWidget(resault)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
