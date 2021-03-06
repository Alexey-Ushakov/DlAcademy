import os
import sys
import shutil

print("sys argv= ", sys.argv)

def print_help():
    print("help -  получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp - создает копию указанного файла")
    print("rm - удаляет указанный файл ")
    print("cd - смена директории на указанную'")
    print("ls - отображение полного пути текущей директории")
    print("dr - удаляет указанную папку")

def make_dir():
    if not dir_name:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def file_copy():
    if not name_file:
        print("Необходимо указать имя файла вторым параметром")
        return
    current_dir = os.getcwd()
    old_file = os.path.join(current_dir, name_file)
    new_file = os.path.join(current_dir, (name_file +'.copy'))
    if not os.path.exists(new_file):
        shutil.copy(old_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')

def del_file():
    if not name_file:
        print("Необходимо указать имя файла вторым параметром")
        return
    current_dir = os.getcwd()
    old_file = os.path.join(current_dir, name_file)
    if os.path.exists(old_file):
        answer = input('Вы уверены что хотите удалить файл? y/n: ')
        if answer == 'y':
            os.remove(old_file)
            print(old_file + ' - удален')
        else:
            return
    else:
        print('Файла не существует')

def change_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.chdir(dir_name)
        print('Успешно перешли в папку: {}'.format(dir_name))
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print('dir_{} - папки не существует'.format(dir_name))

def current_dir():
    print(os.getcwd())

def make_del_dir():
    if not dir_name:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileExistsError:
        print('директория {} не существует'.format(dir_name))


do = {"help": print_help, "mkdir": make_dir, 'cp': file_copy,
      'cd': change_dir, 'rm': del_file, 'ls': current_dir, "dr": make_del_dir}

try:
    name_file = sys.argv[2]
except IndexError:
    name_file = None


try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")