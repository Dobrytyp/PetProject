from Funkcje import Konto

imie_nazwisko = input("Podaj swoje imię\n")

user = Konto(imie_nazwisko, 0, "otwarte")

# ZAPISYWANIE DO PLIKU

# f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.py', "a")
# f.write(F"User: {imie_nazwisko}")
# f.write("\n")
# f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.txt', "a")
# f.write("User: ")
# f.write(imie_nazwisko)
# f.write("\n")
# f.close()

#---------------------------------------

print(user.stan_konta())

print(user.description())

operacje_na_rachunku = ''
while operacje_na_rachunku != "+" or operacje_na_rachunku != "-" or operacje_na_rachunku != "r":
    operacje_na_rachunku = input(
        "Jaką operację chcesz wykonać?\nWpłata (+)\nWypłata (-)\nPowrót do menu głównego (r)\n")
    if operacje_na_rachunku == "+":
        add_money = float(input("Jaką kwotę chcesz wpłacić na konto?\n"))
        user.wplyw(add_money)
        print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}")
        break
    elif operacje_na_rachunku == "-":
        take_money = float(input("Jaką kwotę chcesz wypłacić z konta?\n"))
        if user.stan < take_money:
            print("Za mało dostępnych środków na rachunku")
            break
        else:
            user.wyplyw(take_money)
            print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}")
    elif operacje_na_rachunku == "r":
        break


