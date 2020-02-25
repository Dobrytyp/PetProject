import Opisy
import sys
from Funkcje import netto_brutto, brutto_netto

"""imie_nazwisko, user, its_open are global"""  # imie_naziwsko - Name and surname
                                                # user - name for class account
its_open = False                                # ist_open - checking if tge account is open


def user_name():                                # User Name and surname
    global imie_nazwisko
    imie_nazwisko = ''
    while imie_nazwisko == '':                  # User name cannot be empty
        imie_nazwisko = input(Opisy.name_surname_text)  


def petla(password):                            # password checksum counter
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


def set_password(password, total_counter):          # control password checksum 
    while "l" not in total_counter or "u" not in total_counter or "d" not in total_counter \
            or "s" not in total_counter or len(password) > 12 or len(password) < 6:
        if password == "e":                         # exit
            print(Opisy.exit_text)
            sys.exit(0)
        print(Opisy.bad_type_password)
        password = input(Opisy.ask_password_again_text)
        petla(password)
        total_counter = petla(password)
    print(Opisy.correct_password_text)


def logon(logon_ask):                               # Ask about entrance
    while logon_ask != "t" or logon_ask != "n":
        logon_ask = input(Opisy.confirm_logon_text)
        if logon_ask == "t" or logon_ask == "n":
            if logon_ask == "n":                    # exit
                print(Opisy.exit_text)
                sys.exit(0)
            elif logon_ask == "t":                  # continue
                break


def confirm_password(password):                     # Confirm your password
    while True:
        ownerpassword = input(Opisy.confirm_password)
        if ownerpassword == "e":                    # exit
            print(Opisy.exit_text)
            sys.exit()
        elif ownerpassword != password:             # if password is not correct
            print(Opisy.bad_password)
        else:                                       # ending login process
            print(Opisy.welcome_text)
            break


def menu(menu_input):                               # main menu
    while menu_input != "e" or menu_input != "o" or menu_input != "r" or menu_input != "s" \
            or menu_input != "d" or menu_input != "a":
        menu_input = input(Opisy.menu_input_text)
        if menu_input == "a":                       # add on menu
            add_on_input = ''
            add_on(add_on_input)
        elif menu_input == "e":                     # exit
            print(Opisy.exit_text)
            sys.exit(0)
        elif menu_input == "r":                     # open account
            accounts_input = ''
            open_account(accounts_input)
        elif menu_input == "o":                     # Transaction
            operacje_na_rachunku = ''
            account_transaction(operacje_na_rachunku)
        elif menu_input == "s":                     # account balance
            if not its_open:                            # if account is not open yet
                print("Najpierw musisz mieć towarte konto\n")
            else:
                print("Na twoim rachnku znajduje się: ", user.stan_konta(), "złotych")


def open_account(accounts_input):                   # account menu
    while accounts_input != 'k' or accounts_input != 'e' or accounts_input != 'w' or accounts_input != 'r':
        accounts_input = input(Opisy.open_account_text)
        if accounts_input == "r":                   # return to main menu
            break
        elif accounts_input == "k":                 # open account
            global user
            user = Konto(imie_nazwisko, 0, "otwarte")
            global its_open
            its_open = True
            print(user.description())
            break


def add_on(add_on_input):
    while add_on_input != "b" or add_on_input != "k" or add_on_input != "e" or add_on_input != "r":
        add_on_input = input(Opisy.add_on_text)
        if add_on_input == "b":                     # brutto netto calculator
            ask_brutto_netto = ''
            brutto_netto_calc(ask_brutto_netto)
        elif add_on_input == "e":                   # exit
            print(Opisy.exit_text)
            sys.exit(0)
        elif add_on_input == "r":                   # return to menu
            break
        elif add_on_input == "k":                   # rate interest calculator
            rate_interest_start = 0
            interest_rate(rate_interest_start)


def brutto_netto_calc(ask_brutto_netto):
    while ask_brutto_netto != "b" or ask_brutto_netto != "n" or ask_brutto_netto != "e" or ask_brutto_netto != "r":
        ask_brutto_netto = input(Opisy.brutto_netto_calc_text)
        if ask_brutto_netto == "r":                 # return to menu
            break
        kwota = float(input(Opisy.salary_text))
        elif ask_brutto_netto == "b":               # netto to brutto
            netto_brutto(kwota)
        elif ask_brutto_netto == "n":               # brutto to netto
            brutto_netto(kwota)
        elif ask_brutto_netto == "e":               # exit
            print(Opisy.exit_text)
            sys.exit(0)


def interest_rate(rate_interest_start):             # rate interest calculator
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
    if pytanie == "m":                              # month capitalization
        wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")

    elif pytanie == "r":                            # year capitalization
        wynik = stan_p * ((1 + (procent / 100)) ** okres)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")

    elif pytanie == "d":                            # day capitalization
        wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
        return print(Opisy.how_much_after_text, round(wynik, 2), "\n")


def account_transaction(operacje_na_rachunku):      # Transaction
    while operacje_na_rachunku != "+" or operacje_na_rachunku != "-" or operacje_na_rachunku != "r":
        operacje_na_rachunku = input(Opisy.account_transaction_text)
        if not its_open:                            # if account is not open yet
            print("Najpierw musisz mieć otwarte konto")
            break
        elif operacje_na_rachunku == "+":           # add money
            add_money = float(input(Opisy.add_transaction_text))
            user.wplyw(add_money)
            print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n")
            break
        elif operacje_na_rachunku == "-":           # withdraw money
            take_money = float(input(Opisy.withdraw_transaction_text))
            if user.stan < take_money:              # if there is not enough money on account
                print("Za mało dostępnych środków na rachunku\n")
                break
            else:
                user.wyplyw(take_money)
                print(f"Na twoim koncie po operacji znajduje się {user.stan_konta()}\n\n")
        elif operacje_na_rachunku == "r":
            break


"""Class Acount"""


class Konto:
    def __init__(self, imie_nazwisko, stan, status):
        self.imie_nazwisko = imie_nazwisko
        self.stan = stan
        self.status = status

    def description(self):
        return f"Witaj {self.imie_nazwisko}. Twoje konto jest {self.status} znajduje się na nim {self.stan} złotych"

    def stan_konta(self):                           # account balance
        return self.stan

    def wplyw(self, wplyw):                         # money income
        self.stan += wplyw

    def wyplyw(self, wyplyw):                       # money whitdraw
        self.stan -= wyplyw

    def zamknij_konto(self, status):                # close account
        self.status = status
        return self.status == "Zamkniętę"

    def stats(self):                                # account status
        return self.imie_nazwisko, self.stan, self.status
