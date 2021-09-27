'ex2'
L=[3, 14, 15, 92, 65]

def func(L):
        S=0
        for i in L:
                if i%2==0:
                S+=1
        return S
def decorator(F,L)
        S=F(L)
        if S==0: print('нет')
        elif S>10: print('много')
        else: print(S)
decorator (func, L)
