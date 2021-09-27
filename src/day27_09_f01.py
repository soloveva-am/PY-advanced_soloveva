'ex2'
L=[3, 14, 15, 92, 65, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
L1=[3, 5, 7]
L2=[3, 5, 7, 2, 4, 6, 8]
def decorator(F):
        def decorated_f(*args):
                S=F(*args)
                if S==0: print('нет')
                elif S>10: print('много')
                else: print(S)
        return decorated_f

@decorator
def func(L):
        S=0
        for i in L:
                if i%2==0:
                        S+=1
        return S



func(L)
func(L1)
func(L2)
'ex3'
def swap(func):
        def wrap(*args, **kwargs):
                M=func(*reversed(args), **kwargs)
                return M
        wrap.__name__=func.__name__
        return wrap


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)
print(div(2,4,False))
print(div.__name__)
print('ex4')
'''Время вызова функции
Входящие аргументы
Ответ return (если есть, если нет то логгировать '-')
Время завершения работы функции
Время работы функци'''

def log_deco(func, filename):
        from time import time
        def wrapper(*args, **kwargs):
                with open(filename, "a") as file:
                        open_time = time()
                        file.write( 'begin '+ str(open_time))
                        file.write( 'input '+ str(*args) +' '+ str(**kwargs))
                        ans=func(*args, **kwargs)
                        stop_time=time()
                        if ans: file.write( 'output '+ str(ans))
                        else: file.write( 'output '+ '-')
                        file.write('end ' + str(stop_time))
                        file.write('timing ' + str(stop_time-open_time) )
                        file.write('     \n ')
                        file.close()
                return ans
        return wrapper

def fib (A):
        if A<3: return 1
        return fib(A-1)+fib(A-2)

fib=log_deco(fib, 'logs.txt')
for i in range(10): fib(i)
print('finish')