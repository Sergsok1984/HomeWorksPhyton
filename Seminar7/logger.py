from datetime import datetime as dt

def generate_logger(data):
    time = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ('log.json', 'a', encoding="utf-8") as file:
        file.write(f'\n{time}; создан справочник; {data}')

def output_logger():
    time = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ('log.json', 'a', encoding="utf-8") as file:
        file.write(f'\n{time}; справочник выведен на экран')

def save_logger():
    time = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ('log.json', 'a', encoding="utf-8") as file:
        file.write(f'\n{time}; справочник сохранен в файл phonebook.csv')

def load_logger():
    time = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ('log.json', 'a', encoding="utf-8") as file:
        file.write(f'\n{time}; справочник загружен из файла phonebook.csv')