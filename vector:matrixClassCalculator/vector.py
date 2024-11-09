class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.coordinates])

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot be divided by 0")
        return Vector([a / scalar for a in self.coordinates])

    def __repr__(self):
        return f"({', '.join(map(str, self.coordinates))})"

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r') as f:
                coordinates = list(map(float, f.readline().strip().split()))
            return cls(coordinates)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}'not found")
        except ValueError:
            raise ValueError(f"Error in file '{filename}'.")

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(' '.join(map(str, self.coordinates)) + '\n')
