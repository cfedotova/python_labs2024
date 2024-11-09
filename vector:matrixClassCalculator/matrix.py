class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix must be the same length")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def __sub__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix must be the same length")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("The number of columns of the first matrix must be equal to the number of rows of the second matrix")
        result = [[0 for _ in range(len(other.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def __truediv__(self, other):
        inverse = self.inverse(other)
        return self * inverse

    def inverse(self, other):
        if len(other.data) != 2 or len(other.data[0]) != 2:
            raise ValueError("Calculating the inverse matrix is supported only for 2x2 matrices")
        a, b, c, d = other.data[0][0], other.data[0][1], other.data[1][0], other.data[1][1]
        det = a * d - b * c
        if det == 0:
            raise ValueError("Matrix cannot be inversed")
        return Matrix([[d / det, -b / det], [-c / det, a / det]])

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r') as f:
                data = [list(map(float, line.strip().split())) for line in f.readlines()]
            return cls(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found")
        except ValueError:
            raise ValueError(f"Error in file '{filename}'")

    def save(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')
