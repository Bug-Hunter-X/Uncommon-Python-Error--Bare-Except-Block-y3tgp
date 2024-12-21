def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Unsupported operation: {e}"    except Exception as e:
        return f"An unexpected error occurred: {e}"