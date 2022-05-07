




class Vehicle:
    def __init__(self, type, color, doors):
        self._type = type
        self.color = color
        self.doors = doors

    @property
    def type(self):
        print(f'type of Vehicle {self._type}')
        return  self._type
    @type.setter
    def type(self, new_type):
        self._type = new_type
    @type.deleter
    def type(self):
        del self._type
    def col(self):
        print(f'color is {self.color}')
        return  self.color



class Bus(Vehicle):
     def __init__(self, trans, type, color, doors):
         super().__init__(type, color, doors)
         self.trans = trans

class Car(Vehicle):
    def __init__(self, view, type, color, doors):
        super().__init__(type, color, doors)
        self.view = view
    def color(self):
        print(f'car color is {self.color}')
        return  self.color




a = Vehicle
b = Bus(trans='akpp', type= 'bus', color='red', doors=4)
c = Car(view='sedan', type='car', color='black', doors=3)

print(b.type)
print(c.col)
print(c.color)

