# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
# a = input("Введите дроби через пробел: ")
a = 5/6 + 4/7
a = a.split()

a[0] = a[0].split("/")
a[2] = a[2].split("/")
b = ["1"]
if len(a[0]) == 1:
    a[0] = list(a[0])
    a[0] = a[0] + b
if len(a[2]) == 1:
    a[2] = list(a[2])
    a[2] = a[2] + b


if a[1] == "+":
    obch_chislitel = int(a[0][0]) * int(a[2][1]) + int(a[0][1]) * int(a[2][0])
    obch_znam = int(a[0][1]) * int(a[2][1])
    celai = obch_chislitel // obch_znam
    drobnai = abs(obch_chislitel % obch_znam)
elif a[1] == "-":
    obch_chislitel = int(a[0][0]) * int(a[2][1]) - int(a[0][1]) * int(a[2][0])
    obch_znam = int(a[0][1]) * int(a[2][1])
    celai = obch_chislitel // obch_znam
    drobnai = abs(obch_chislitel % obch_znam)
print("{} {}/{}".format(celai,drobnai,obch_znam ))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
path = os.path.join("data", "hours_of.txt")
f = open(path, encoding="UTF-8" )
# with open("data", "hours_of.txt") as read_file:
#     read_file.read()
b = f.readline().split()
dic_work = {}
dic_work["Name"] = [""]
dic_work["Last_name"] = [""]
dic_work["hours_at_work"] = [""]
for b in range(6):
    b = f.readline().split()
    # print(b)
    # print(dic_work)
    dic_work["Name"] += b[0].split()
    dic_work["Last_name"] += b[1].split()
    dic_work["hours_at_work"] += b[2].split()
f.close
print(dic_work["Name"])

path = os.path.join("data", "workers.txt")
f = open(path, encoding="UTF-8" )
b = f.readline().split()
dic_work = {}
dic_work["Name"] = [""]
dic_work["Last_name"] = [""]
dic_work["hours_at_work"] = [""]
for b in range(6):
    b = f.readline().split()
    # print(b)
    # print(dic_work)
    dic_work["Name"] += b[0].split()
    dic_work["Last_name"] += b[1].split()
    dic_work["hours_at_work"] += b[2].split()
f.close



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))