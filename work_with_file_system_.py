
# Реализовать прототип консольной программы - проводника, для работы с файлами. 
# Создать функции создания, удаления, перемещения, копирования(файла, папки) с использованием системы контроля версий git. 
# Зарегистрироваться на Github и выгрузить с помощью git программу в созданный репозиторий. 
# Прикрепить ссылку на репозиторий.

import os
import shutil
from pathlib import Path
import re

# Функция создания папки
def create_dir(root_folder, dir_name):
    if not dir_name:
        dir_name = input('Название папки: ')
    if not os.path.isdir(root_folder + dir_name): # если не создана, то создаем
        os.makedirs(root_folder + dir_name) #  создание папки/подпапок
        print('Папка создана:', root_folder + dir_name)
    else:
        print('Данная папка уже создана:', root_folder + dir_name)

# Функция создания файла
def create_file(root_folder):

    file_name = input('Название файла:')

    # если не создана папка - создаем (в случае, если создавать файл будете в другой папке)
    dir_name = os.path.dirname(file_name)
    if dir_name != '':
        create_dir(root_folder, dir_name)

    if not os.path.isfile(root_folder + file_name): # если не создан, то создаем
        filename = open(root_folder + file_name, 'a')
        filename.write("Test")
        filename.close() 
        print('Файл создан:', root_folder + file_name)
    else:
        print('Данный файл уже создан:', root_folder + file_name)

# Функция перемещения файла/папки
def move_file(root_folder): 
    name = input('Название файла/папки :')
    dst_name = input('В какую папку перемещать? :')

    # если не создана папка - создаем (в случае, если перемещать будем в другую папку)
    print(dst_name)
    dir_name = os.path.dirname(dst_name)
    if dir_name != '':
        create_dir(root_folder, dir_name)

    print(root_folder+name)
    if os.path.isfile(root_folder+name):
        shutil.move(root_folder+name, root_folder+dst_name)
        print('Файл ', root_folder+name, ' перемещен в', root_folder+dst_name)
    elif os.path.isdir(root_folder+name):
        shutil.move(root_folder+name, root_folder+dst_name)
        print('Папка ', root_folder+name, ' перемещена в', root_folder+dst_name)
    else:
        print('Файл/Папка уже ранее был скопирован или уже такой файл существует/либо данные ввели неверно!')  

# Функция копирования файла
def copy_file(root_folder):
    file_name = input('Название файла :')
    dst_name = input('Скопировать файл в :')

    # если не создана папка - создаем (в случае, если копировать будете в другую папку)
    dir_name = os.path.dirname(dst_name)
    if dir_name != '':
        create_dir(root_folder, dir_name)

    print(root_folder+file_name)
    if os.path.isfile(root_folder+file_name):
        shutil.copy2(root_folder+file_name, root_folder+dst_name)
        print('Файл скопирован из ', root_folder+file_name, 'в папку', root_folder+dst_name)
    else:
        print('Файл уже ранее был скопирован или уже такой файл существует/либо данные ввели неверно!')      

# Функция копирования папки
def copy_dir(root_folder):
    dir_name = input('Название папки :')
    dst_name = input('Скопировать папку в :')

    # если не создана папка - создаем (в случае, если копировать будете в другую папку)
    dir_name = os.path.dirname(dst_name)
    if dir_name != '':
        create_dir(root_folder, dir_name)
    
    try:
        if os.path.isdir(root_folder+dir_name):
            shutil.copytree(root_folder+dir_name, root_folder+dst_name)
            print('Папка скопирована из ', root_folder+dir_name, 'в папку', root_folder+dst_name)
        else:
            print('Папка уже ранее была скопирована или уже такая папка существует/либо данные ввели неверно!')  
    except:
        print('Папка уже существует!')
# Функция удаления папки
def delete_dir(root_folder):
    dir_name = input('Название папки: ')
    if os.path.isdir(root_folder+dir_name): # если существует, то удаляем
        try:
            os.rmdir(root_folder+dir_name)
            print('Папка удалена:', root_folder+dir_name)
        except:
            action = input('Папка не пуста! Удалить папку со всем содержимым ("yes"/"no")? :')
            print(action)
            if action == 'yes':
                shutil.rmtree(root_folder+dir_name)
                print('Папка удалена:', root_folder+dir_name)
    else:
        print('Данной папки не существует:', root_folder+dir_name)

# Функция удаления файла
def delete_file(root_folder):
    file_name = input('Название файла :')
    if os.path.isfile(root_folder+file_name): # если существует, то удаляем
        os.remove(root_folder+file_name)
        print('Файл удален:', root_folder+file_name)
    else:
        print('Данного файла не существует:', root_folder+file_name)

def check_all_dir_and_files(main_path):
    list_paths = []
    path = Path(main_path)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for item in path.rglob("*"):
        if (not '.git' in os.path.dirname(item) and 
            not os.path.basename(__file__) in os.path.basename(item) and 
            not '.git' in os.path.basename(item)):
            list_paths.append(str(item))

    main_path = re.sub(r'\\', '/', main_path) + '/'
    for lp in list_paths:
        lp = re.sub(r'\\', '/', lp)
        lp = re.sub(main_path, '', lp)
        print(lp)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return main_path

# Получаем путь корневой папки, где у нас лежит скрипт
main_path = os.getcwd()

while True:

    # Выводим весь список файлов и папок
    print('\nСписок всех файлов и папок в корневой папке: '+main_path)
    root_folder = check_all_dir_and_files(main_path)

    list_actions = {
        '0' : 'Создать папку', 
        '1' : 'Создать файл',
        '2' : 'Переместить папку/файл',
        '3' : 'Копировать папку',
        '4' : 'Копировать файл',
        '5' : 'Удалить папку',
        '6' : 'Удалить файл',
        '7' : 'Выйти из программы',
    }
    print(' -------------------- ')
    for elem in list_actions:
        print(elem,'-', list_actions.get(elem))
    print(' -------------------- ')
    action = input('Что хотите сделать?\nУкажите только номер пункта: ')


    print('\n----', list_actions.get(action), '----\n')
    dir_name = None
    if action == '0':
        # Создание папки
        create_dir(root_folder, dir_name)

    elif action == '1':
        create_file(root_folder)

    elif action == '2':
        move_file(root_folder)

    elif action == '3':
        copy_dir(root_folder)

    elif action == '4':
        copy_file(root_folder)

    elif action == '5':
        delete_dir(root_folder)

    elif action == '6':
        delete_file(root_folder)

    elif action == '7':
        break

print('Программа завершена!')

