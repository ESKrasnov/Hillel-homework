# task 1 in homework
import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

str = 'qwertyuiopp'

for i in str:

    i = str.replace(tconsonants, random.choice(vowels))
    print(i)

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
# 2.2 in homework
from itertools import groupby
def key_func(k):
    return k['city']



data = sorted(data, key=key_func)

for key, value in groupby(data, key_func):
    print(key , ':')
    print(list(value))

