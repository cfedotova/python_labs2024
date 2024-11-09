def add_vectors(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Vectors must be the same length for addition")
    return [vectorA[i] + vectorB[i] for i in range(len(vectorA))]


def subtract_vectors(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Vectors must be the same length for subtraction")
    return [vectorA[i] - vectorB[i] for i in range(len(vectorA))]


def multiply_vectors_by_scalar(vectorA, scalar):
    return [vectorA[i] * scalar for i in range(len(vectorA))]


def divide_vectors_by_scalar(vectorA, scalar):
    if scalar == 0:
        raise ValueError("Division by zero is not allowed")
    return [vectorA[i] / scalar for i in range(len(vectorA))]


def read_vectors(file_path):
    try:
        with open(file_path, 'r') as reading_file:
            vectors = []
            for line in reading_file:
                vector = list(map(float, line.strip().split()))
                vectors.append(vector)
        if len(vectors) < 2:
            raise ValueError("The file must contain at least two vectors")
        return vectors
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found")
    except ValueError as error:
        raise ValueError(f"Error reading vectors from file: {error}")


def write_to_file(results_file, result):
    results_file.write(result + '\n')


try:
    vector1, vector2 = read_vectors("vectors.txt")

    with open("vector_results.txt", "w") as file:
        try:
            write_to_file(file, f"Sum: {add_vectors(vector1, vector2)}")
        except ValueError as e:
            write_to_file(file, f"Error in addition: {e}")

        try:
            write_to_file(file, f"Difference: {subtract_vectors(vector1, vector2)}")
        except ValueError as e:
            write_to_file(file, f"Error in subtraction: {e}")

        try:
            write_to_file(file, f"Multiply by scalar (2): {multiply_vectors_by_scalar(vector1, 2)}")
        except ValueError as e:
            write_to_file(file, f"Error in multiplication: {e}")

        try:
            write_to_file(file, f"Division by scalar (2): {divide_vectors_by_scalar(vector2, 2)}")
        except ValueError as e:
            write_to_file(file, f"Error in division: {e}")
except FileNotFoundError as e:
    print(f"File error: {e}")
except ValueError as e:
    print(f"Vector error: {e}")
