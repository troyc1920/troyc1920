# File: L6q1.py
# Author: Colin Troy
# Date: 03/21/2022
# Section: 496
# Email: troyc1920@tamu.edu
# Description: Creates a menu which you can add, delete, and search the fruits in stock in a grocery store

def menu():
    print('********************Main Menu********************')
    print('1. Add fruits')
    print('2. Edit fruits')
    print('3. Delete fruits')
    print('4. Search fruits')
    print('5. Quit' )
    print('************************************************** \n')

def choose():
    global user_choice
    user_choice = (input('Choose from the menu: '))

fruit_inventory = {}
def add_fruit():
    global fruit_inventory
    global fruti
    global fruit_prices
    fruti = (input('Enter fruit followed by prices: '))
    fruti = fruti.split(',')
    fruit_prices = fruti[1].split()
    
    fruit_inventory[fruti[0]] = fruit_prices
    for i in range(0, len(fruit_prices)):
        fruit_prices[i] = float(fruit_prices[i])
    print('Current Stock:', fruit_inventory)
    print()

def edit_fruit():

    edit_choice = str(input("Enter fruit name: "))
    for key in fruit_inventory:
        if edit_choice == key:
            fruit_prices = input('Enter the fruit prices: ')
            fruit_prices = fruit_prices.split()
            for i in range(0, len(fruit_prices)):
                fruit_prices[i] = float(fruit_prices[i])
            fruit_inventory[edit_choice] = fruit_prices
            break

    print()
    print('Current Stock:', fruit_inventory)
    print()

def delete_fruit():
    delete_choice = str(input('If you want to remove all items enter all otherwise enter the fruit name: '))
    flag = 1
    for key in fruit_inventory:
        if delete_choice == key:
            del fruit_inventory[key]
            flag = 0
            break
            
        elif delete_choice == 'all':
            fruit_inventory.clear()
            flag = 0
            break
    if flag == 1:
        print(delete_choice, 'is not on the list.')
    print()   
    print('Current Stock:', fruit_inventory)
    print()

def search_fruit():
    search = str(input('Enter the fruit name: '))
    flag = 1
    for key in fruit_inventory:
        if search == key:
            print(search, 'have', len(fruit_prices), 'different prices of: ', fruit_inventory[search])
            flag = 0
            break
    if flag == 1:
        print(search, 'is not on the list')


flag = 0
while flag == 0:
    menu()
    choose()
    if user_choice == '1':
        add_fruit()
    elif user_choice == '2':
        edit_fruit()
    elif user_choice == '3':
        delete_fruit()
    elif user_choice == '4':
        search_fruit()
    elif user_choice == '5':
        print()
        print('Current Stock:', fruit_inventory)
        flag = 1