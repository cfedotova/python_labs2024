def add_matrices(matrixA, matrixB):
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    return [[matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]


def subtract_matrices(matrixA, matrixB):
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction")
    return [[matrixA[i][j] - matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]


def matrix_multiply(matrixA, matrixB):
    if len(matrixA[0]) != len(matrixB):
        raise ValueError("Matrices must have compatible dimensions for multiplication")
    result = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            result[i][j] = sum(matrixA[i][k] * matrixB[k][j] for k in range(len(matrixB)))
    return result


def matrix_determinant(matrixA):
    if len(matrixA) != 3 or len(matrixA[0]) != 3:
        raise ValueError("Matrix must be 3x3")

    a, b, c = matrixA[0]
    d, e, f = matrixA[1]
    g, h, i = matrixA[2]

    determinant = (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g))
    return determinant


def inverse_matrix(matrix):
    determinant = matrix_determinant(matrix)
    if determinant == 0:
        raise ValueError("Matrix cannot be inverted because its determinant is zero")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    inverse = [
        [(e * i - f * h) / determinant, -(b * i - c * h) / determinant, (b * f - c * e) / determinant],
        [-(d * i - f * g) / determinant, (a * i - c * g) / determinant, -(a * f - c * d) / determinant],
        [(d * h - e * g) / determinant, -(a * h - b * g) / determinant, (a * e - b * d) / determinant]
    ]
    return inverse


def divide_matrices(matrixA, matrixB):
    try:
        inverse_matrixB = inverse_matrix(matrixB)
    except ValueError as e:
        raise ValueError(f"Matrix inversion error: {e}")

    return matrix_multiply(matrixA, inverse_matrixB)


def read_matrix(file_path):
    try:
        with open(file_path, 'r') as reading_file:
            matrix = [list(map(int, line.split())) for line in reading_file]
        return matrix
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except ValueError:
        raise ValueError(f"Error processing file {file_path}. Ensure it contains valid integers.")


def write_to_file(results_file, label, matrix):
    with open(results_file, 'a') as file:
        file.write(label + '\n')
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n')


try:
    A = read_matrix('matrixA.txt')
    B = read_matrix('matrixB.txt')

    with open('matrix_results.txt', 'w') as file:
        try:
            result = add_matrices(A, B)
            write_to_file('matrix_results.txt', "Sum:", result)
        except ValueError as error:
            write_to_file('matrix_results.txt', f"Error in addition: {error}", [])

        try:
            result = subtract_matrices(A, B)
            write_to_file('matrix_results.txt', "Subtract:", result)
        except ValueError as error:
            write_to_file('matrix_results.txt', f"Error in subtraction: {error}", [])

        try:
            result = matrix_multiply(A, B)
            write_to_file('matrix_results.txt', "Multiply:", result)
        except ValueError as error:
            write_to_file('matrix_results.txt', f"Error in multiplication: {error}", [])

        try:
            result = divide_matrices(A, B)
            write_to_file('matrix_results.txt', "Division:", result)
        except ValueError as error:
            write_to_file('matrix_results.txt', f"Error in division: {error}", [])
except FileNotFoundError as error:
    print(f"File error: {error}")
except ValueError as error:
    print(f"Matrix error: {error}")
