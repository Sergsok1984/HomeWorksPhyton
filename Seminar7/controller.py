import model
import view
import logger


def run():
    pos = True
    while pos:
        pos = view.menu()
        match pos:
            case 1:
                n = view.num_contacts()
                result = model.generate_phonebook(n)
                logger.generate_logger(" ".join(result))
            case 2:
                view.output_phonebook(result)
                logger.output_logger()
            case 3:
                with open('phonebook.csv', 'w', encoding='utf-8') as file:
                    for value in model.lst_contact:
                        file.write(f"{value}\n")
                file.close()
                logger.save_logger()
            case 4:
                with open('phonebook.csv', 'r', encoding='utf-8') as lst_contact:
                    lst_contact = lst_contact.readlines()
                    view.output_phonebook(lst_contact)
                logger.load_logger()
