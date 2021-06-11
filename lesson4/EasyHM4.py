# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    miles = 1.609 * km
    print(miles)
convert(12)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):

    a = str(number).split(".") # разделяем вещественное число до знака и
    new_a = list(a[1])
    if int(new_a[ndigits]) >= ndigits:
        new_a[ndigits - 1] = int(new_a[ndigits - 1]) + 1
        new_a[ndigits] = str(new_a[ndigits])
        new_a[ndigits - 1] = str(new_a[ndigits - 1])
        new_a = "".join(new_a)
    new_a = new_a[0:ndigits]
    a[1] = new_a
    a = ".".join(a)
    a = float(a)
    return a


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return False
    else:
        a = str(ticket_number)
        b = str(a[0:3])
        c = str(a[3:6])
        b = list(b)
        c = list(c)
        b = [int(x) for x in b]
        c = [int(x) for x in c]
        b = sum(b)
        c = sum(c)
        if b == c:
            return True
        else:
            return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))