'''
Case sensitive - _cars, CARS, cars

'''

# number_of_cards = 23
# kind_of_cars = 'Ferrari'
#
# print(number_of_cards)
# print(kind_of_cars)
#
# print(str(number_of_cards) + " " + kind_of_cars)
#
# # Python String Format - format()
#
# print('{} works at {}.'.format(number_of_cards, kind_of_cars))


'''
Functions
'''

# def addition():
#     a = int(input('Informe um numero: '))
#     b = int(input('Informe um numero: '))
#     print(a + b)
#
#
# addition()

'''
    Args, Kwargs, *args
'''


def user_info(name, age=0, city='São Paulo'):
    print('{} is {} years old, from {}'.format(name, age, city))


user_info('Anne', 37, 'Blumenau')
user_info(34, 'New York')
user_info(
    'Edu')  # def user_info(name, age=0, city='São Paulo'): quando tem valor default
user_info(age=57, name='Eduardo')

'''Keyword arguments
Argumentos não nomeados (*args) vem sempre primeiro que os argumentos nomeados (**kwargs).
'''


def application(fname, lname, email, company, *args, **kwargs):
    print('{} {} works at {}. Her email is {}.'.format(fname, lname, company,
                                                       email))


application('Jesus', 'Salvador', email='ceu@terra.com', company='Heaven')


def função_com_argumentos_variaveis(arg, *args):
    print("Primeiro argumento:", arg)

    for argumento in args:
        print("Argumento de *args", argumento)


função_com_argumentos_variaveis('primeiro_arg', 'arg2', 'arg3', 'arg3')


def adicao(*args):
    resultado = 0

    for argumento in args:
        resultado += argumento

    return resultado


print(adicao(1, 2))
print(adicao(1, 2, 4, 6))
print(adicao(1, 2, 4, 6, 8, 10))
