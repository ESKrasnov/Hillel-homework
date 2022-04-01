# task 1 in homework
import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

str = 'qwertyuiopp'

#for i in len(str):

#r = str.split().replace(consonants.split(), random.choice(vowels), len(str))
#print(r)







b = random.choice(vowels)
print(b)
#############
# task 2 in homework
data = [

  {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },

  {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},

  {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},

  {'name': 'Andrey', 'city': 'Kiev', 'age': 34},

  {'name': 'Artem', 'city': 'Dnepr', 'age': 50},

  {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

newlist = sorted(data, key=lambda  k: k['age'])
print(newlist)

from collections import Counter
from itertools import groupby
from operator import itemgetter

#esults = {k
#           : Counter(i for i in v)
#          for k, v in groupby(sorted(((k, v)
#                                       for i in data
#                                       for k, v in i.items()),
#                                      key=itemgetter(0)),
#                              key=itemgetter(0))}
#print(results)

# ключевая функция сортировки
keyfunc = lambda x:x['city']

# сортируем список заданий по названию 'x[0]'
city = sorted(data, key=keyfunc)

# при группировке по заданиям применяем
# ту же ключевую функцию сортировки
for city, action in groupby(city , key=keyfunc):
    print(city)
    print('-' * len(city))
sorted_data = sorted(data, key=lambda x:x['city'])
 # вывод
        for _, 'name', 'age' in sorted_data:
         print(f'  {} -> {}')