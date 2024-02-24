import text


def show_main_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print(f"\t{i}. {item}")
        else:
            print(item)
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        else:
            print(text.choice_main_menu_error)

def show_contacts(max_len:dict[int,int,int], phone_book: dict[int, [str]], error_message: str):
    if phone_book:
        print("\n" + "&" * sum(max_len,11))
        print(f'{"id":>3}. {"Имя":<{max_len[0]}} | {"Номер":<{max_len[1]}} | {"Коментарий":<{max_len[2]}}')
        print("_" * sum(max_len,11))
        for u_id, contact in phone_book.items():
            print(f'{u_id:>3}. {contact[0]:<{max_len[0]}} | {contact[1]:<{max_len[1]}} | {contact[2]:<{max_len[2]}}')
        print("&" * sum(max_len,11), "\n")
    else:
        show_message(error_message)


def show_message(message: str):
    print('\n' + "%" * len(message))
    print(message)
    print("%" * len(message) + '\n')


def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input("\n" + message)
    return [input(mes) for mes in message]
