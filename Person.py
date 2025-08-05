from Birthday import Birthday

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = None
        self.email_address = None
        self.nickname = None
        self.street_address = None
        self.city = None
        self.state = None
        self.zip = None
        self.phone = None

    def set_birthday(self, month, day):
        self._birthday = Birthday(month, day)

    def set_city(self, city): self.city = city
    def get_first_name(self): return self.first_name
    def get_last_name(self): return self.last_name

    def say_birthday(self):
        return str(self._birthday) if self._birthday else "No birthday set"

    def __str__(self):
        return f"[ {self.first_name} {self.last_name} ]"
