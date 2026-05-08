def validate_numbers(a, b):
    """Validate that inputs are numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

def add(a, b):
    """Return the sum of a and b."""
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    validate_numbers(a, b)
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except ZeroDivisionError as e:
        return f"Error: {e}"

def power(base, exponent):
    """Return base raised to the power of exponent."""
    validate_numbers(base, exponent)
    return base ** exponent

def modulo(a, b):
    """Return the remainder of a divided by b."""
    validate_numbers(a, b)
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero")
        return a % b
    except ZeroDivisionError as e:
        return f"Error: {e}"
