# Урок: ООП. Магические методы, утиная типизация, статические методы и методы класса.
# Задание Pro:
# 1. Выполнить задание уровня light
# 2. Реализовать собственный класс с использованием магических методов (не менее 10-ти). Можно использовать собственный класс из вебинара 10.


# Выполнение задания Pro:
# 1. Выполнить задание уровня light - выполнено: https://github.com/91472/Lesson11_MagicMethod_DuckTyping_Static-Class_Methods/blob/3d74fab1ed8ab7668689938f1e5fa141501be104/Lite.py
# 2. Реализуем собственный класс Houseroom, объектами которого будут комнаты жилой квартиры, с использованием магических методов.

import matplotlib.pyplot as plt
import pickle

class Houseroom:
    '''
    Документрирование класса.
    Класс Houseroom - экземлпярами являются комнаты произвольного помещения при следующих условиях:
        1) Аргументами класса являются координаты вершин многоуголника, образованного периметром стен по линии пола произвольного количества (именованные параметры **kwargs)
        2) Углы комнаты могут быть произвольные и могут быть ориентированы как наружу, так и во внутрь многоугольника (комнаты)
        3) Порядок следования аргументов имеет значение и для каждого конкретного объекта (комнаты) должен строго следовать по часовой стрелке,
        4) Принцип "замкнутости контура, периметра", т.е. аргументы (координаты) для конкретного объекта должны образовывать замкнутую геометрическую фигуру (многоугольник),
        5) В общем случае аргументы класса описывают замкнутую ломаную линию, образующую многоугольник, состоящий из N сторон и N углов, без радиусов и дуг,
        6) Пример аргументов объекта "комната" в формате словаря из точек-координат вершин многоугольника (8 точек-координат):
        {'p1': (0,0), 'p2': (0,400), 'p3': (-100,400), 'p4': (-100,600), 'p5': (200,600), 'p6': (200,500), 'p7': (600,500), 'p8': (600,0)},
        где, например, 'p2': (0,4) - означает вторую по счету по частовой стрелке вершину с координатами: (х = 0, y =4).
        7) Масштаб по умолчанию: отрезок (x = 0, y = 1) = 1см.
    Для экземпляров класса Houseroom определены поведения следующих функций:
        # 1) вывод на экран объекта функцией print,
        # 2) определение длины объекта функцией len (периметр комнаты в см)
        # 3) определение объекта к типу float (значение площади комнаты)
        # 4) определение объекта к типу int (количество сторон комнаты)
        # 5) магический метод сложения объектов (в данном классе под суммой объектов понимается сумма площадей этих экземпляров класса)
        # 6) результат сравнения объектов на равенство (==) по критерию равенства всех площадей, периметра и количества сторон объектов
        # 7) результат сравнения объектов на знак меньше (<) по критерию сравнения их площадей
        # 8) определение поведения оператора целочисленной части от деления // (деление площадей фигур через оператор //)
        # 9) определение поведения оператора остатка от деления % (деление площадей фигур через оператор %)
        # 10) магический метод определения поведения при доступе к элементу, используя синтаксис self[key]
        # 11) магический метод определения поведения при присваивании значения элементу, используя синтаксис self[key] = value
        # 12) магический метод определения поведения при удалении элемент по ключу key, используя синтаксис del self[key]
        # 13) магический метод определения поведения при вызове экземпляра класса как функции, используя синтаксис self()
        # 14) магические методы определения поведения передачи набора данных при сериализации и десериализации
    '''
    def __init__(self, room_name, **kwargs):  # магический метод инициализация объекта
        self.point = kwargs  # аргументы, словарь именованных параметров с точками и их координатами
        self.room_name = room_name
        self.x = [i[0] for i in self.point.values()]
        self.y = [i[1] for i in self.point.values()]

    def __str__(self): # магический метод формата вывода на экран созданного объекта через функцию print
        plt.plot(self.x, self.y, c='r')
        plt.plot([self.x[0], self.x[-1]], [self.y[0], self.y[-1]], c='r')
        plt.title(f'Объект {self.room_name}, перимерт {len(self)/100}м, площадь {self.area()}м2')
        plt.grid()
        plt.show()
        return f'Объект {self.room_name}, перимерт {len(self)/100}м, площадь {self.area()}м2'

    def area(self): #метод класса, вычисление площади комнаты
        return round(abs(sum([((self.y[i-1] + self.y[i])/2) * (self.x[i-1] - self.x[i]) for i in range(len(self.x))]))/10000, 2)

    def __len__(self): # магический метод вычисления длины объекта (в данном классе длиной объекта является целая часть его периметра в см)
        return int(self.perimeter())

    def perimeter(self): #метод класса, вычисление периметра комнаты
        return round(sum([((self.y[i-1] - self.y[i])**2 + (self.x[i-1] - self.x[i])**2)**0.5 for i in range(len(self.x))]), 2)

    def __float__(self):
        return float(self.area())  # float определеяем как площадь объекта

    def __int__(self):
        return len(self.x)  # int определеяем как количество сторон объекта-фигуры

    def __add__(self, other): # магический метод сложения объектов (в данном классе под суммой объектов понимается сумма площадей этих экземпляров класса)
        if isinstance(other, Houseroom):
            return self.area() + other.area()
        if isinstance(other, (int, float)):
            return self.area() + other

    def __radd__(self, other): # магический метод отражения арифметического оператора + (тоже, что и __add__, но обратный порядок применения объектов)
        return self + other

    def __eq__(self, other):  # магический метод определения поведения оператора равенства ==
        return self.area() == other.area() and self.perimeter() == other.perimeter() and len(self.x) == len(other.x)

    def __lt__(self, other):  # магический метод определения поведения оператора сравнения <
        return self.area() < other.area()

    def __floordiv__(self, other):  # магический метод определения поведения оператора целочисленной части от деления //
        return self.area() // other.area()

    def __mod__(self, other):  # магический метод определения поведения оператора остатка от деления %
        return self.area() % other.area()

    def __getitem__(self, key):  # магический метод определения поведения при доступе к элементу, используя синтаксис self[key]
        return [(j,self.y[i]) for i,j in enumerate(self.x)][key]

    def __setitem__(self, key, value):  # магический метод определения поведения при присваивании значения элементу, используя синтаксис self[nkey] = value
        (self.x[key], self.y[key]) = value

    def __delitem__(self, key):  # магический метод определения поведения при удалении элемент по ключу key, используя синтаксис del self[key]
        del (self.x[key], self.y[key])

    def __call__(self, *args, **kwargs): # магический метод определения поведения при вызове экземпляра класса как функции, используя синтаксис self()
        return (round(self.area() * kwargs['room_height'], 2), round((self.perimeter()/100) * kwargs['room_height'] - sum(args), 2))  # вызов вернет кортеж значений объема комнаты и площади ее стен с учетом или без учета проемов (не именованные параметры являются площадями проемов)

    def __getstate__(self): #магический метод определения поведения передачи набора данных при сериализации
        dict_state = {'point': {'p1': (0, 0)}, 'room_name': 'Комната №1 после десериализации', 'x': [0], 'y': [0]}
        return dict_state #будем передавать при сериализации список из одного элемента 0 для последующей передачи "обнуленных координат" после десериализации

    def __setstate__(self, state): #магический метод определения поведения приема набора данных от getstate при десериализации
        self.__dict__ = state


