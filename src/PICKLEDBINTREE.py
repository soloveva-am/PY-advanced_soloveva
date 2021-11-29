import pickle
class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.dict=[self, ]
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
        if parent==None:
            with open("tree_backup.pickle", "wb") as f:
                try:
                    l = pickle.load(f)
                    if isinstance(l, list) and l!=[]:
                        l.append (self.value)
                        self.value=l.pop(0)
                        for i in l:
                            self.add(i)
                except Exception: pass

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
    def add(self, n):
        if self.parent==None:
            self.dict.append(Node(n, self))
        else: self.parent.add(n)
    def find(self, n):
        for i in self:
            if i.value==n:
                return i #
        else: return ('None')
    def __list__(self):
        l=[]
        for i in self:
            l.append(i.value)
        return list(set(l))
    def delete(self, instance):
        key=self.find(instance)
        if key !=None:
            if key.value>=key.parent.value: #side=right
                key.parent.right=None
            else: #side=left
                key.parent.left=None
        rest=list(key).pop(0)
        for i in rest: self.add(i)
    def print(self):
        print (self.__list__())
    def dump(self):
        l=list(self)
        with open("tree_backup.pickle", "wb") as f:
            pickle.dump(l, f, pickle.HIGHEST_PROTOCOL)
    def close(self):
        if self.parent==None:
            self.dump()
        else: self.parent.dump()
    def clear(self):
        with open('tree_backup.pickle', 'w') as f:
            f.write('0')






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