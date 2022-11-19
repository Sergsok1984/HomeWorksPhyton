lst_contact = []


def generate_phonebook(n):
    global lst_contact
    for i in range(1, n + 1):
        id = str(i)
        first_name = input(f"Введите имя {id}-го контакта: ")
        second_name = input(f"Введите фамилию {id}-го контакта: ")
        birth_date = input(f"Введите год рождения {id}-го контакта: ")
        work_place = input(f"Введите место работы {id}-го контакта: ")
        phone_number = input(f"Введите номер телефона {id}-го контакта: ")
        lst_contact.append(id + ' ' + first_name + ' ' + second_name +
                           ' ' + birth_date + ' ' + work_place + ' ' + phone_number)
    return lst_contact
