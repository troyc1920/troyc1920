# File: L9q1.py
# Author: Colin Troy
# Date: 4/14/2022
# Section: 496
# E-mail: troyc1290@tamu.edu
# Description: The program finds the result of an exponential function using recursion
base = int(input('Enter a number: '))
exponent = int(input('Enter an integer between -100 and 100: '))

def recursive(exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * recursive(exponent-1)
    elif exponent < 0:
        return (1/base) * recursive(exponent+1)

print(base, 'raised to the power of', exponent, 'is', recursive(exponent))