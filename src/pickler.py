import pickle
class pony():
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return (f'pony({self.n})')
    def __str__(self):
        s='i'
        for i in range (self.n):
            s.append('-go')
        return s

from collections import deque
# Коллекция сериализуемых объектов
data = {
    'a': [1, 2.0, 3, 4+6j, float("nan")],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# Сериализация словаря data с использованием
# версии протокола по умолчанию.
print(pickle.dumps(data))

with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    #pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    #pickle.dump(range(10), f, pickle.HIGHEST_PROTOCOL)
    #pickle.dump(print, f, pickle.HIGHEST_PROTOCOL)
    pickle.dump(deque, f, pickle.HIGHEST_PROTOCOL)
    #pickle.dump(pony, f, pickle.HIGHEST_PROTOCOL)



