import math

from calcu import calcu_function
from calcu import sr_function

#Calculation program
calculating = "N"
operator = ""

#Asks if you want to calculate
calculating = input("\nDo you want to calculate? Y/N: ")
operator = input("\nFill in operator: |/|-|+|*|^|sr| : ")

if calculating is "N":
    quit()
elif calculating is not "Y":
    calculating = input("\nWrong input, do you want to calculate? Y/N: ")

#Does the calculating
while calculating == "Y":
    if calculating == "Y" and operator == "sr":
        numbSr = int(input("\nFind square root of number: "))
        sr_function(numbSr, operator,)
        operator = input("\nFill in operator: |/|-|+|*|^|sr| : ")
    elif calculating == "Y" and operator is not "sr":
        numbOne = int(input("\nFirst number: "))
        numbTwo = int(input("\nSecond number: "))
        calcu_function(operator, numbOne, numbTwo)
        operator = input("\nFill in operator: |/|-|+|*|^|sr| : ")

exit()