
#Description: Takes the length of an input (greater than 2 less than 10) and allows the user to enter that many integers (which are greater than 0), it creates a list and from there it sees if any values from the list add to the target number.

print('*************************Section A*************************')
length = int(input("Enter the length: "))
while length <= 2 or length >= 10:
    print("Invalid list length, try again.")
    length = int(input("Enter the length: "))
    print()

print("This list contains", length, "entries.")
print()
print('*************************Section B*************************')
lst = list()
i = 0
x = 0
while i <= (length - 1):
  
  variable = int(input("Enter the entry at index {0}: ".format(x)))
  if variable <= 0:
      print("Invalid entry at index", x)
      print("")

  else:
      x += 1
      lst.append(variable)
      i += 1
print()
print('*************************Section C*************************')
target = int(input("Enter the target value: "))
flag = 0
for e, number in enumerate(lst[:]):
    complementary = target - number
    if complementary in lst[1+e:]:
        flag = 1
        print("The entries {}, {} found at index {}, {} sum to {}.".format(number, complementary, lst.index(number), lst.index(complementary), target)) 
        break
if flag == 0:
    print("No valid combination summing to {} was found".format(target))

           

    