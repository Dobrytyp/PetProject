from Funkcje_i_klasy_refaktoring import petla, logon, set_password, confirm_password, menu
import Opisy


imie_nazwisko = ''
while imie_nazwisko == '':
    imie_nazwisko = input(Opisy.name_surname_text)          # user data


password = input(Opisy.logon_text)                          # password input


petla(password)                                             # set correct password
total_counter = petla(password)                             # check password control sum


set_password(password, total_counter)                       # checksum password control


logon_ask = ''
logon(logon_ask)                                            # asking about entrance


confirm_password(password)                                  # Confirm your password


menu("")                                                    # Main Menu
