import Opisy
import sys

from Funkcje import netto_brutto, brutto_netto


def petla(password):  # password checksum counter
    total_counter = ""
    lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
    upper = lower.upper()
    digits = "01234567890"
    specials = "!@$%^&*"
    for i in password:
        if i in lower:
            total_counter += "l"
        elif i in upper:
            total_counter += "u"
        elif i in digits:
            total_counter += "d"
        elif i in specials:
            total_counter += "s"
    return total_counter


def set_password(password, total_counter):  # checksum password control
    while "l" not in total_counter or "u" not in total_counter or "d" not in total_counter \
            or "s" not in total_counter or len(password) > 12 or len(password) < 6:
        if password == "e":
            print(Opisy.exit_text)
            sys.exit(0)
        print(Opisy.bad_type_password)
        password = input(Opisy.ask_password_again_text)
        petla(password)
        total_counter = petla(password)
    print(Opisy.correct_password_text)


def logon(logon_ask):  # Ask about entrance
    while logon_ask != "t" or logon_ask != "n":
        logon_ask = input(Opisy.confirm_logon_text)
        if logon_ask == "t" or logon_ask == "n":
            if logon_ask == "n":
                print(Opisy.exit_text)
                sys.exit(0)
            elif logon_ask == "t":
                break


def confirm_password(password):  # Confirm your password
    while True:
        ownerpassword = input(Opisy.confirm_password)
        if ownerpassword == "e":
            print(Opisy.exit_text)
            sys.exit()
        elif ownerpassword != password:
            print(Opisy.bad_password)
        else:
            print(Opisy.welcome_text)
            break


def menu(menu_input):
    while menu_input != "e" or menu_input != "o" or menu_input != "r" or menu_input != "s" \
            or menu_input != "d" or menu_input != "a":
        menu_input = input(Opisy.menu_input_text)
        if menu_input == "a":           # add on menu
            add_on_input = ''
            add_on(add_on_input)
        elif menu_input == "e":         # exit
            print(Opisy.exit_text)
            sys.exit(0)
        elif menu_input == "r":         # open account
            accounts_input = ''
            open_account(accounts_input)


def open_account(accounts_input):
    while accounts_input != 'k' or accounts_input != 'e' or accounts_input != 'w' or accounts_input != 'r':
        accounts_input = input("Jaki typ konta chcesz otworzyć?\n Rachunek Bierzący (k)\n Konto oszczędnościowe "
                               "(e)\n Konto Walutowe (w)\n Powrót do menu (r)\n\n")
        if accounts_input == "r":
            break
        # if podaj == "k":
        #     user = Konto(imie_nazwisko, 0, "otwarte")
        #     its_open = True
        #     print(user.description())
        #     break
        # elif podaj == "r":
        #     break


def add_on(add_on_input):
    while add_on_input != "b" or add_on_input != "k" or add_on_input != "e" or add_on_input != "r":
        add_on_input = input(Opisy.add_on_text)
        if add_on_input == "b":  # brutto netto calculator
            ask_brutto_netto = ''
            brutto_netto_calc(ask_brutto_netto)
        elif add_on_input == "e":  # return to menu
            print(Opisy.exit_text)
            sys.exit(0)
        elif add_on_input == "r":
            break
        elif add_on_input == "k":  # exit
            rate_interest_start = 0
            interest_rate(rate_interest_start)


def brutto_netto_calc(ask_brutto_netto):
    while ask_brutto_netto != "b" or ask_brutto_netto != "n" or ask_brutto_netto != "e" or ask_brutto_netto != "r":
        ask_brutto_netto = input(Opisy.brutto_netto_calc_text)
        if ask_brutto_netto == "r":
            break
        kwota = float(input(Opisy.salary_text))
        if ask_brutto_netto == "b":
            netto_brutto(kwota)
        elif ask_brutto_netto == "n":
            brutto_netto(kwota)
        elif ask_brutto_netto == "e":
            print(Opisy.exit_text)
            sys.exit(0)


def interest_rate(rate_interest_start):  # rate interest inputs
    print(Opisy.interest_calc_text)
    stan_p = float(input(Opisy.account_1_text))
    procent = float(input(Opisy.account_2_text))
    okres = float(input(Opisy.account_how_lon_text))
    pytanie = input(Opisy.ask_capitalization_text)
    pytanie = pytanie.lower()
    while not pytanie in ["m", "d", "r"]:
        print(Opisy.choose_how_long_text)
        pytanie = input(Opisy.choose_how_long_text)
    miesiąc = okres * 12
    procent_m = procent / 12

    dzień = okres * 365
    procent_d = procent / 365
    if pytanie == "m":
        wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")

    elif pytanie == "r":
        wynik = stan_p * ((1 + (procent / 100)) ** okres)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")

    elif pytanie == "d":
        wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")
