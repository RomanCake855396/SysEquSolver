import sys
import re

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from sympy import symbols, sympify, Eq, solve



class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set window title and size
        self.setWindowTitle('Solver')
        self.setGeometry(200, 200, 200, 200)

        self.__init__ui()   # Initialize UI elements


    def __init__ui(self):
        # Create input fields for up to 3 equations
        self.equation1 = QLineEdit(self)
        self.equation1.setPlaceholderText('Equation1')

        self.equation2 = QLineEdit(self)
        self.equation2.setPlaceholderText('Equation2')
        
        self.equation3 = QLineEdit(self)
        self.equation3.setPlaceholderText('Equation3')

        # Create "Solve" button and connect it to the solve function
        self.solve_btn = QPushButton(self)
        self.solve_btn.setText('Solve')
        self.solve_btn.clicked.connect(self.solve)

        # Create a label to show the result
        self.result = QLabel(self)
        self.result.setText('x = None')

        # Arrange all widgets in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.equation1)
        layout.addWidget(self.equation2)
        layout.addWidget(self.equation3)
        layout.addWidget(self.solve_btn)
        layout.addWidget(self.result)

        self.setLayout(layout)  # Set the layout for the main window


    def input(self, text):
        """
        Convert a text input like '2x + 3 = 9' into a SymPy equation.
        Handles implicit multiplication like '2x' -> '2*x'.
        """
        try:
            tmp_left, tmp_right = text.split('=')
            # Add multiplication sign between number and variable if missing
            left = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_left))
            right = sympify(re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', tmp_right))
            # Create symbolic equation
            equation = Eq(left, right)
        except:
            return  # Return None on invalid input

        return equation


    def equations(self):
        """
        Retrieve equations from the input fields and convert them using the input() method.
        Returns a list of SymPy equations.
        """
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
        """
        Solve 1 to 3 equations and display the result.
        Supports up to 3 variables (x, y, z).
        Shows error messages if input is invalid or empty.
        """
        try:
            equations = self.equations()
            x, y, z = symbols('x y z')   # Define symbols to be solved
            match len(equations):   # Count number of valid equations
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
                    self.result.setText('ERROR: Empty input!')  # No input provided

        except:
            self.result.setText('ERROR: No found results or invalid syntax!') # Handle any parsing/solving errors



# Start the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
