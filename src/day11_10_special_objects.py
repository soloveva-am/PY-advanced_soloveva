class Complex(object):
    def __init__(self, rat, irr):
        self.rat=rat
        self.irr=irr

    def __str__(self):
        return f'{self.rat} + {self.irr} * i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.rat+other.rat, self.irr+other.irr)
        else:
            return Complex(self.rat+other, self.irr)
    #x + y
    def __radd__(self, other):
    #y + x
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
    #x += y
    #Вычитание
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.rat-other.rat, self.irr-other.irr)
        else:
            return Complex(self.rat-other, self.irr)
    #x - y
    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(other.rat-self.rat, other.irr-self.irr)
        else:
            return Complex(-self.rat+other, self.irr)
    #y - x
    def __isub__(self, other):
        if isinstance(other, Complex):
            self.rat = self.rat - other.rat
            self.irr = self.irr - other.irr
        else:
            self.rat = self.rat - other
    #x -= y
    #Умножение
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.rat*other.rat+self.irr*other.irr, self.rat*other.irr+self.irr*other.rat)
        else: return Сomplex(self.rat*other, self.irr*other)
    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Сomplex(self.rat * other.rat + self.irr * other.irr, self.rat * other.irr + self.irr * other.rat)
        else:
            return Сomplex(self.rat * other, self.irr*other)
    #y * x
    def __imul__(self, other):
        if isinstance(other, Complex):
            self.rat = self.rat * other.rat + self.irr * other.irr
            self.irr = self.rat * other.irr + self.irr * other.rat
        else:
            self.rat = self.rat*other
            self.irr = self.irr*other

    #Деление
    def __truediv__(self, other):
    #x / y
        if isinstance(other, Complex):
            return Complex(self.rat * other.rat + self.irr * other.irr, self.irr*other.rat-self.rat*other.irr)/(other.irr**2+other.rat**2)
        else: return Complex(self.rat/other, self.irr/other)
    def __rtruediv__(self, other):
    #y / x
        if isinstance(other, Complex):
            return Complex(other.rat * self.rat + other.irr * self.irr, other.irr*self.rat-other.rat*self.irr)//(self.irr**2+self.rat**2)
        else: return other/((other.irr**2+other.rat**2)**0,5)
    def __itruediv__(self, other):
        if isinstance(other, Complex):
            self.rat = (self.rat * other.rat + self.irr * other.irr)/(other.irr**2+other.rat**2)
            self.irr = (self.irr*other.rat-self.rat*other.irr)/(other.irr**2+other.rat**2)
        else:
            self.rat = self.rat/other
            self.irr = self.irr/other

x=Complex(3, 4)
y=Complex(7,11)
#print(|x|)
print(x+y)
print(x-y)
print(x*y)
print(y/x)