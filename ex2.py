"""
Без использования библиотечных контейнеров
реализуйте класс  «неизменяемый список».
Такой список, будучи единожды сконструированным,
не может изменять своё содержимое, тем не менее, в этом классе должны
присутствовать операции добавления и удаления элемента по произвольной
позиции, получения элемента по позиции. Подумайте, что должны возвращать
такие операции и как эффективно использовать память.

"""

class UnchangedList:

    def __init__(self, list = []):
        self.obj = ' '.join(map(str, list))

    def print_elts(self):
        for i in self.obj:
            if i != ' ':
                print(i)

    def add_by_idx(self, new_elts = [], idx = 0):
        # кол-во пробелов до вставки == idx
        # место вставки(индекс строки) = idx*2

        self.obj = self.obj[:idx*2] + ' '.join(map(str, new_elts)) + ' ' + self.obj[idx*2:]

    def get_by_idx(self, idx):
        # место вставки(индекс строки) = idx*2
        return self.obj[idx*2]

    def del_by_idx(self, idx):
        self.obj = self.obj[:idx*2-1] + ' ' + self.obj[idx*2+1:]

unch = UnchangedList([1, 3, 'g', 'w', 6])
unch.print_elts()
print('#####')

unch.add_by_idx([4], 3)
unch.print_elts()
print('#####')

print(unch.get_by_idx(4))
print('#####')

unch.del_by_idx(4)
unch.print_elts()
