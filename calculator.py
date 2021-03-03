def calculator(number1, number2, operator):
    if operator == '+':
       print(number1 + number 2)
    elif operator == '-':
       print(number1 - number 2)
    elif operator == '*':
       print(number1 * number 2)
    elif operator == '/':
       print(number1 / number 2)
    elif operator == '//':
       print(number1 // number 2)
    elif operator == '**':
       print(number1 ** number 2)
    else:
       quit()

def input_output():
    number1 = input("Enter the first number: ")
    print(int(number1))
    number2 = input("Enter the second number: ")
    print(int(number2))
    operator = input("Enter the operation: ")
    print(operator)
    calculator(number1, number2, operator)
    continue_q = input("Do you wish to exit? ")
    print(continue_q)
    if continue_q == 'n':
       input_output()
    else:
       quit()

