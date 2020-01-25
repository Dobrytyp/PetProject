def is_even(data):
    return data % 2 == 0

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_name_with_titles(self, title):
        return f'{title} {self.name} {self.surname}'

import os

def remove_file(name):
    if os.path.isfile(name):
        os.remove(name)


