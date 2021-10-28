

print('N1')


def print_map(function, iterable):
    i1 = iter(iterable)

    while True:
        try:
            print(function(next(i1)))
        except StopIteration:
            break
print_map(float, range(5))

print('N2')


def fib_range(n, a=0, b=1):
    for i2 in range (n):
        yield b
        a,b= b, (b+a)

for i in fib_range(6):
    print(i)


print('N3')


def my_map(function, iterable):
    i=iter(iterable)

    while True:
        try: e=next(i)
        except StopIteration: break
        yield function(e)


def my_zip(*iterables):
    L=[]
    for iterable in iterables:
       L.append(iter(iterable))
    while True:
        S=[]
        try:
            for i in L:
                S.append(next(i))
            yield tuple(S)
        except StopIteration:
            break


def my_enumerate(iterable):
    i=0
    for j in iterable:
        yield (i, j)
        i+=1


for i in my_map(float, range(5)):
    print(i)
print(' ')


for i in my_enumerate( range(5)):
    print(i)
print(' ')

for i in my_zip([1, 2, 3], [2, 3, 4], ['a','b','c']):
    print(i)
print(' ')
print('N4')

import itertools
print('N4.1')


def get_cartesian_product(a, b):
    S=itertools.product(a,b,repeat=1)
    return list(S)
print(get_cartesian_product([1,2], [5,6,7]))

print('N4.2')


def get_permutations(s, n):
    return sorted(itertools.permutations(s,n))
print(get_permutations('fgahk', 3))
print('N4.3')


def get_combinations(s,n):
    S=[]
    for i in range(1,n+1):
        for j in itertools.permutations(s,i):
            S.append(j)
    return S
print(get_combinations('fgahk', 3))
print('N4.4')


def get_cwr(s,n):
    return list (itertools.combinations_with_replacement(s,n))
print(get_cwr('kgjf',2))
print('N4.5')


def compress_string(s):
    S=[]
    for i in itertools.groupby(s):
        c=0
        for _ in i[1]:
            c+=1
        S.append((i[0], c))
    return(S)
print(compress_string('ggghhdddgg'))
print('N4.6')


def maxvalue(K, m):
    M=0
    for i in itertools.product(*K):
       S=0
       for j in i:
            S+=j^2
       S%=m
       if S>M: M=S
    return M
lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maxvalue(lists, 1000))
a=1
b=2
c=3
print ('aa{}  {}, {}'.format(a, b, c))







