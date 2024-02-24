main_menu = ["Главное меню",
             "Открыть книгу",
             "Сохранить книгу",
             "Показать контакт",
             "Создать контакт",
             "Найти контакт",
             "Изменить контакт",
             "Удалить контакт",
             "Выход"]

choice_main_menu = f"Выберите пункт меню от ({1}-{len(main_menu) - 1}): "
choice_main_menu_error = f"Нужно ввести число от {1} до {len(main_menu) - 1}!"

phone_book_opened_successful = f"Телефонная книга открыта успешна!"
phone_book_saved_successful = f"Телефонная книга сохранена успешна!"

phone_book_exit_new = f"В телефонной книге изменение 'Создан новый контакт'!"
phone_book_exit_edit = f"В телефонной книге изменение 'Изменен контакт'!"
phone_book_exit_del = f"В телефонной книге изменение 'Удален контакт'!"
phone_book_exit_save = f"Сохранить y/n: "

empty_phone_book_error = "Телефонная книга пуста или не открыта!"

input_new_contact = ['Введите имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комент контакта: ']

no_changes = "Или ENTER, чтобы оставить без изменений"

edit_contact = [f"Введите новое имя ({no_changes}): ",
                f"Введите новый номер ({no_changes}): ",
                f"Введите новый коментарий ({no_changes}): "]

input_search_word = "Введите слово для поиска: "
input_search_word_for_edit = "Введите слово для поиска контакта который хотите изменить: "
input_search_word_for_delete = "Введите слово для поиска контакта который хотите удалить: "
input_id_for_edit = "Введите id контакта который хотите изменить: "
input_id_for_delete = "Введите id контакта который хотите удалить: "


def new_contact_add_successful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'


def find_contact_no_result(word: str) -> str:
    return f"Контакты содержащие '{word}' не найдены!"


def edit_contact_successful(name: str) -> str:
    return f'Контакт "{name}" успешно изменен!'


def delete_contact_successful(name: str) -> str:
    return f'Контакт "{name}" успешно удален!'
