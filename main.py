import math
from unittest import skip

from calcu import calcu_function
from calcu import sr_function

#Calculation program
calculating = "N"
operator = ""

#Asks if you want to calculate
calculating = input("\nDo you want to calculate? Y/N: ")

if calculating == "N":
    quit()
elif calculating == "Y":
    operator = input("\nFill in operator: |/|-|+|*|^|sr| : ")
elif calculating != "Y":
    calculating = input("\nWrong input, do you want to calculate? Y/N: ")

#Does the calculating
while calculating == "Y":
    if calculating == "Y" and operator == "sr":
        numbSr = int(input("\nFind square root of number: "))
        sr_function(numbSr, operator,)
        operator = input("\nFill in operator: |/|-|+|*|^|sr| : ")
    elif calculating == "Y" and operator != "sr":
        numbOne = int(input("\nFirst number: "))
        numbTwo = int(input("\nSecond number: "))
        calcu_function(operator, numbOne, numbTwo)
    elif calculating == "N":
        quit()

exit()