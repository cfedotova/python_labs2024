import os
from red import Red
from yellow import Yellow
from blue import Blue
from circle import Circle
from rectangle import Rectangle
from square import Square


def read_shapes_from_file(filename):
    figures = []
    color_map = {
        "Red": Red(),
        "Yellow": Yellow(),
        "Blue": Blue()
    }

    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 2:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            shape_type = parts[0]
            color_name = parts[-1]

            if color_name not in color_map:
                print(f"Unknown color '{color_name}' in line: {line.strip()}")
                continue

            color = color_map[color_name]

            try:
                if shape_type == "Circle":
                    radius = float(parts[1])
                    figures.append(Circle(radius, color))
                elif shape_type == "Rectangle":
                    width = float(parts[1])
                    height = float(parts[2])
                    figures.append(Rectangle(width, height, color))
                elif shape_type == "Square":
                    side = float(parts[1])
                    figures.append(Square(side, color))
                else:
                    print(f"Unknown shape type '{shape_type}' in line: {line.strip()}")
            except (ValueError, IndexError) as error:
                print(f"Error processing line: {line.strip()}. Error: {error}")

    return figures


if __name__ == '__main__':
    try:
        shapes = read_shapes_from_file('info.txt')
        for shape in shapes:
            print(shape.draw())
    except Exception as e:
        print(f"An error occurred: {e}")
