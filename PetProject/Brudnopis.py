#
#
# # ZAPISYWANIE DO PLIKU
#
# # f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.py', "a")
# # f.write(F"User: {imie_nazwisko}")
# # f.write("\n")
# # f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.txt', "a")
# # f.write("User: ")
# # f.write(imie_nazwisko)
# # f.write("\n")
# # f.close()
#
# #---------------------------------------
#
import sys
def netto_brutto(kwota):
    wynagrodzenie = kwota * 140.26 / 100
    return print("Twoja kwota brutto to:", round(wynagrodzenie, 2), "\n")


def brutto_netto(kwota):
    wynagrodzenie = kwota * 71.3 / 100
    return print("Twoja kwota netto to:", round(wynagrodzenie, 2), "\n")


def kalkulator_oprocentowania(stan_p, procent, okres, pytanie):
    miesiąc = okres * 12
    procent_m = procent / 12

    dzień = okres * 365
    procent_d = procent / 365
    if pytanie == "m":
        wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "r":
        wynik = stan_p * ((1 + (procent / 100)) ** okres)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "d":
        wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")


def petla(password):
    totatlcounter = ""
    lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
    upper = lower.upper()
    digits = "01234567890"
    specials = "!@$%^&*"
    for i in password:
        if i in lower:
            totatlcounter += "l"
        elif i in upper:
            totatlcounter += "u"
        elif i in digits:
            totatlcounter += "d"
        elif i in specials:
            totatlcounter += "s"
    return totatlcounter


class Konto:
    def __init__(self, imie_nazwisko, stan, status):
        self.imie_nazwisko = imie_nazwisko
        self.stan = stan
        self.status = status

    def description(self):
        return f"Witaj {self.imie_nazwisko}. Twoje konto jest {self.status} znajduje się na nim {self.stan} złotych"

    def stan_konta(self):
        return self.stan

    def wplyw(self, wplyw):
        self.stan += wplyw

    def wyplyw(self, wyplyw):
        self.stan -= wyplyw

    def zamknij_konto(self, status):
        self.status = status
        return self.status == "Zamkniętę"


    def stats(self):
        return self.imie_nazwisko, self.stan, self.status

class Lokata:
    def __init__(self, imie_nazwisko, stan, status, okres, procent):
        self.imie_nazwisko = imie_nazwisko
        self.stan = stan
        self.status = status
        self.okres = okres
        self.procent = procent

    def description(self):
        return f"Witaj {self.imie_nazwisko}. Twoja lokata jest {self.status} znajduje się na niej {self.stan} złotych \n Będzie trwała {self.okres} miesiąc. \nOprocentowanie wynosi {self.procent}%\n"

    def open_depo(self, stan, okres, procent):
        self.stan = stan
        self.okres = okres
        self.procent = procent

imie_nazwisko = input("Podaj imię i nazwisko\n")

password = input("Witamy w systemie bankowości elektronicznej.\n \nWpisz nowe hasło. Hasło musi mieć od 6 do 12 "
                 "znaków. \nHasło musi zawierać przynajmniej jedną wielką, jedną mała litere, cyfrę i znak "
                 "specjalny\n")
petla(password)
totatlcounter = petla(password)


quit1 = True

