import pandas as pd
from pandas import DataFrame
from logger import LOG
import view

global df
df = pd.read_csv('Seminar8/data_base.csv', encoding='utf-8')


@LOG
def loading_date():
    '''Загружена база данных сотрудников'''
    print(df)
    return


@LOG
def add_date():
    '''Добавлены данные сотрудника'''
    global df
    x1 = input('ID: ')
    x2 = input('Фамилия: ')
    x3 = input('Имя: ')
    x4 = input('Отчество: ')
    x5 = input('Дата рождения: ')
    x6 = input('Должность: ')
    new_row = {'ID': x1, 'Фамилия': x2,
               'Имя': x3, 'Отчество': x4, 'Дата рождения': x5, 'Должность': x6}
    df = df.append(new_row, ignore_index=True)
    print(df)
    return


@LOG
def delete_date():
    '''Удалены данные сотрудника'''
    global df
    x = int(input('Введите ID сотрудника, данные которого нужно удалить: '))
    df = df.loc[df['ID'] != x]
    print(df)
    return


@LOG
def edit_date():
    '''Изменены данные сотрудника'''
    global df
    global id
    id = int(input('Введите ID сотрудника: '))     
    while True:
        button = view.menu_edit()        
        if button == 1:            
            y = (input('Введите фамилию сотрудника: '))
            df.loc[df['ID'] == id, 'Фамилия'] = y
        elif button == 2:
            y = (input('Введите имя сотрудника: '))
            df.loc[df['ID'] == id, 'Имя'] = y
        elif button == 3:
            y = (input('Введите отчетство сотрудника: '))
            df.loc[df['ID'] == id, 'Отчество'] = y
        elif button == 4:
            y = (input('Введите дату рождения сотрудника: '))
            df.loc[df['ID'] == id, 'Дата рождения'] = y
        elif button == 5:
            y = (input('Введите должность сотрудника: '))
            df.loc[df['ID'] == id, 'Должность'] = y
        elif button == 6:
            print('Выход в предыдущее меню.')
            break
        else:
            print('Повторите ввод.')
        print(df)


@LOG
def save_date():
    '''Сохранены данные в файле 'data_base' '''
    df.to_csv('Seminar8/data_base.csv', index=False)



