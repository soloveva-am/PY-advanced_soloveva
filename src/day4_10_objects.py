print('ex2.1')
import random


class shape(object):
    h=None
    w=None
    _name='shape'
    _k=1
    def __init__(self, height, width):
        self.h=height
        self.w=width
    def __str__(self):
        return f'{self._name}, {self.h} points high, {self.w} points wide '

    def area(self):
        return self.h * self.w * self._k


class rectangle(shape):
    _k = 1
    _name = 'rectangle'

class triangle(shape):
    _k = 0.5
    _name = 'triangle'

T = triangle(3, 4)


R = rectangle(3,4)

print(T)

print(T.area())
print(R.area())

print('ex2.2')

class mother:
    k=None
    name='Sarah'
    def __str__(self):
        return 'i am '+ self.name

class daughter(mother):
    __r__=None
    v=True
    name= 'Karen'

M=mother()
D=daughter()
print(M)
print(D)

print('ex2.3')
class animal:
    name=None
    age=None
    info=None
    def return_bias(self):
        L=f'''my name is {str(self.name)}. 
I am {str(self.age)} years old. 
I am an example of {str(self.info)}.'''
        return L

class dolphin(animal):
    info='dolphin, which is a sea mammal carnivore species'
    def swim(self):
        print ('dolphins love swimming')

class zebra(animal):
    info='zebra which is a tropical mammal herbivore species'
    def run(self):
        print ('igogogo')


Z1=zebra()
Z1.name = 'Lulu'
Z1.age = 3
print(Z1.return_bias())
Z1.run()
