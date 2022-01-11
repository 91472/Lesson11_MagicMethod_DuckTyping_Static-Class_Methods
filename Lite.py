# Урок: ООП. Магические методы, утиная типизация, статические методы и методы класса.
# Задание Lite:
# 1. Реализовать собственный класс с использованием магических методов (не менее 5-ти). Например, можно использовать класс из вебинара Point2D.


# Выполнение задания Lite:
# Реализуем собственный класс Figure_2D, объектами которого могут быть следующие геометрические фигуры: quadrat (квадрат), rectangle (прямоугольник),
# parallelogram (параллелограмм), rhombus (ромб), trapezoid (трапеция), triangle (треугольник), circle (окружность), с использованием магических методов.

from math import pi

class Figure_2D:
    '''
    Домументрирование класса.
    Класс Figure_2D - это геометрические плоские фигуры. Экземлпярами класса могут быть следующие фигуры:
        quadrat (квадрат),
        rectangle (прямоугольник),
        parallelogram (параллелограмм),
        rhombus (ромб),
        trapezoid (трапеция),
        triangle (треугольник),
        circle (окружность).
    При создания экземпляра класса необходимо в качестве параметров указать:
        Тип фигуры (первый аргумент, type_figure) может быть один из перечисленных выше.
        Длины сторон, высота, радиус (второй аргумент, **kwargs - именованные параметры):
            для квадрата - длина одной стороны (a),
            для прямоуголника - длины двух различных сторон (a и b),
            для параллелограмма - длины двух различных сторон (a и b) и длина высоты опущенной на одну из сторон (ha или hb),
            для ромба - длина стороны (a) и длина высоты опущенной на эту сторону (h),
            для трапеции - длины оснований (а и b) и длины боковых сторон (с и d),
            для треугольника - длины все трех сторон (a, b и c),
            для окружности - радиус (r).

    Для экземпляров класса Figure_2D определены поведения следующих функций:
        1) вывод на экран объекта функцией print,
        2) определение длины объекта функцией len (целая часть периметра с множителем 100 для масшатабирования точности)
        3) определение объекта к типу float (значение площади фигуры)
        4) определение объекта к типу int (количество сторон фигуры)
        5) сложение однотипных объектов между собой (результат сложения - однотипный объект с длинами сторон, равными сумме длин слогаемых объектов)
        6) результат сравнения объектов на равенство (==) по критерию равенства всех сторон и других параметров, если применимо
        7) результат сравнения объектов на знак меньше (<) по критерию сравнения их площадей
        8) определение поведения оператора целочисленной части от деления // (деление площадей фигур через оператор //)
        9) определение поведения оператора остатка от деления % (деление площадей фигур через оператор %)
    '''
    def __init__(self, type_figure, **kwargs): # магический метод инициализация объекта
        self.figure = type_figure # аргумент, тип фигуры
        self.side = kwargs # аргумент, словарь именованных параметров с длинами сторон фигур (а также высота или радиус, если требуется)
        if (self.figure, self.side.keys()) not in [('circle', {'r'}), ('quadrat', {'a'}), ('rectangle', {'a', 'b'}), ('parallelogram', {'a', 'b', 'ha'}), ('parallelogram', {'a', 'b', 'hb'}), ('triangle', {'a', 'b', 'c'}), ('trapezoid', {'a', 'b', 'c', 'd'}), ('rhombus', {'a', 'h'})] or any(values <= 0 for values in self.side.values()):
            raise Exception('Ошибка ввода аргументов') # если уловие True, то принудительно запустить исключение
        if self.area() == 0 or isinstance(self.area(), complex): # проверка корректности заданных длин сторон треугольника
            raise Exception(f'Треугольника со сторонами {self.side["a"]}, {self.side["b"]}, {self.side["c"]} не существует!')

    def __str__(self): # магический метод формата вывода на экран созданного объекта через функцию print
        return f'Фигура {self.figure} с радиусом r {self.side}' if self.figure == 'circle' else f'Фигура {self.figure} со сторонами {self.side}' if self.figure == 'quadrat' or self.figure == 'rectangle' or self.figure == 'triangle'  else f'Фигура {self.figure} с основаниями a,b и сторонами c,d {self.side}' if self.figure == 'trapezoid' else f'Фигура {self.figure} со сторонами a и высотой к ней h {self.side}' if self.figure == 'rhombus' else f'Фигура {self.figure} со сторонами a,b и высотой {self.side}'

    def area(self): #метод класса, вычисление площади заданной фигуры
        if self.figure == 'quadrat':
             area_fig = self.side['a']**2
        elif self.figure == 'rectangle':
             area_fig = self.side['a'] * self.side['b']
        elif self.figure == 'parallelogram':
             if self.side.keys() in [{'a', 'b', 'ha'}]:
                 area_fig = self.side['a'] * self.side['ha']
             elif self.side.keys() in [{'a', 'b', 'hb'}]:
                 area_fig = self.side['b'] * self.side['hb']
        elif self.figure == 'rhombus':
             area_fig = self.side['a'] * self.side['h']
        elif self.figure == 'trapezoid':
             p = sum(self.side.values()) / 2
             area_fig = ((self.side['a'] + self.side['b'])/abs(self.side['a'] - self.side['b']))*(((p-self.side['a'])*(p-self.side['b'])*(p-self.side['a']-self.side['c'])*(p-self.side['a']-self.side['d']))**0.5)
        elif self.figure == 'triangle':
            p = sum(self.side.values()) / 2
            area_fig = (p * (p - self.side['a']) * (p - self.side['b']) * (p - self.side['c'])) ** 0.5
        elif self.figure == 'circle':
             area_fig = pi*self.side['r']**2
        return area_fig

    def __len__(self): # магический метод вычисления длины объекта (в данном классе длиной объекта-геометрической плоской фигуры является целая часть его периметра умноженная на масштабирующий коэффициент 100)
        return int(100*self.perimeter())

    def perimeter(self): #метод класса, вычисление периметра заданной фигуры
        if self.figure == 'quadrat':
             perimeter_fig = 4 * self.side['a']
        elif self.figure == 'rectangle':
             perimeter_fig = 2 * sum(self.side.values())
        elif self.figure == 'parallelogram':
             perimeter_fig = 2 * (self.side['a'] + self.side['b'])
        elif self.figure == 'rhombus':
             perimeter_fig = 4 * self.side['a']
        elif self.figure == 'trapezoid':
             perimeter_fig = sum(self.side.values())
        elif self.figure == 'triangle':
            perimeter_fig = sum(self.side.values())
        elif self.figure == 'circle':
             perimeter_fig = 2 * pi * self.side['r']
        return perimeter_fig

    def __float__(self):
        return float(self.area())  # float определеяем как площадь объекта-фигуры

    def __int__(self):
        dict_figure = {'quadrat': 4, 'rectangle': 4, 'parallelogram': 4, 'rhombus': 4, 'trapezoid': 4, 'triangle': 3, 'circle': 0}
        return dict_figure[self.figure]  # int определеяем как количество сторон объекта-фигуры

    def __add__(self, other): # магический метод сложения объектов (в данном классе под суммой объектов понимается новый однотипный объект со стороными равными сумме сторон слогаемых однотипных объектов)
        if isinstance(other, Figure_2D) and self.figure == other.figure:
            if self.figure == 'quadrat':
                return Figure_2D(self.figure, a = self.side['a'] + other.side['a'])
            if self.figure == 'rectangle':
                return Figure_2D(self.figure, a = self.side['a'] + other.side['a'], b = self.side['b'] + other.side['b'])
            if self.figure == 'parallelogram':
                if self.side.keys() in [{'a', 'b', 'ha'}] and other.side.keys() in [{'a', 'b', 'ha'}]:
                    return Figure_2D(self.figure, a = self.side['a'] + other.side['a'], b = self.side['b'] + other.side['b'], ha = self.side['ha'] + other.side['ha'])
                elif self.side.keys() in [{'a', 'b', 'hb'}] and other.side.keys() in [{'a', 'b', 'hb'}]:
                    return Figure_2D(self.figure, a = self.side['a'] + other.side['a'], b = self.side['b'] + other.side['b'], ha = self.side['hb'] + other.side['hb'])
                else:
                    raise Exception(f'Параллелограммы с высотами опущенными на разные стороны не могут быть сложены!')
            if self.figure == 'rhombus':
                return Figure_2D(self.figure, a = self.side['a'] + other.side['a'], h = self.side['h'] + other.side['h'])
            if self.figure == 'trapezoid':
                return Figure_2D(self.figure, a=self.side['a'] + other.side['a'], b = self.side['b'] + other.side['b'], c = self.side['c'] + other.side['c'], d = self.side['d'] + other.side['d'])
            if self.figure == 'triangle':
                return Figure_2D(self.figure, a=self.side['a'] + other.side['a'], b = self.side['b'] + other.side['b'], c = self.side['c'] + other.side['c'])
            if self.figure == 'circle':
                return Figure_2D(self.figure, r = self.side['r'] + other.side['r'])

    def __eq__(self, other):  # магический метод определения поведения оператора равенства ==
        return self.side == other.side

    def __lt__(self, other):  # магический метод определения поведения оператора сравнения <
        return self.area() < other.area()

    def __floordiv__(self, other):  # магический метод определения поведения оператора целочисленной части от деления //
        return self.area() // other.area()

    def __mod__(self, other):  # магический метод определения поведения оператора остатка от деления %
        return self.area() % other.area()

