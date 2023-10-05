#:TODO контрольная

# def sCircle ():
#     pi = 3.14
#     r = int(input(f'Введите радиус круга: '))
#     s = pi * r**2
#     print (f'Площадь круга: {s}')
#
# def pCircle ():
#     pi = 3.14
#     r = int(input(f'Введите радиус круга: '))
#     p = 2 * pi * r
#     print (f'Пириметр круга: {p}')
#
#
# def sTrapezoid ():
#     a = int(input(f'Введите сторону трапеции: '))
#     b = int(input(f'Введите сторону трапеции: '))
#     h = int(input(f'Введите высоту трапеции: '))
#     s = ((a + b) * h)/2
#     print (f'Площадь трапеции: {s}')
#
#
# def pTrapezoid ():
#     a = int(input(f'Введите сторону трапеции: '))
#     b = int(input(f'Введите сторону трапеции: '))
#     c = int(input(f'Введите сторону трапеции: '))
#     d = int(input(f'Введите сторону трапеции: '))
#     p = a + b + c + d
#     print (f'Пириметр трапеции: {p}')
#
# def sRectangle ():
#     h = int(input(f'Введите высоту прямоугольника: '))
#     w = int(input(f'Введите ширину прямоугольника: '))
#     s = a * b
#     print (f'Площадь прямоугольника: {s}')
#
# def pRectangle ():
#     h = int(input(f'Введите высоту прямоугольника: '))
#     w = int(input(f'Введите ширину прямоугольника: '))
#     p = a + a + b + b
#     print (f'Площадь прямоугольника: {p}')
#
# def sTriangle ():
#     a = int(input(f'Введите первый катет: '))
#     b = int(input(f'Введите второй катет: '))
#     s = (a * b) / 2
#     print (f'Площадь треугольника: {s}')
#
#
# print ('Площадь или катет какой фигуры вы хотите расчитать')
# print()
# print ('1 - круг')
# print ('2 - трапеция')
# print ('3 - прямоугольник')
# print ('4 - треугольник')
# print()
# user = int(input('Что будем считать? '))
#
# if user == 1:
#     print('Площадь или Периметр')
#     print()
#     print('1 - Площадь')
#     print('2 - Периметр')
#     choice = int(input('Что будем считать? '))
#     if choice == 1: sCircle ()
#     if choice == 2: pCircle ()
#
# elif user == 2:
#     print('Площадь или Периметр')
#     print()
#     print('1 - Площадь')
#     print('2 - Периметр')
#     choice = int(input('Что будем считать? '))
#     if choice == 1: sTrapezoid ()
#     if choice == 2: pTrapezoid ()
#
# elif user == 3:
#     print('Площадь или Периметр')
#     print()
#     print('1 - Площадь')
#     print('2 - Периметр')
#     choice = int(input('Что будем считать? '))
#     if choice == 1: sRectangle ()
#     if choice == 2: pRectangle ()
#
# elif user == 4:
#     print('Выбор без выбора')
#     print()
#     print('1 - Площадь')
#     choice = int(input('Что будем считать? '))
#     if choice == 1: sTriangle ()
#
# else:
#     print ('Вы ввели неверное значение')






#:TODO дополнительное задание

# string = "Трапеция площадь a=11 b=12 h=113"
# count = 0
# if string.find("Трапеция "):
#     count += 1
#     if string.find("площадь "):
#         count += 1
#         if string.find("a=11 "):
#             count += 1
#             if string.find("b=12 "):
#                 count += 1
#                 if string.find("h=113"):
#                     count += 1
#                     if count == 5:
#                         s = ((11+12)*113)/2
#                         print(s)

# print("Есть совпадение 'Трапеция '?", string.find("Трапеция ") != -1)
# print("Есть совпадение 'площадь '?", string.find("площадь ") != -1)
# print("Есть совпадение 'a=11 '?", string.find("a=11 ") != -1)
# print("Есть совпадение 'b=12 '?", string.find("b=12 ") != -1)
# print("Есть совпадение 'h=113'?", string.find("h=113") != -1)

def squarePrym(a,b):
    return a*b
stroke = input('шаблон')
stroke.strip().lower()
if stroke.find('прямоугольник') != -1:
    if stroke.find('площадь') != -1:
        a = int(stroke[stroke.find('a')+2:stroke.find('b')])
        b = int(stroke[stroke.find('b')+2:])
        print(squarePrym(a, b))