def is_numeric(text):
    return text.isnumeric()


def is_supported(text):
    return text in ['+', '-', '*', '/']


def calculate(operand1, poperator, operand2):
    rv = 0
    if poperator == '+':
        rv = operand1 + operand2
    elif poperator == '-':
        rv = operand1 - operand2
    elif poperator == '*':
        rv = operand1 * operand2
    elif poperator == '/':
        rv = operand1 / operand2
    return rv
