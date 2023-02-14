import csv
from csv import writer, DictReader
from os import path
from exceps import *
from logg import logging

def staff_menu_print():
    file = open('staff.csv', 'r')
    for line in file:
        print(line)
    file.close()

last_id = 0
all_data = {}

def read_all():
    global all_data, last_id
    logging.info(f"Show all Show all entries. Database File - staff.csv")
    with open('staff.csv', "r") as file:
        csv_reader = csv.DictReader(file, delimiter = ';')
        all_data = [i for i in csv_reader]
        last_id = int(all_data[-1]["id"])
        return all_data

def find_empl(data_find):
    logging.info(f"Search for an entry: {data_find}")
    t = 0
    with open('staff.csv', 'r') as staff:
        for line in staff:
            if data_find in line:
                logging.info(f"Search result: {line}")
                print (line)
                t += 1
            pass
        if t == 0:
            logging.warning(f"No data found: {data_find}")
            print('Совпадений не найдено')
            return 0

def add_empl():
    global last_id, all_data
    new_list = [0, 0, 0, 0, 0]
    new_list[0] = last_id + 1
    last_id += 1
    new_list[1] = input('Введити фамилию сотрудника: ')
    new_list[2] = input('Введите имя сотрудника: ')
    new_list[3] = input('Введите должность сотрудника: ')
    new_list[4] = input('Введите номер телефона сотрудника: ')
    # if matching_rec(new_list, all_data):
    logging.info(f"Adding a new entry: {new_list}")
    with open('staff.csv', 'a', newline = '') as staff:
        writer_object = writer(staff, delimiter=';')
        writer_object.writerow(new_list)
        staff.close()
        all_data = read_all()
        logging.warning(f"Data added to the notebook: {new_list}")
        print("Сотрудник добавлен")
    # else:
    #     logging.warning(f"The data is already present in the database")
    #     print("Такой сотрудник уже записан")


# def new_data():
#     global last_id
#     new_list = [0, 0, 0, 0, 0]
#     new_list[0] = last_id + 1
#     last_id += 1
#     new_list[1] = input('Введити фамилию сотрудника: ')
#     new_list[2] = input('Введите имя сотрудника: ')
#     new_list[3] = input('Введите должность сотрудника: ')
#     new_list[4] = input('Введите номер телефона сотрудника: ')
#     return(new_list)


def edit_entry(data_change, id_change):
    global all_data
    key, value = data_change

    logging.info(f"Data changes: {data_change}")
    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                logging.info(f"New value: {v[key]}")
                all_data[i] = v

        with open('staff.csv', "w", newline="") as file:
            fieldnames = ["id", "фамилия", "имя", "должность", "телефон"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(all_data)
            logging.info(f"Data changed")
            print("Изменения добавлены\n")
    else:
        logging.warning(f"No data found: {data_change}")
        print("Id не найден\n")

def edit_menu():
    add_dict = {"1": "фамилия", "2": "имя", "3": "должность", "4": "телефон"}
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. фамилия\n"
                       "2. имя\n"
                       "3. должность\n"
                       "4. телефон\n"
                       "5. выход\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "5":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("Повторрите ввод: ")


def del_empl(data_del):
    global all_data

    logging.info(f"Deleting an entry: {data_del}")
    id_cand = find_entry(data_del, all_data)
    if id_cand:
        id_del = input(f"Enter the id: ")
        logging.info(f"Id selected: {id_del}")

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open('staff.csv', "w", newline="",) as file:
                fieldnames = ["id", "фамилия", "имя", "должность", "телефон"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                logging.info(f"Data deleted")
                print("Данные сотрудника удалены\n")
        else:
            logging.warning(f"No data found: {data_del}")
            print("id не найден\n")
    else:
        logging.warning(f"No data found: {data_del}")
    
# def del_empl():
#     staff_menu_print()
#     n = input('Введите id сотрудника: ')
#     while not n.isdigit:
#         print ('Ошибка ввода!')
#         n = input('Введите id сотрудника: ')
#     with open('staff.csv', 'r') as staff:
#         reader = csv.DictReader(staff, delimiter=";")
#         for i in reader:
#             if n in staff['id']:
#                 new_data = [i for i in staff if i['id'] != n]
#                 with open('staff.csv', 'w', newline = '') as file:
#                     writer_object = writer(file, delimiter=';')
#                     writer_object.writerow(new_data)
#                     file.close()
#             else:
#                 print('id не найден')