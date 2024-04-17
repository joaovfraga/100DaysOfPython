from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    finish_calc = True

    while finish_calc:

        operator_symbol = input("Pick an operator: ")

        num2 = float(input("What's the next number? "))

        calculation_function = operations[operator_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        continue_or_not = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if continue_or_not == "y":
            num1 = answer
        else:
            finish_calc = False
            calculator()


calculator()
