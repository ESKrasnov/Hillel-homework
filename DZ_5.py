

class ProcessInput:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
                return self.a - self.b

    def multiple(self):
                return self.a * self.b

    def divide(self):
        try:
            return self.a // self.b
        except ZeroDivisionError:
            print(f'ZeroDivisionError')



proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add())         # выведет 30
print(proccess_input.subtract())    # выведет 10
print(proccess_input.multiple())    # выведет 200
print(proccess_input.divide())      # выведет 2
