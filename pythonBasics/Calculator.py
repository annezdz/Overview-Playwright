on = True


def add():
    a = float(input('Number 1:'))
    b = float(input('Number 2:'))
    print(a + b)


def substraction():
    a = float(input('Number 1:'))
    b = float(input('Number 2:'))
    print(a - b)


def multiply():
    a = float(input('Number 1:'))
    b = float(input('Number 2:'))
    print(a * b)


def divide():
    a = float(input('Number 1:'))
    b = float(input('Number 2:'))
    print(a // b)


while on:
    operation = input('Please choose +, -, * or / - or 0 to exit ')
    if operation == '+':
        add()
    elif operation == '-':
        substraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == '0':
        on = False
    else:
        print('This operations is not available')

print('*********************************************************************')

# fruits = ['apple', 'orange', 'pears', 'cherries', 'grapes']
#
# for fruit in fruits:
#     print('Would you like {} ?'.format(fruit))
#
# for number in range(1, 11):
#     print('{} '.format(number))

print('*********************************************************************')

# temp_f = 40
#
# while temp_f > 32:
#     print('The water is {} degrees.'.format(temp_f))
#     temp_f -= 1
#     if temp_f == 3:
#         break
#
# for number in range(1, 11):
#     if number == 7:
#         print('Were skipping number 7.')
#         continue
#     print('This is the number {}.'.format(number))
