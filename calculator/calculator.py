
import math
def multiplication(num1,num2):
    """
    :param num1: The first number
    :param num2: The second number
    :return: The product of the two numbers
    """
    return num1*num2

def division(num1,num2):
    """

    :param num1: The first number
    :param num2: The second number
    :return: The quotient when the first number is divided by the second number
    """
    return num1/num2

def addition(num1, num2):
    """

    :param num1: The first number
    :param num2: The second number
    :return: The sum of the numbers
    """
    return num1+num2

def subtraction(num1, num2):
    """

    :param num1: The first number
    :param num2: The second number
    :return: The difference between these numbers
    """
    return num1-num2





if __name__ == "__main__":
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    operation = raw_input("What operation do you want to perform?")
    if operation == "/":
        result = division(num1,num2)  #assigning the returned value to result
    elif operation == "*":
        result = multiplication(num1,num2) #assigning the returned value to result
    elif operation == "+":
        result = addition(num1,num2)  #assigning the returned value to result
    elif operation == "-":
        result = subtraction(num1,num2)  #assigning the returned value to result

    print "The result is "+ str(result)