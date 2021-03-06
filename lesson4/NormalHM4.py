import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Возвращает ряд фибоначи от n-элемента до m-элемента включительно
    :param n: Значение с какого порядкового номера элемента начать выводить значение ряда фибоначи
    :param m: Значение с какого порядкого номера элемента закончить выводить ряд фибоначи
    :return: Возвращает список ряда фибоначи от n- элеманта до m- Элемента
    """

    fib1 = 1
    fib2 = 1
    z = 0
    list_fib = [1, 1]
    new_listfib = []
    while m != z:
        z += 1
        fib1, fib2 = fib2, fib1 + fib2
        if z >= n:
            list_fib.append(fib2)
    return list_fib[n-1:m]


print(fibonacci(2, 8))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Возвращает отсортированный список по возрастанию
    :param origin_list: Значение списка который нужно отсортировать
    :return: Возвращает остортированный оригинальный список
    """
    i = 0
    while i < (len(origin_list) - 1):
        j = 0
        while j < (len(origin_list) - 1) - i:
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
            j += 1
        i += 1
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# def new_sort(origin_list):
#     mixed = True
#     iter_num = 1
#     while mixed:
#         mixed = False
#         for i in range(0, len(origin_list)-iter_num):
#             if origin_list[i] > origin_list[i+1]:
#                 origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
#                 mixed = True
#         iter_num += 1
#     print(origin_list)
#


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(my_filter,list):
    """
    Работает не верно и не понятно. Списал фигню хоть она и работает. Фильтер должен возвращать Истиность или ложность
    :param my_filter: Должен возвращать истинность или ложность функции
    :param list:
    :return:
    """
    result = []
    for elem in list:
        if my_filter(elem):
            result.append(elem)
    return result

print(my_filter(lambda x: x % 2 == 0, [0,-2, -5, 10, 15]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogran(x1,x2,x3,x4,y1,y2,y3,y4):
    """
    Возвращает True если точки могут быть вершинам параллеограмма
    :param x1: Значение первой точки по оси абсцисс
    :param x2: Значение второй точки по оси абсцисс
    :param x3: Значение третьей точки по оси абсцисс
    :param x4: Значение четвертой точки по оси абсцисс
    :param y1: Значение первой точки по оси ординат
    :param y2: Значение второй точки по оси ординат
    :param y3: Значение третьей точки по оси ординат
    :param y4: Значение четвертой точки по оси ординат
    :return: Возвращает Булевое значение
    """
    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    cd = math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
    da = math.sqrt((x4 - x1)**2 + (y4 - y1)**2)

    bd = math.sqrt((x2 - x2)**2 + (y2 - y2)**2)
    ac = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    if (ab == cd and bc == da) or (ab == cd and bd == ac):
        return True
    else:
        return False
print(parallelogran(1,5,5,1,1,1,8,8))

