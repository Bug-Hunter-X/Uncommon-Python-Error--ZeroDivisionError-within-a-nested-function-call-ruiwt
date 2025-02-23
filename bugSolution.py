def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return 1 / a
    except ZeroDivisionError:
        return "Error: Division by zero"
    return a + b