if __name__ == '__main__':
    quadrat_1 = Figure_2D('quadrat', a = 1)  # создаем экземпляр класса квадрат №1
    rectangle_1 = Figure_2D('rectangle', a = 1, b = 2)  # создаем экземпляр класса прямоугольник №1
    parallelogram_1 = Figure_2D('parallelogram', a = 1, b = 2, ha = 1)  # создаем экземпляр класса параллелограмм №1
    rhombus_1 = Figure_2D('rhombus', a = 2, h = 1)  # создаем экземпляр класса ромб №1
    trapezoid_1 = Figure_2D('trapezoid', a = 2, b = 4, c = 1, d = 2)  # создаем экземпляр класса трапеция №1
    triangle_1 = Figure_2D('triangle', a = 1, b = 2, c = 2)  # создаем экземпляр класса треугольник №1
    circle_1 = Figure_2D('circle', r = 2)  # создаем экземпляр класса окружность №1
    print(quadrat_1, ', Длина объекта: ', len(quadrat_1), ', Приведение объекта к типу float: ', float(quadrat_1), ' и к типу int: ', int(quadrat_1))
    print(f'Результат сложения двух квадратов quadrat_1: {quadrat_1+quadrat_1}')
    print(f'Результат сравнения на равенство двух квадратов quadrat_1: {quadrat_1 == quadrat_1}, и на знак меньше: {quadrat_1 < quadrat_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{rectangle_1}" на "{quadrat_1}" соответственно: {rectangle_1 // quadrat_1}, {rectangle_1 % quadrat_1}\n')

    print(rectangle_1, ', Длина объекта: ', len(rectangle_1), ', Приведение объекта к типу float: ', float(rectangle_1), ' и к типу int: ', int(rectangle_1))
    print(f'Результат сложения двух прямоугольников rectangle_1: {rectangle_1 + rectangle_1}')
    print(f'Результат сравнения на равенство двух прямоуголников rectangle_1: {rectangle_1 == rectangle_1}, и на знак меньше: {rectangle_1 < rectangle_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{parallelogram_1}" на "{rectangle_1}" соответственно: {parallelogram_1 // rectangle_1}, {parallelogram_1 % rectangle_1}\n')

    print(parallelogram_1, ', Длина объекта: ', len(parallelogram_1), ', Приведение объекта к типу float: ', float(parallelogram_1), ' и к типу int: ', int(parallelogram_1))
    print(f'Результат сложения двух параллелограммов parallelogram_1: {parallelogram_1 + parallelogram_1}')
    print(f'Результат сравнения на равенство двух параллелограммов parallelogram_1: {parallelogram_1 == parallelogram_1}, и на знак меньше: {parallelogram_1 < parallelogram_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{rhombus_1}" на "{trapezoid_1}" соответственно: {rhombus_1 // trapezoid_1}, {rhombus_1 % trapezoid_1}\n')

    print(rhombus_1, ', Длина объекта: ', len(rhombus_1), ', Приведение объекта к типу float: ', float(rhombus_1), ' и к типу int: ', int(rhombus_1))
    print(f'Результат сложения двух ромбов rhombus_1: {rhombus_1 + rhombus_1}')
    print(f'Результат сравнения на равенство двух ромбов rhombus_1: {rhombus_1 == rhombus_1}, и на знак меньше: {rhombus_1 < rhombus_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{triangle_1}" на "{triangle_1}" соответственно: {triangle_1 // triangle_1}, {triangle_1 % triangle_1}\n')

    print(trapezoid_1, ', Длина объекта: ', len(trapezoid_1), ', Приведение объекта к типу float: ', float(trapezoid_1), ' и к типу int: ', int(trapezoid_1))
    print(f'Результат сложения двух трапеций trapezoid_1: {trapezoid_1 + trapezoid_1}')
    print(f'Результат сравнения на равенство двух трапеций trapezoid_1: {trapezoid_1 == trapezoid_1}, и на знак меньше: {trapezoid_1 < trapezoid_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{circle_1}" на "{triangle_1}" соответственно: {circle_1 // triangle_1}, {circle_1 % triangle_1}\n')

    print(triangle_1, ', Длина объекта: ', len(triangle_1), ', Приведение объекта к типу float: ', float(triangle_1), ' и к типу int: ', int(triangle_1))
    print(f'Результат сложения двух треугольков triangle_1: {triangle_1 + triangle_1}')
    print(f'Результат сравнения на равенство двух треугольков triangle_1: {triangle_1 == triangle_1}, и на знак меньше: {triangle_1 < triangle_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{circle_1}" на "{quadrat_1}" соответственно: {circle_1 // quadrat_1}, {circle_1 % quadrat_1}\n')

    print(circle_1, ', Длина объекта: ', len(circle_1), ', Приведение объекта к типу float: ', float(circle_1), ' и к типу int: ', int(circle_1))
    print(f'Результат сложения двух окружностей circle_1: {circle_1 + circle_1}')
    print(f'Результат сравнения на равенство двух окружностей circle_1: {circle_1 == circle_1}, и на знак меньше: {circle_1 < circle_1}')
    print(f'Результат целочисленного деления и остатка от деления объекта "{triangle_1}" на "{quadrat_1}" соответственно: {triangle_1 // quadrat_1}, {triangle_1 % quadrat_1}\n')

