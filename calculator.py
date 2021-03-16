def calculator(number1, number2, operator):
    """
    A program that simulates like a calculator.
    The operators allowed are +, -, *, /, //, and **, as addition,
    subtraction, multiplication, division, integer division, and
    power, respectively
    """
    #This will only perform the operation that the input gives.
    if operator == '+':
       return (number1 + number2)
    elif operator == '-':
       return (number1 - number2)
    elif operator == '*':
       return (number1 * number2)
    elif operator == '/':
       if number2 == 0:
          return False
       else:
          return (number1 / number2)
    elif operator == '//':
       if number2 == 0:
          return False
       else:
          return (number1 // number2)
    elif operator == '**':
       return (number1 ** number2)
    else:
       return False

def input_output():
    """
    Takes input from the user and calls the calculator function.
    """
    number1 = input("Enter the first number: ")
    return (int(number1))
    number2 = input("Enter the second number: ")
    operator = input("Enter the operation: ")
    calculator(number1, number2, operator)
    continue_q = input("Do you wish to exit? ")
    return (continue_q)
    #If user wants to continue program, input_output function is called again.
    if continue_q == 'n':
       input_output()
    else:
       quit()

