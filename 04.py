# File: L4q4.py
# Author: Colin Troy
# Date: 02/23/2022
# Section: 496
# Email: troyc1920@tamu.edu
#Description: Takes a string variable, it computes the length of the string, if the length is even it prints out the even indexes, if it is odd it prints out the odd indexes (each with their coresponding index locations)
print('**************************************************')
a = str(input("Enter a string variable: "))
print('Length of the string', a, 'is', len(a))
print('')
i = list()
d = 0
if len(a) % 2 == 0:
    b = (a[0:len(a):2])
    print("    ".join(b))
    for x in b:
        i.append(d)
        d += 2
    print("    ".join(str(x) for x in i))
y = list()
e = 1
if len(a) % 2 != 0:
    c = (a[1:(len(a)+1):2])
    print("    ".join(c))
    for x in c:
        y.append(e)
        e +=2
    print("    ".join(str(x) for x in y))
print('**************************************************')

