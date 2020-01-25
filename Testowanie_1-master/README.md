# SDA Python Intermediate

## Zadania w czasie zajęć:

## Unittest
### Zadanie 1.
1. Napisz testy do funkcji is_even sprawdzający przypadki pozytywne
2. Napisz testy obsługujące przypadki negatywne (obsługa wyjątków)
3. Napisz logikę funkcji


### Zadanie 2.
Klasa Person posiada atrybut name, surname, age.
Niech ta klasa zawiera metodę `say_name_with_title` gdzie jako parametr przekażesz `title` 
a funkcja zwróci string zbudowany z title i name oraz surname.
1. Napisz klasę testową który w setUp tworzy obiekt typu Person
2. Napisz testy które korzystają z tego samego obiektu klasy i testują jego pojedynczą metode
3. Napisz logikę klasy

### Zadanie 3.
Napisz funkcję `remove_file` która jako parametr przyjmie nazwę pliku do usunięcia.
Napisz test który zamockuje jego usuwanie i sprawdzi tylko czy moduł `os` został wywołany z 
przekazanym parametrem.




## Pytest
### Zadanie 4.
1. Uzywając `mark.parametrize` napisz testy które sprawdzą funkcję `is_odd`.
2. Napisz logikę funkcji

### Zadanie 5.
Klasa Dog oraz Cat dziedziczy po klasie Animal i obie implementują metode `speak`

1. Używając `fixtures` napisz testy który będą sprawdzać poprawność wyniku metody `speak` dla każdego zwierzęcia. 


### Zadanie 6.
Funkcja `is_correct_website` powinna wykonac request do żądanego adresu www. 
Sprawdź status code i jeśli wynosi on 2xx lub 3xx zwróć True, dla pozostałych przypadków zwróć False. 
Napisz test który będzie mockował metodę `get` z biblioteki `requests` i
 sprawdzisz jaki adres został przekazany do requestu oraz zamockujesz poprawne jak i nie poprawne status code.


### Zadanie 7.
Klasa `Wallet` posiada atrybut `balance` oraz dwie metody: `spend_cash` i `add_cash`. 
Domyślnie `balance` wynosi 0 ale jeśli zostanie przekazana inna wartość to weźmie tą wartość przekazaną.
Rzuć wyjątek jeśli przy `spend_cash` brakuje wystarczających środków w portfelu.

1. Utwórz testy sprawdzające poprawne sytauacje (dodawanie do portfela, odejmowanie jeśli stan konta jest na plusie itp.)
2. Utwórz testy sprawdzjące negatywne sytuacje (odejmowanie jeśli stan konta jest poniżej zera)
3. Zrefactoruj testy aby uzyć fixtures.