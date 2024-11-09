input_file = "input.txt"
try:
    with open(input_file, "r") as file:
        data = file.readlines()
        data_list = [line.strip() for line in data]
        a = float(data_list[0])
        b = float(data_list[1])

except FileNotFoundError:
    print("Error: Input file not found.")
    a = b = 0
except ValueError:
    print("Error: Input file contains invalid data.")
    a = b = 0

steps_file = "steps.txt"
try:
    with open(steps_file, "r") as file:
        number = int(file.readline())

except FileNotFoundError:
    print("Error: Steps file not found.")
    number = 0
except ValueError:
    print("Error: Steps file contains invalid data.")
    number = 0

limit_file = "limit.txt"
try:
    with open(limit_file, "r") as file:
        lim = int(file.readline())

except FileNotFoundError:
    print("Error: Limit file not found.")
    lim = 0
except ValueError:
    print("Error: Limit file contains invalid data.")
    lim = 0


def fibonacci_by_steps(input_values, steps):
    if len(input_values) >= steps:
        return input_values
    next_value = input_values[-1] + input_values[-2]
    input_values.append(next_value)
    return fibonacci_by_steps(input_values, steps)


def fibonacci_by_limit(fibonacci_result, limit):
    temp_fibonacci = (fibonacci_result[-1] + fibonacci_result[- 2])
    if temp_fibonacci > limit:
        return fibonacci_result
    temp_fibonacci = fibonacci_result + [temp_fibonacci]
    return fibonacci_by_limit(temp_fibonacci, limit)


def result_by_steps():
    try:
        impute_values = [a, b]
        result_file = "result_by_steps.txt"
        with open(result_file, "w") as result_file:
            fibonacci_result = fibonacci_by_steps(impute_values, number)
            for num in fibonacci_result:
                result_file.write(f"{num}\n")
    except FileNotFoundError:
        print("Error: Result by steps file not found.")


def result_by_limit():
    try:
        impute_values = [a, b]
        result_file = "result_by_limit.txt"
        with open(result_file, "w") as result_file:
            fibonacci_result = fibonacci_by_limit(impute_values, lim)
            for num in fibonacci_result:
                result_file.write(f"{num}\n")
    except FileNotFoundError:
        print("Error: Result by limit file not found.")


result_by_steps()
result_by_limit()
