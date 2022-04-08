
# task 1 in homework
import functools
def decorator1(f):
    @functools.wraps(f)
    def wrapper(*args):
        a = 100 % f(*args)
        if a == 0:
            return 'We are OK!'
        else:
            d = (f'Bad news guys, we got' , {a} )
            return d
    return wrapper

@decorator1
def func1(z, y):
    b = z * y
    return b
print(func1(3, 7))



#Task 2 in homework
def deco(f):
    @functools.wraps(f)
    def wrapper(*args):
        try:
           d = int(f(*args))
           print(d)
        except ValueError:
           raise ValueError ('string type is not supported')
    return wrapper

@deco
def func1(a):
    z = a+a
    return z
print(func1(5))
print(func1('ffuagf'))

