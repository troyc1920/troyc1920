# File: L5q2.py
# Author: Colin Troy
# Date: 02/28/2022
# Section: 496
# Email: troyc1920@tamu.edu
#Description:returns the factorial and possible combinations of a number

def my_input():
    global n
    global k
    global flag
    flag = 0
    i = 0
    while i < 1:
        n = int(input("n: "))
        k = int(input("k: "))
        i = i + 1
    if k <= 0 or n <= 0 or k > n:
        print()
        print('Invalid input')
    else:
        flag = 1
        return
    
        
def my_factorial():
    global factorial_n
    global factorial_k
    global factorial_difference
    factorial_n = 1
    for i in range(1, n+1):
        factorial_n *= i
    factorial_k = 1
    for x in range(1, k+1):
        factorial_k *= x
    factorial_difference = 1
    for y in range(1, (n-k)+1):
        factorial_difference *= y

def my_combination():
    global combination
    combination = int(factorial_n/ (factorial_k * factorial_difference))
    return combination

my_input()
if flag == 1:
    my_factorial()
    my_combination()
    print('Test passed')
    print('You can choose', k, 'objects from', n, 'objects in', combination, 'ways')