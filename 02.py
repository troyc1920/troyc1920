#Description: Takes a starting fibonacci number and an ending number, from there it shows how many fibonnaci numbers are between the starting number and ending number, printing the list out.

print('**************************************************')
startNum = int(input('Enter starting number: '))
endNum = int(input('Enter ending number: '))
print('')
n1 = 0
n2 = 1
while (n1 + n2) < startNum:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if (n1 + n2) > startNum:
        print('Invalid Starting number try again')
        startNum = int(input('Enter starting number: '))


fibonacci = list()
while n2 < endNum:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    fibonacci.append(n2)
    if n2 > endNum:
        del fibonacci[-1]
print("The", len(fibonacci), "Fibonacci numbers between", startNum, "and", endNum, "are:")
print(" ".join(str(x) for x in fibonacci))
print('**************************************************')  
