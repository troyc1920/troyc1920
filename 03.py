#Description: Takes single digit numbers (first and last cant be 0) and creates a list, it priints the normal list, backwards list, and the numbers from the two lists added together.

print('**************************************************')
lst = []
is_valid = False
is_printed = False
while not is_valid:
    
    lst = input("Enter single digits seperated by one space: ")
    lst = lst.split(' ')
    for i in range(0,len(lst)):
        lst[i]= int(lst[i])
        print(type(i))
    is_valid = True
    for i in lst:
        if i >= 10:
            is_valid = False
            print('Invalid list, try again')
            is_printed = True
            break
    if lst[0] == 0 or lst[-1] == 0:
        is_valid = False
        if not is_printed:
            print('Invalid list, try again')


lst_number = [str(integer) for integer in lst]
lst_number = "".join(lst_number)
lst_number = int(lst_number)
lst_number_one = lst_number



print("The initial list is:", lst)

number1_reversed = 0
while lst_number != 0:
    remainder = lst_number % 10
    number1_reversed = (number1_reversed*10) + remainder
    lst_number = lst_number //10


number_reversed = str(number1_reversed)
number_reversed = map(int, number_reversed)
number_reversed = list(number_reversed)
print('The reversed list is:',number_reversed)

addition_number = lst_number_one + number1_reversed
addition_number = str(addition_number)
addition_number = map(int, addition_number)
addition_number = list(addition_number)
print('The addition list is:', addition_number)
print('**************************************************')

