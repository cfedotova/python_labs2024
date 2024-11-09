from vector import Vector
from matrix import Matrix


def vector_calculator():
    try:
        v1 = Vector.load('vectorA.txt')
        v2 = Vector.load('vectorB.txt')

        addition_result = v1 + v2
        subtraction_result = v1 - v2
        multiplication_result = v1 * 2
        division_result = v1 / 2

        with open('vector_results.txt', 'w') as f:
            f.write(f"{v1} + {v2} = {addition_result}\n")
            f.write(f"{v1} - {v2} = {subtraction_result}\n")
            f.write(f"{v1} * 2 = {multiplication_result}\n")
            f.write(f"{v1} / 2 = {division_result}\n")
    except Exception as e:
        print(f"Error: {e}")


vector_calculator()


def matrix_calculator():
    try:
        m1 = Matrix.load('matrixA.txt')
        m2 = Matrix.load('matrixB.txt')

        addition_result = m1 + m2
        subtraction_result = m1 - m2
        multiplication_result = m1 * m2
        division_result = m1 / m2

        with open('matrix_results.txt', 'w') as f:
            f.write(f"Addition\n{addition_result}\n")
            f.write(f"Subtraction\n{subtraction_result}\n")
            f.write(f"Multiplication\n{multiplication_result}\n")
            f.write(f"Division\n{division_result}\n")
    except Exception as e:
        print(f"Error: {e}")


matrix_calculator()
