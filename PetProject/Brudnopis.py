from Funkcje import Konto

imie_nazwisko = input("Podaj swoje imię\n")

user = Konto(imie_nazwisko, 0, "otwarte")

# ZAPISYWANIE DO PLIKU
#
# f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.py', "a")
# f.write("User: ")
# f.write(imie_nazwisko)
# f.write("\n")
# f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.txt', "a")
# f.write("User: ")
# f.write(imie_nazwisko)
# f.write("\n")
# f.close()
#
#---------------------------------------

print(user)