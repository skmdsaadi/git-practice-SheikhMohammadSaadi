def add(a, b):
"""Return the sum of a and b."""
return a + b

def subtract(a, b):
"""Return the difference of a and b."""
return a - b

def multiply(a, b):
"""Return the product of a and b."""
return a * b

def divide(a, b):
"""Return the quotient of a and b. Returns error message if dividing by zero."""
if b == 0:
return "Error: Cannot divide by zero"
return a / b

def power(base, exponent):
"""Return base raised to the power of exponent."""
return base ** exponent

def modulo(a, b):
"""Return the remainder of a divided by b."""
if b == 0:
return "Error: Cannot modulo by zero"
return a % b
