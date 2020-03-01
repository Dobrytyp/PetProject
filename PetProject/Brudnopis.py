# #
# #
# # # ZAPISYWANIE DO PLIKU
# #
# # # f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.py', "a")
# # # f.write(F"User: {imie_nazwisko}")
# # # f.write("\n")
# # # f = open('C:\\Users\\Maciek\\Desktop\\Python\\Python Podstawowy\\PetProject\\User_data.txt', "a")
# # # f.write("User: ")
# # # f.write(imie_nazwisko)
# # # f.write("\n")
# # # f.close()
# #
# # #---------------------------------------
# #
# import sys
# from Funkcje import netto_brutto
# from Funkcje import brutto_netto
# from Funkcje import Konto
# from Funkcje import petla
# from Funkcje import kalkulator_oprocentowania
# from Funkcje import Lokata
#
#
# imie_nazwisko = input("Podaj imię i nazwisko\n")
#
# password = input("Witamy w systemie bankowości elektronicznej.\n \nWpisz nowe hasło. Hasło musi mieć od 6 do 12 "
#                  "znaków. \nHasło musi zawierać przynajmniej jedną wielką, jedną mała litere, cyfrę i znak "
#                  "specjalny\n")
# petla(password)
# totatlcounter = petla(password)
#
# quit1 = True
#
# while quit1:
#     while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(
#             password) > 12 or len(password) < 6:
#         totatlcounter = ""
#         print("Twoje hasło nie spełnia wymagań\n")
#         password = input("Wpisz jeszcze raz hasło\n")
#         petla(password)
#         totatlcounter = petla(password)
#     print("Hasło zostało zmienione\n")
#
#     ask1 = ''
#     quitprogram = False
#
#     while ask1 != "t" or ask1 != "n":
#         ask1 = input("czy chcesz się teraz zalogowaćC? \nTak(t),Nie (n)?\n")
#         if ask1 == "t" or ask1 == "n":
#             break
#     if ask1 == "n":
#         print("Dziękujemy za skorzystanie z naszego systemu logowania\n")
#         sys.exit(0)
#     elif ask1 == "t":
#         while True:
#             ownerpassword = input("podaj swoje hasło\nWyjdź (e)\n")
#             if ownerpassword == "e":
#                 sys.exit()
#             elif ownerpassword != password:
#                 print("Podałeś błedne hasło")
#             else:
#                 print("Witamy w systemie bankowosci elektronicznej\n")
#                 break
#
#     if quitprogram:
#         sys.exit()
#
#     program = ''
#     # Menu główne
#     its_open = False
#     while program != "k" or program != "e" or program != "b" or program != "r" or program != "o" or program != "r" or program != "s" or program != "d":
#         program = input(
#             "MENU GŁÓWNE\nZ jakiej funkcji chcesz skorzystać?\nKalkulator oprocentowania: (k)\n"
#             "Kalkulator Brutto - Netto (""b)\nOferta kont (r)\nWyjście z systemu bankowości: (e)"
#             "\nOperacje na rachunku: (o)\nStan rachunku (s)\nZałóż Depozyt (d)\n")
#         if program == "b":  # Kalkulator brutto netto
#             podaj = ''
#             while podaj != "b" or podaj != "n" or podaj != "e" or podaj != "r":
#                 podaj = input(
#                     "KALKULATOR BRUTTO-NETTO\nCo chcesz obliczyć?\nBrutto (b)\nnetto (n)\nPowrót do menu (r)\n"
#                     "Zakończ program (e)\n")
#                 if podaj == "r":
#                     break
#                 kwota = float(input("Podaj wysokść wynagrodzenia\n"))
#                 if podaj == "b":
#                     netto_brutto(kwota)
#                 elif podaj == "n":
#                     brutto_netto(kwota)
#                 elif podaj == "e":
#                     print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
#                     sys.exit(0)
#
#         elif program == "k":  # Kalkulator oprocentowania
#             print("KALKULATOR OPROCENTOWANIA")
#             stan_p = float(input("podaj stan poczatkowy konta\n"))
#             procent = float(input("podaj oprocentowanie\n"))
#             okres = float(input("ile lat będziez trzymał środki\n"))
#             pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
#             pytanie = pytanie.lower()
#             while not pytanie in ["m", "d", "r"]:
#                 print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
#                 pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
#             kalkulator_oprocentowania(stan_p, procent, okres, pytanie)
#
#         elif program == "r":  # ofeta kont
#             typ_konta = ''
#             print("Zapraszamy do skoszystania z baszej bogatej oferty.\nDzięki dostoswanej do każdego oferty, "
#                   "napewno znajdziesz coś dla siebie.\n")
#             while typ_konta != 'k' or typ_konta != 'e' or typ_konta != 'w' or typ_konta != 'r':
#                 podaj = input("Jaki typ konta chcesz otworzyć?\n Rachunek Bierzący (k)\n Konto oszczędnościowe "
#                               "(e)\n Konto Walutowe (w)\n Powrót do menu (r)\n\n")
#                 if podaj == "k":
#                     user = Konto(imie_nazwisko, 0, "otwarte")
#                     its_open = True
#                     print(user.description())
#                     break
#                 elif podaj == "r":
#                     break
#         elif program == "o":  # Operacje na rachunku
#             operacje_na_rachunku = ''
#
#             while operacje_na_rachunku != "+" or operacje_na_rachunku != "-" or operacje_na_rachunku != "r":
#                 operacje_na_rachunku = input(
#                     "Jaką operację chcesz wykonać?\nWpłata (+)\nWypłata (-)\nPowrót do menu głównego (r)\n")
#                 if not its_open:
#                     print("Najpierw musisz mieć otwarte konto")
#                     break
#                 elif operacje_na_rachunku == "+":
#                     add_money = float(input("Jaką kwotę chcesz wpłacić na konto?\n"))
#                     user.wplyw(add_money)
#                     print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n")
#                     break
#                 elif operacje_na_rachunku == "-":
#                     take_money = float(input("Jaką kwotę chcesz wypłacić z konta?\n"))
#                     if user.stan < take_money:
#                         print("Za mało dostępnych środków na rachunku\n")
#                         break
#                     else:
#                         user.wyplyw(take_money)
#                         print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n\n")
#                 elif operacje_na_rachunku == "r":
#                     break
#
#         elif program == "s":  # Stan rachunku
#             if not its_open:
#                 print("Najpierw musisz mieć towarte konto\n")
#             else:
#                 print(user.stan_konta())
#                 print(user_depo.stan_lokaty())
#
#         elif program == "d":  # załóż lokatę
#             if not its_open:
#                 print("Najpierw musisz mieć otwarte konto\n")
#             else:
#                 typ_depo = ''
#                 print("Zapraszamy do skoszystania z baszej bogatej oferty.\nDzięki dostoswanej do każdego oferty, "
#                       "napewno znajdziesz coś dla siebie.\n")
#                 kwota_lokaty = float(input("Ile chcesz wpłacić na lokatę?\n"))
#                 if kwota_lokaty > user.stan_konta():
#                     print("Masz za mało środków\n")  # <----- TU wywala do poziomu logowania
#
#                 else:
#                     add_money = ''
#                     while add_money != "m" or typ_depo != "t" or typ_depo != "s" or typ_depo != "r" or typ_depo != "e":
#                         add_money = input(
#                             "Na jaki okres chcesz otowrzyć lokatę? \nJedno Miesięczna (m) \nTrzy miesięczna (t) \nSześciomiesięczną (s) \nRoczną (r) \nPowrót do menu (e)\n")
#                         if add_money == "m":
#                             user_depo = Lokata(imie_nazwisko, kwota_lokaty, "otwarte", 1, 1.5, )
#                             its_open = True
#                             print(user_depo.description())
#                             user.wyplyw(kwota_lokaty)
#                             print(f"Po założeniu lokaty na rachnku zostało ci {user.stan} złotych\n\n")
#                             break
#
#         elif program == "e":
#             print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
#             sys.exit(0)
