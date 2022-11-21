import view
import model


def run():
    while True:
        button = view.menu()
        if button == 1:
            model.loading_date()
        elif button == 2:
            model.add_date()
        elif button == 3:
            model.delete_date()
        elif button == 4:
            model.edit_date() 
        elif button == 5:            
            model.save_date()
        elif button == 6:
            print('Выход из программы.')
            break
        else:
            print('Повторите ввод.')
