import view
from model import PhoneBook
import text

pb = PhoneBook()


def find_contacts(message):
    search_word = view.input_data(message)
    result = pb.find_contact(search_word)
    view.show_contacts(pb.max_len_contact(), result, text.find_contact_no_result(search_word))
    return True if result else False


def start_app():
    while True:
        user_chois = view.show_main_menu()
        match user_chois:
            case 1:
                pb.open_phone_book()
                view.show_message(text.phone_book_opened_successful)
            case 2:
                pb.save_phone_book()
                view.show_message(text.phone_book_saved_successful)
            case 3:
                view.show_contacts(pb.max_len_contact(), pb.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                pb.add_new_contact(new_contact)
                view.show_message(text.new_contact_add_successful(new_contact[0]))
            case 5:
                find_contacts(text.input_search_word)
            case 6:
                if find_contacts(text.input_search_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = pb.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successful(name))
            case 7:
                if find_contacts(text.input_search_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = pb.delete_contact(u_id)
                    view.show_message(text.delete_contact_successful(name))
            case 8:

                if pb.edit_tru[0] == True:
                    view.show_message(text.phone_book_exit_new)
                if pb.edit_tru[1] == True:
                    view.show_message(text.phone_book_exit_edit)
                if pb.edit_tru[2] == True:
                    view.show_message(text.phone_book_exit_del)

                if any(pb.edit_tru) and view.input_data(text.phone_book_exit_save) == "y":
                    pb.save_phone_book()
                    view.show_message(text.phone_book_saved_successful)
                    break
                else:
                    break
