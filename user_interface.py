from logg import logging
from work_prog import *


def menu():
    print('Добро пожаловать в квесты!\n'
    'Вы находитесь в меню сотрудников!')
    read_all()
    while True:
        st = input('Выберите опцию\n'
        '1 - Показать всю информацию\n'
        '2 - Найти сотрудника\n'
        '3 - Добавить нового сотрудника\n'
        '4 - Изменить данные сотрудника\n'
        '5 - Удалить данные сотрудника\n'
        '0 - Выход\n')
        match st:
            case '1':
                staff_menu_print()
            case '2':
                find_empl(input('Введите фамилию или имя сотрудника: '), read_all())
            case '3':
                add_empl()
            case '4':
                staff_menu_print()
                id_change = input(f"Введите id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case '5':
                del_empl(input('Введите фамилию или имя сотрудника: '))
            case '0':
                logging.info('Stop program.\n')
                print('До свидания!') 
                break
            case _:
                print('Ошибка ввода')
                break


        
    