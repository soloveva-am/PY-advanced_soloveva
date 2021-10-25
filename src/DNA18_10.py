import random
from abc import abstractmethod


class NA:

    def __init__(self, l1):
        self.d=self.dict()
        for i in l1:
            if i not in self.d: raise ValueError
        self.line1=l1

    @abstractmethod
    def dict(self):
        pass

    def __str__(self):
        return (f"3'-{self.line1}-5'")
    def complement(self, l):
        s=''
        for i in l:
            s+=self.d[i]
        return s
    def __add__(self, other):
        return str(self.line1+other.line1)
    def __radd__( self, other):
        return str(self.line1 + other.line1)
    def __mul__( self, other):
        L1= len(self.line1)
        L2= len(other.line1)
        L=min(L1, L2)
        s=''
        for i in range(L):
            if random.random()>0.5: s+= (self.line1[i])
            else: s+=(other.line1[i])
        return str(s)+str(self.line1[L:L1])+str(other.line1[L:L2])
    def __rmul__(self, other):
        L1, L2 = len(self.line1), len(other.line1)
        L=min(L1, L2)
        s=''
        for i in range(L):
            if (random.random()>0.5 ): s.append(self.line1[i])
            else: s.append(other.line1[i])
        return str(s)+str(self.line1[L,L1])+str(other.line1[L,L2])

    def __eq__( self, other):
        C=self.__class__
        if isinstance(other, C) and self.line1==other.line1:
            return True
        return False
    @abstractmethod
    def __get__(self, instance, owner):
        pass
    def __call__(self):
        print('это нуклеиновая кислота')
        print(self)

class DNA(NA):
    def dict(self):
        return {'A':'T', 'T':'A', 'C':'G', 'G':'C' }

    def __init__(self, l1):
        super().__init__( l1)
        self.line2=self.complement(l1)

    def __str__(self):
        return f"3'-{self.line1}-5'\n   {self.line2}"
    def __add__(self, other):
        return DNA(super().__add__( other))
    def __radd__(self, other):
        return DNA(super().__add__( other))
    def __mul__(self, other):
        return DNA(super().__mul__( other))
    def __rmul__(self, other):
        return DNA(super().__mul__( other))
    def __get__ (self, instance, owner):
        return self.line1[instance], self.line2[instance]

class RNA(NA):
    def dict(self):
        return {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    def __mul__(self, other):
        return (RNA(super().__mul__( other)))
    def __add__(self, other):
        return RNA(super().__add__( other))
    def __radd__(self, other):
        return RNA(super().__add__( other))



    def __rmul__(self, other):
        return (RNA(super().__mul__( other)))
    def __get__(self, instance, owner):
        return self.line1[instance]


D=DNA('AAATTT')
print (D)
R=RNA('ACUGCU')
print(R)
R1=RNA('AUAUAU')
D1=DNA('GGGCCC')
R2=RNA('GGGCCC')
print(D*D1)
print(R+R1)
D()
print(D1==R)
print(D==D)
print(D==D1)
print(D1==R2)
print(D1)
print(R2)