while quit1:
    while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(
            password) > 12 or len(password) < 6:
        totatlcounter = ""
        print("Twoje hasło nie spełnia wymagań\n")
        password = input("Wpisz jeszcze raz hasło\n")
        petla(password)
        totatlcounter = petla(password)
    print("Hasło zostało zmienione\n")

    ask1 = ''
    quitprogram = False

    while ask1 != "t" or ask1 != "n":
        ask1 = input("czy chcesz się teraz zalogowaćC? \nTak(t),Nie (n)?\n")
        if ask1 == "t" or ask1 == "n":
            break
    if ask1 == "n":
        print("Dziękujemy za skorzystanie z naszego systemu logowania\n")
        sys.exit(0)
    elif ask1 == "t":
        while True:
            ownerpassword = input("podaj swoje hasło\nWyjdź (e)\n")
            if ownerpassword == "e":
                sys.exit()
            elif ownerpassword != password:
                print("Podałeś błedne hasło")
            else:
                print("Witamy w systemie bankowosci elektronicznej\n")
                break

    if quitprogram:
        sys.exit()

    program = ''
    # Menu główne
    its_open = False
    while program != "k" or program != "e" or program != "b" or program != "r" or program != "o" or program != "r" or program != "s" or program != "d":
        program = input(
            "MENU GŁÓWNE\nZ jakiej funkcji chcesz skorzystać?\nKalkulator oprocentowania: (k)\n"
            "Kalkulator Brutto - Netto (""b)\nOferta kont (r)\nWyjście z systemu bankowości: (e)"
            "\nOperacje na rachunku: (o)\nStan rachunku (s)\nZałóż Depozyt (d)\n")
        if program == "b":  # Kalkulator brutto netto
            podaj = ''
            while podaj != "b" or podaj != "n" or podaj != "e" or podaj != "r":
                podaj = input(
                    "KALKULATOR BRUTTO-NETTO\nCo chcesz obliczyć?\nBrutto (b)\nnetto (n)\nPowrót do menu (r)\n"
                    "Zakończ program (e)\n")
                if podaj == "r":
                    break
                kwota = float(input("Podaj wysokść wynagrrodzenia\n"))
                if podaj == "b":
                    netto_brutto(kwota)
                elif podaj == "n":
                    brutto_netto(kwota)
                elif podaj == "e":
                    print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
                    sys.exit(0)

        elif program == "k":  # Kalkulator oprocentowania
            print("KALKULATOR OPROCENTOWANIA")
            stan_p = float(input("podaj stan poczatkowy konta\n"))
            procent = float(input("podaj oprocentowanie\n"))
            okres = float(input("ile lat będziez trzymał środki\n"))
            pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
            pytanie = pytanie.lower()
            while not pytanie in ["m", "d", "r"]:
                print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
                pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
            kalkulator_oprocentowania(stan_p, procent, okres, pytanie)

        elif program == "r":  # ofeta kont
            typ_konta = ''
            print("Zapraszamy do skoszystania z baszej bogatej oferty.\nDzięki dostoswanej do każdego oferty, "
                  "napewno znajdziesz coś dla siebie.\n")
            while typ_konta != 'k' or typ_konta != 'e' or typ_konta != 'w' or typ_konta != 'r':
                podaj = input("Jaki typ konta chcesz otworzyć?\n Rachunek Bierzący (k)\n Konto oszczędnościowe "
                              "(e)\n Konto Walutowe (w)\n Powrót do menu (r)\n\n")
                if podaj == "k":
                    user = Konto(imie_nazwisko, 0, "otwarte")
                    its_open = True
                    print(user.description())
                    break
                elif podaj == "r":
                    break
        elif program == "o":  # Operacje na rachunku
            operacje_na_rachunku = ''

            while operacje_na_rachunku != "+" or operacje_na_rachunku != "-" or operacje_na_rachunku != "r":
                operacje_na_rachunku = input(
                    "Jaką operację chcesz wykonać?\nWpłata (+)\nWypłata (-)\nPowrót do menu głównego (r)\n")
                if not its_open:
                    print("Najpierw musisz mieć otwarte konto")
                    break
                elif operacje_na_rachunku == "+":
                    add_money = float(input("Jaką kwotę chcesz wpłacić na konto?\n"))
                    user.wplyw(add_money)
                    print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n")
                    break
                elif operacje_na_rachunku == "-":
                    take_money = float(input("Jaką kwotę chcesz wypłacić z konta?\n"))
                    if user.stan < take_money:
                        print("Za mało dostępnych środków na rachunku\n")
                        break
                    else:
                        user.wyplyw(take_money)
                        print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n\n")
                elif operacje_na_rachunku == "r":
                    break

        elif program == "s":    # Stan rachunku
            if not its_open:
                print("Najpierw musisz mieć towarte konto\n")
            else:
                print(user.stan_konta())

        elif program == "d":        # załóż lokatę
            if not its_open:
                print("Najpierw musisz mieć towarte konto\n")
            else:
                typ_depo = ''
                print("Zapraszamy do skoszystania z baszej bogatej oferty.\nDzięki dostoswanej do każdego oferty, "
                      "napewno znajdziesz coś dla siebie.\n")
                kwota_lokaty = float(input("Ile chcesz wpłacić na lokatę?\n"))
                if kwota_lokaty > user.stan_konta():
                    print("Masz za mało środków\n")   # <----- TU wywala do poziomu logowania

                else:
                    add_money = ''
                    while add_money != "m" or typ_depo != "t" or typ_depo != "s" or typ_depo != "r" or typ_depo != "e":
                        add_money = input("Na jaki okres chcesz otowrzyć lokatę? \nJedno Miesięczna (m) \nTrzy miesięczna (t) \nSześciomiesięczną (s) \nRoczną (r) \nPowrót do menu (e)\n")
                        if add_money == "m":
                            user_depo = Lokata(imie_nazwisko, kwota_lokaty, "otwarte", 1, 1.5,)
                            its_open = True
                            print(user_depo.description())
                            user.wyplyw(kwota_lokaty)
                            print(f"Po założeniu lokaty na rachnku zostało ci {user.stan} złotych\n\n")
                            break

        elif program == "e":
            print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
            sys.exit(0)
