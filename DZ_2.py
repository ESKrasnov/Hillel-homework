#list()
a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]



d = sorted(a)
print(d[-3], d[-2], d[-1]) # 1.2 in homework



print(a.index(min(a))) # 1.3 in homework

b = list(reversed([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))
print(b)  # 1.4 in homework


for i in reversed(range(len(a))):
    if a[i] in a[:i]:
        del a[i]
print(a) # 1.1 in homework
print(list(set(a))) # 1.1 in homework если нужно отобразить масив без повторений и удалений


c = list(range (0 , 100 ))
f = [x for x in c if not x % 2]
print(f)  # 2 in homework

#3 in homework
dict_one = { 'a': 1, 'b': 2, 'c': 3,  'd': 4 }
dict_two = { 'a': 6,  'b': 7, 'z': 20, 'x': 40 }

for key in dict_one.keys():
    if key in dict_two.keys():
        print(key)



keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict = { t: t*t for t in keys }
print(dict) # 4 in homework