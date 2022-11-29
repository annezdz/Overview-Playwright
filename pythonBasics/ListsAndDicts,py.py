# '''
#
# Lists
#
#
# '''
#
# fruits = ['peaches', 'pears', 'apples']
# years = [3, '1998', 2.5, 987, '1994']
#
# print(fruits, years)
# fruits.append('oranges')
# print(fruits)
#
#
# fruits.extend(years)
# print(fruits)
#
# # fruits.remove('oranges')
# # print(fruits)
# #
# #
# # fruits.pop(0)
# # print(fruits)
# #
# # fruits.pop(-1)
# # print(fruits)
# # fruits.sort()  #TypeError: '<' not supported between instances of 'int' and 'str'
# print(fruits)
#
# numbers = [1, 99, 85, 7]
# numbers.sort()
# print(numbers)
#
# print('apples' in fruits)
# print('apple' in fruits)

stuff = {'food': 15, 'energy': 100, 'enemies': 3}

# print(stuff.get('food')) #pegar o valor
#
# print(stuff.items()) #imprimir chave / valor
# print(stuff.keys()) #imprimir os valores

# print(stuff.popitem()) #vai excluir a ultima chave e valor - 'enemies': 3
# print(stuff)

# print(stuff.setdefault('food'))
# print(stuff.setdefault('friends', 123)) #vai incluir no final da sequencia
# print(stuff)

new_items = {'rock': 4, 'arrows': 18}
stuff.update(new_items)
print(stuff)

new_items = {'rock': 2, 'arrows': 5}
stuff.update(new_items)
print(stuff)

up_news = {'food': 3, 'webs': 2}
stuff.update(up_news)
print(stuff)

stuff.update(food=450, cookies=6)
print(stuff)

