print('ex2.1')
import random


class shape(object):
    h=None
    w=None
    k=None

    def area(self):
        return self.h * self.w * self.k


class rectangle(shape):
    k = 1

class triangle(shape):
    k = 0.5

T = triangle()
T.h=3
T.w=4

R = rectangle()
R.h=3
R.w=4

print(T)

print(T.area())
print(R.area())

print('ex2.2')

class mother:
    k=None

class daughter(mother):
    __r__=None
    v=True

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
    def stripes(self):
        return random.Random('black', 'white')

Z1=zebra()
Z1.name = 'Lulu'
Z1.age = 3
print(Z1.return_bias())
Z1.run()
