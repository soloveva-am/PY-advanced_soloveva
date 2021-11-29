import pickle
import os
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
    def __getstate__(self):
        # Копируем состояние объекта из self.__dict__, который
        # содержит все атрибуты. Всегда используйте dict.copy()
        # во избежании модификации состояния самого объекта.
        state = self.__dict__.copy()
        # Удаляем несериализуемые атрибуты.
        del state['file']
        return state

    def __setstate__(self, state):
        # Восстанавливаем атрибуты объекта.
        self.__dict__.update(state)
        # Восстанавливаем состояние открытого ранее файла. Для этого нам надо
        # заного открыть его и прочитать необходимое количество строк.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Создаем атрибут для file.
        self.file = file



print(os.getcwd())
print(next(iter(textloader("C:\\Users\msolo\PycharmProjects\pythonProject2\src\sample"))))
with open('TLdata.pickle', 'wb') as f:
    pickle.dump(textloader, f, pickle.HIGHEST_PROTOCOL)

