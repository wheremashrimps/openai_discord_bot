def bot_math(x: int, operator: str, y: int) -> int:
    if operator == '+':
        # Add the numbers
        result = x + y
    # If the operator is subtraction
    elif operator == '-':
        # Subtract the numbers
        result = x - y
    # If the operator is multiplication
    elif operator == '*':
        # Multiply the numbers
        result = x * y
    # If the operator is division
    elif operator == '/':
        # Divide the numbers
        result = x / y
    # If the operator is exponentiation
    elif operator == '^':
        # Exponentiate the numbers
        result = x ** y
    # If the operator is modulus
    elif operator == '%':
        # Modulus the numbers
        result = x % y
    # If the operator is floor division
    elif operator == '//':
        # Floor divide the numbers
        result = x // y
    # If the operator is not one of the above
    else:
        # Raise an error
        raise ValueError('Invalid operator')
    # Return the result
    return result

