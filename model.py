class PhoneBook:
    def __init__(self, path='phone.txt', separator=";"):
        self.phone_book = {}
        self.path = path
        self.SEPARATOR = separator
        self.edit_tru = [False, False, False]

    def open_phone_book(self):
        with open(self.path, "r", encoding="UTF-8") as file:
            data = file.readlines()

        for u_id, contact in enumerate(data, 1):
            self.phone_book[u_id] = contact.strip().split(self.SEPARATOR)

    def max_len_contact(self) -> dict[int, int, int]:
        max_len_name = 0
        max_len_number = 0
        max_len_comment = 0
        for contact in self.phone_book.values():
            max_len_name = max(max_len_name, len(contact[0]))
            max_len_number = max(max_len_number, len(contact[1]))
            max_len_comment = max(max_len_comment, len(contact[2]))

        return [max_len_name, max_len_number, max_len_comment]

    def save_phone_book(self):
        data = []
        for contact in self.phone_book.values():
            data.append(self.SEPARATOR.join(contact))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding="UTF-8") as file:
            file.write(data)
            self.edit_tru = [False, False, False]

    def _next_id(self):
        if self.phone_book:
            return max(self.phone_book) + 1 if self.phone_book else 1

    def add_new_contact(self, new_contact: list[str]):
        self.phone_book[self._next_id()] = new_contact
        self.edit_tru[0] = True

    def find_contact(self, search_word: str) -> dict[int, list[str]]:
        result = {}
        for u_id, contact in self.phone_book.items():
            if search_word.lower() in " ".join(contact).lower():
                result[u_id] = contact
        return result

    def edit_contact(self, u_id: int, edited_contact: list[str]):
        current_contact = self.phone_book[u_id]
        for i in range(len(current_contact)):
            current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
        self.phone_book[u_id] = current_contact
        self.edit_tru[1] = True
        return current_contact[0]

    def delete_contact(self, u_id: int) -> str:
        self.edit_tru[2] = True
        return self.phone_book.pop(u_id)[0]
