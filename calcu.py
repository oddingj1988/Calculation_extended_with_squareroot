import math

def calcu_function(operator, numbOne, numbTwo):
    if operator == "*":
        answ = numbOne * numbTwo
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
        if calculating == "N":
            exit()
    elif operator == "/":
        answ = numbOne / numbTwo
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
        if calculating == "N":
            exit()
    elif operator == "+":
        answ = numbOne + numbTwo
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
        if calculating == "N":
            exit()
    elif operator == "-":
        answ = numbOne - numbTwo
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
        if calculating == "N":
            exit()
    elif operator == "^":
        answ = numbOne ** numbTwo
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
        if calculating == "N":
            exit()
    else:
        print("Wrong input\n")
        calculating = input("Do you want to calculate? Y/N: ")
        if calculating == "N":
            exit()


def sr_function(numbSr, operator):
    calculating = "Y"
    
    if (calculating == "Y") is True:
        answ = math.sqrt(numbSr)
        print("\nThe answer is: \n")
        print(answ)
        calculating = input("\nDo you want to calculate? Y/N: ")
