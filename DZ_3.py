# task 1 in homework
import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"



def change_into_vowels(random_str):

    for letter in random_str:
        if letter.lower() in consonants:
            random_str = random_str.replace(letter, random.choice(vowels))
    return random_str
print(change_into_vowels('fdsafdsafdsafjytjfadbshjyteektyejae'))

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
###########################################
#3 in homevork

from collections import Counter

def most_frequent(x) :
    if not x:
        return []
    else:
        most_common = Counter(x).most_common()
        max_count = most_common[0][1]
        result = []
        for x, count in most_common:
            if count < max_count:
                break
            else:
                result.append(x)
        return result
print(most_frequent([3, 15, 22, 3, 41, 11, 15, 1, 1, 1]))
print(most_frequent([3, 15, 22, 24, 41, 11, 15, 24, 24, 24]))
print(most_frequent(['b', 'b', 'b', 'c', 'a']))