from logg import logging


def find_entry(data_find, all_data):
    logging.info(f"Search for an entry: {data_find}")
    employee = [" ".join(i.values()) for i in all_data if data_find in i.values()]
    if employee:
        logging.info(f"Search result: {employee}")
        print(*employee, sep="\n", end="\n\n")
        return [n[0] for n in employee]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Сотрудник не найден.\n")
        return 0


def matching_rec(new_entry: dict, all_data):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_data]
    return value not in all_values


def check_new_data(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "фамилия имя должность":
            if answer.isalpha():
                break
        if num == "телефон":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer