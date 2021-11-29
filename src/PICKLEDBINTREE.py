import pickle
class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.dict=[]
        if parent != None:
            while True:
                if (self.value) >= (parent.value):  # side= 'parent.right'
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
        else:
            try:
                with open("tree_backup.pickle", "rb") as f:

                        l = pickle.load(f)
                        print(l)
                        if isinstance(l, list) and l!=[]:
                            l.append (self.value)
                            self.value=l.pop(0)
                            for i in l:
                                self.dict.append(Node(i,self))
            except FileNotFoundError: pass
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
    def lister(self):
        l=[]
        for i in self:
            l.append(i.value)
        #return list(set(l))
        return l
    def delete(self, instance):
        key=self.find(instance)
        if key !=None:
            print(key.value, 'to be deleted')
            if key.value>=key.parent.value: #side=right
                key.parent.right=None
            else: #side=left
                key.parent.left=None
        rest=key.lister()
        rest1=[]
        for i in rest:
            if i!=instance:
                rest1.append(i)
        for i in rest1: self.add(i)
    def print(self):
        print (self.lister())
    def dump(self):
        l=self.lister()
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
Top.print()
Top.add(88)
i=Top.find(27)
Top.delete(6)
Top.print()
Top.dump()
Top=Node(28)
Top.add(35)
Top.print()
#Top.clear()