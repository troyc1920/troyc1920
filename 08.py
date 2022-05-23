#File: L9q2.py
# Author: Colin Troy
# Date: 4/14/2022
# Section: 496
# E-mail: troyc1290@tamu.edu
# Description: solves Ackermann's function using recursion
def ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

m = int(input('Enter an integer value for m: '))
n = int(input('Enter an integer value for n: '))
print('Ackerman({0},{1}) = {2}'.format(m, n, ackermann(m, n)))