class Human:  # классы пишутся с большой буквы
    def __int__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def say(self):
        print(f"Привет меня зовут {self.name} мне {self.age}")

    def working(self):
        print(f"Работаю {self.work}")
