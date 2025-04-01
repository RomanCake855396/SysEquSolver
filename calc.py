from sympy import symbols, sympify, Eq, solve

import re

equel = input("Equel: ")
tmp_left, tmp_right = equel.split('=')
left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
x = symbols('x')
equation = Eq(left, right)
solution = solve(equation, x)
print(solution) 
