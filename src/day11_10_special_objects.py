class Complex(object):
    def __init__(self, rat, irr):
        self.rat = rat
        self.irr = irr

    def __str__(self):
        return f'{self.rat} + {self.irr} * i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.rat + other.rat, self.irr + other.irr)
        else:
            return Complex(self.rat + other, self.irr)

    # x + y
    def __radd__(self, other):
        # y + x
        if isinstance(other, Complex):
            return Complex(self.rat + other.rat, self.irr + other.irr)
        else:
            return Complex(self.rat + other, self.irr)

    def __iadd__(self, other):
        if isinstance(other, Complex):
            self.rat = self.rat + other.rat
            self.irr = self.irr + other.irr
        else:
            self.rat = self.rat + other

    # x += y
    # Вычитание
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.rat - other.rat, self.irr - other.irr)
        else:
            return Complex(self.rat - other, self.irr)

    # x - y
    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(other.rat - self.rat, other.irr - self.irr)
        else:
            return Complex(-self.rat + other, self.irr)

    # y - x
    def __isub__(self, other):
        if isinstance(other, Complex):
            self.rat = self.rat - other.rat
            self.irr = self.irr - other.irr
        else:
            self.rat = self.rat - other

    # x -= y
    # Умножение
    def __mul__(self, other):
        if not isinstance(other, Complex):
            return Сomplex(self.rat * other, self.irr * other)
        else:
            return Complex(self.rat * other.rat + self.irr * other.irr, self.rat * other.irr + self.irr * other.rat)

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Сomplex(self.rat * other.rat + self.irr * other.irr, self.rat * other.irr + self.irr * other.rat)
        else:
            return Сomplex(self.rat * other, self.irr * other)

    # y * x
    def __imul__(self, other):
        if isinstance(other, Complex):
            self.rat = self.rat * other.rat + self.irr * other.irr
            self.irr = self.rat * other.irr + self.irr * other.rat
        else:
            self.rat = self.rat * other
            self.irr = self.irr * other

    # Деление
    def __truediv__(self, other):
        # x / y
        if isinstance(other, Complex):
            return Complex(self.rat * other.rat + self.irr * other.irr, self.irr * other.rat - self.rat * other.irr) / (
                        other.irr ** 2 + other.rat ** 2)
        else:
            return Complex(self.rat / other, self.irr / other)

    def __rtruediv__(self, other):
        if not isinstance(other, Complex):
            return other / ((other.irr ** 2 + other.rat ** 2) ** 0, 5)
        # y / x
        else:
            return Complex(other.rat * self.rat + other.irr * self.irr,
                           other.irr * self.rat - other.rat * self.irr) / (self.irr ** 2 + self.rat ** 2)

    def __itruediv__(self, other):
        if isinstance(other, Complex):
            self.rat = (self.rat * other.rat + self.irr * other.irr) / (other.irr ** 2 + other.rat ** 2)
            self.irr = (self.irr * other.rat - self.rat * other.irr) / (other.irr ** 2 + other.rat ** 2)
        else:
            self.rat = self.rat / other
            self.irr = self.irr / other


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def fromstr(cls, str1):
        return cls(*list(map(float, str1.split(', '))))

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __abs__(self):
        return float((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __truediv__(self, other):
        if not isinstance(other, Vector): return (self.x/other, self.y/other, self.z/other)

    def __mul__(self, other):
        return float(self.x*other.x+self.y*other.y+self.z*other.z)
    #x * y
    def __rmul__(self, other):
        return float(self.x * other.x + self.y * other.y + self.z * other.z)

def Walker(N, L):
    m=0
    S=Vector(0, 0, 0)
    for i in L:
        V=Vector.fromstr(i)
        S=S+V
        if abs(V)>m:
            m=abs(V)
            fm=V
    S=S/N
    print (f' the most distant is {fm}, centremass is {S}')




x = Complex(3, 4)
y = Complex(7, 11)
# print(|x|)
print(x + y)
print(x - y)
print(x * y)
print(y / x)

x = Vector(1, 2, 3)
y = Vector(3, 4, 5)
k = abs(x)
S = Vector.fromstr('3, 4, 5')
print(x + S)
print(abs(x))
L={'1, 2, 3', '4, 5, 6', '7, -8, 9'}
Walker(3, L)
print(x*y)