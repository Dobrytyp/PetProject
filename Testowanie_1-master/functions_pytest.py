def is_odd(number):
    return number % 2


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return


class Dog(Animal):
    def speak(self):
        return "Hau"


class Cat(Animal):
    def speak(self):
        return "Miau"


# =================================

### Zadanie 6.
# Funkcja `is_correct_website` powinna wykonac request do żądanego adresu www.
# Sprawdź status code i jeśli wynosi on 2xx lub 3xx zwróć True, dla pozostałych przypadków zwróć False.
# Napisz test który będzie mockował metodę `get` z biblioteki `requests` i
#  sprawdzisz jaki adres został przekazany do requestu oraz zamockujesz poprawne jak i nie poprawne status code.

import requests
status_code

def is_correct_website(url):
    req = requests.get(url)
    return 200 <= req.status_code < 400