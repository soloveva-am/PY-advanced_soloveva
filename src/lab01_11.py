print('N1')
S=[1,2,3]
for i in S:
    if i>2: S.append(2)
    print(i)
#1,1,3,2 - rabotaet!

print('N2')
class Node():
    def __init__(self, value, parent=None):
        self.value=value
        self.parent=parent
        self.right=None
        self.left=None
        if parent !=None:
            if self.value>= parent.value: #side= 'parent.right'
                if parent.right ==None:
                    parent.right =self
                else:
                    Node(value, parent.right)
            else: #side='parent.left'
                if parent.left ==None:
                    parent.left=self
                else:
                    Node(value, parent.left)
    def __str__(self):
        return str(self.value)
class bintree():
    def __init__(self, values):
        self._storage=[]
        self.Top=Node(values.pop(0))
        for v in values:
            self._storage.append(Node(v, self.Top))
    def __iter__(self):
        self._curr=self.Top
        self._past=[None, ]
        return(self)

    def __next__(self): #problem might be here
        self._past.append(self._curr)
        yield self._curr
        if self_curr.left not in self._past:
            self._curr=self._curr.left
        elif self._curr.right not in self._past:
            self._curr=self._curr.right
        elif self._curr!=self.Top:
            self._curr=self._curr.parent
        else: raise StopIteration





L=[14, 15, 9, 27, 6, 5, 89, 8]
K=bintree(L)
for i in K:
    print(i)


