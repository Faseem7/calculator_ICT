class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    def quadratic_equation(self, a, b, c):
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            return (-b) / (2 * a)
        else:
            root1 = (-b + (discriminant ** 0.5)) / (2 * a)
            root2 = (-b - (discriminant ** 0.5)) / (2 * a)
            return root1, root2