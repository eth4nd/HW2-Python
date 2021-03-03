def calculator(number1, number2, operator):
    if operator == '+':
       return (number1 + number 2)
    elif operator == '-':
       return (number1 - number 2)
    elif operator == '*':
       return (number1 * number 2)
    elif operator == '/':
       return (number1 / number 2)
    elif operator == '//':
       return (number1 // number 2)
    elif operator == '**':
       return (number1 ** number 2)
    else:
       quit()

def input_output():
    number1 = input("Enter the first number: ")
    return (int(number1))
    number2 = input("Enter the second number: ")
    return (int(number2))
    operator = input("Enter the operation: ")
    return (operator)
    calculator(number1, number2, operator)
    continue_q = input("Do you wish to exit? ")
    return (continue_q)
    if continue_q == 'n':
       input_output()
    else:
       quit()

