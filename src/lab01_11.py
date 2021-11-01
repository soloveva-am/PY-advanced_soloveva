import os

print('N1')
S = [1, 2, 3]
for i in S:
    if i > 2: S.append(2)
    print(i)
# 1,1,3,2 - rabotaet!

print('N2')


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        if parent != None:
            while True:
                if self.value >= parent.value:  # side= 'parent.right'
                    if parent.right == None:
                        parent.right = self
                        self.parent = parent
                        break
                    else:
                        parent = parent.right
                else:  # side='parent.left'
                    if parent.left == None:
                        parent.left = self
                        self.parent = parent
                        break
                    else:
                        parent = parent.left

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        self._curr = self
        self._past = []
        return (self)

    def __next__(self):  # problem might be here
        self._past.append(self._curr)
        K = self._curr
        if self._curr.left != None and self._curr.left not in self._past:
            self._curr = self._curr.left
        elif self._curr.right != None and self._curr.right not in self._past:
            self._curr = self._curr.right
        elif self._curr != self:
            self._curr = self._curr.parent
        else:
            raise StopIteration
        return K


L = [14, 15, 9, 27, 6, 5, 89, 8]

Top = Node(10)
S = []
for i in L:
    S.append(Node(i, Top))

print(Top)
print(Top.right)
print(Top.left)
print(Top.right.right)
print()
for i in Top:
    print(i)

print('N3')


class textloader():
    def __init__(self, dir):
        self.dir = dir
        os.chdir(dir)

    def __len__(self):
        return len(os.listdir(self.dir))


    def __getitem__(self, name):
        os.chdir(self.dir)
        with open(name, 'r', encoding='utf-8') as file:
            S = ''
            for string in file:
                S += string.lower()
                S += '\n'
            return S

    def __iter__(self):
        for name in os.listdir(self.dir):
            yield self.__getitem__ (name)

print(os.getcwd())
print(next(iter(textloader("C:\\Users\msolo\PycharmProjects\pythonProject2\src\sample"))))

print('N4')
def count_coroutine():
    Log=[]
    I=0
    x='start'
    while True:
        x=yield x
        Log.append(x)
        I+=1
        avg = sum(Log)/I
        S=float(0)
        for i in Log:
            S+=(i-avg)**2
        S=(S/I)**0.5
        print(f'{I} numbers, {avg} at average, at {S} different')

coroutine = count_coroutine()
print(next(coroutine))
for i in range(10):
    print(coroutine.send(i))
coroutine.close()

print('N5')
"""class write_to_file(filename):
    def __init__:
        self.filename=str(filename)+'.txt'
    def __call__(self, message):
        with open(self.filename, 'a') as file:
            file.write(message) По-честному не могу"""

def write_to_file():
    filename, message = yield
    with open(self.filename, 'a') as file:
        file.write(message)

def connect_user():
    users=[]
    x = yield
    keys= x.split()
    if keys[0] == 'auth':
        users.append(keys[1])

    elif keys[0]=='disconnect':
        users.remove(keys[1])
    else:
        username=keys.pop(0)
        message=' '.join(keys)
        if username in users:
            write_to_file.send(username, message)