if __name__ == '__main__':
    help(Houseroom)
    room1 = Houseroom('Комната №1', p1 = (0,0), p2 = (0,400), p3 = (-100,400), p4 = (-100,600), p5 = (200,600), p6 = (200,500), p7 = (600,500), p8 = (600,0))  # создаем экземпляр класса комната №1
    print(room1)
    room2 = Houseroom('Комната №2', p1=(0, 200), p2=(0, 400), p3=(200, 400), p4=(200, 600), p5=(400, 600), p6=(400, 400), p7=(600, 400), p8=(600, 200), p9=(400, 200), p10=(400, 0), p11=(200, 0), p12=(200, 200))  # создаем экземпляр класса комната №2
    print(room2)
    room3 = Houseroom('Комната №3', p1=(300, 400), p2=(510, 1100), p3=(1200, 800), p4=(900, 500), p5=(500, 600))  # создаем экземпляр класса комната №3
    print(room3)
    print('\nДлина объекта room3: ', len(room3), ', Приведение объекта к типу float: ', float(room3), ' и к типу int: ', int(room3))
    print('\nСумма объектов room1, room2, room3: ', room1+room2+room3)
    print(f'\nРезультат сравнения на равенство двух комнат room1 и room2, room1 == room2: {room1 == room2}, и на знак меньше room1 < room2: {room1 < room2}')
    print(f'\nРезультат целочисленного деления и остатка от деления room1 на room3 соответственно: {room1 // room3}, {room1 % room3}')
    print(f'\nИтерация по room1:')
    for i,j in enumerate(room1):
        print(f'Координата вершины N{i+1}: {j}')
    print(f'\nИзменяем координату вершины №1 с (0,0) на (100,100) для room1:')
    room1[0] = (100,100)
    for i,j in enumerate(room1):
        print(f'Координата вершины N{i+1}: {j}')
    print(room1)

    print(f'\nУдаляем координату вершины №2 (0,400) для room2:')
    del room2[1]
    for i, j in enumerate(room2):
        print(f'Координата вершины N{i + 1}: {j}')
    print(room2)

    volume_area = room1(room_height = 2.7)
    print(f'\nКортеж из значений объема комнаты room1 и площади стен комнаты высотой без учета площадей проемов: {volume_area}')
    volume_area2 = room1(2, 3, room_height = 2.7)
    print(f'Кортеж из значений объема комнаты room1 и площади стен комнаты c учетом площадей проемов: {volume_area2}')

    with open('room1.pickle', 'wb') as f:
        pickle.dump(room1, f)
        print(f'\nСериализация объекта room1 в файл room1.pickle c передачей одной нулевой координаты, до сериализации: {room1}')
    with open('room1.pickle', 'rb') as f:
        room1_empty = pickle.load(f)
        print(f'\nДесериализация объекта room1 в объект room1_empty c одной нулевой координатой, после десериализации: {room1_empty}')

    for i,j in enumerate(room1_empty):
        print(f'Координата вершины N{i+1}: {j}')

    print('\nОпределим новые координаты для десериализованного объекта room1_empty как для квадрата (100,100), (100,200), (200,200), (200,100)  и выведем объект на экран: ')
    new_coord = [(100,100), (100,200), (200,200), (200,100)]
    del room1_empty[0]
    for i in range(len(new_coord)):
        room1_empty.x.append(new_coord[i][0])
        room1_empty.y.append(new_coord[i][1])
    print(room1_empty)