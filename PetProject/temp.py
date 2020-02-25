# def petla(password):
#     total_counter = ""
#     lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
#     upper = lower.upper()
#     digits = "01234567890"
#     specials = "!@$%^&*"
#     for i in password:
#         if i in lower:
#             total_counter += "l"
#         elif i in upper:
#             total_counter += "u"
#         elif i in digits:
#             total_counter += "d"
#         elif i in specials:
#             total_counter += "s"
#     return total_counter
#
#
# def set_password(password, total_counter):
#     if password == "e":
#         print(exit_text)
#         break
#     while "l" not in total_counter or "u" not in total_counter or "d" not in total_counter or "s" not in total_counter \
#             or len(password) > 12 or len(password) < 6:
#         print(bad_type_password)
#         password = input(ask_password_again_text)
#         petla(password)
#         total_counter = petla(password)
#     # print(correct_password_text)
#     # return password
#
# def logon(logon_ask):                       # Ask about entrance
#     while logon_ask != "t" or logon_ask != "n":
#         logon_ask = input("czy chcesz się teraz zalogowaćC? \nTak(t),Nie (n)?\n")
#         if logon_ask == "t" or logon_ask == "n":
#             if logon_ask == "n":
#                 print(exit_text)
#                 break
#             elif logon_ask == "t":
#                 break
#
# name_surname_text = "Podaj imię i nazwisko\n"
# logon_text = "Witamy w systemie bankowości elektronicznej.\n \nWpisz nowe hasło. Hasło musi mieć od 6 do 12 znaków. " \
#              "\nHasło musi zawierać przynajmniej jedną wielką, jedną mała litere, cyfrę i znak specjalny\n" \
#              "Wyjście z systemu - (e)\n"
# confirm_logon_text = "czy chcesz się teraz zalogowaćC? \nTak(t),Nie (n)?\n"
# welcome_text = "Witamy w systemie bankowosci elektronicznej\n"
# exit_text = "Dziękujemy za skorzystanie z naszego systemu bankowości\n"
#
# bad_type_password = "Twoje hasło nie spełnia wymagań\n"
# ask_password_again_text = "Wpisz jeszcze raz hasło\n"
# correct_password_text = "Hasło zostało zmienione\n"
# confirm_password = "Podaj swoje hasło\nWyjdź (e)\n"
# bad_password = "Podałeś błedne hasło"
#
# imie_nazwisko = input(name_surname_text)      # user data
# password = input(logon_text)                  # password data
#
#
# petla(password)                                     # set correct password
# total_counter = petla(password)
#
#
# set_password(password, total_counter)
#
#
# logon_ask = ''
# logon(logon_ask)                            # asking about entrance
#
# while True:
#     ownerpassword = input(confirm_password)
#     if ownerpassword == "e":
#         print(exit_text)
#         break
#     elif ownerpassword != password:
#         print("Podałeś błedne hasło")
#     else:
#         print("Witamy w systemie bankowosci elektronicznej\n")
#         break
#
# print("siema")


a = "In the hole in the ground there lived a hobbit"
counter = -1
h_list = []

for i in a:
    counter += 1
    if i == "h":
        h_list.append(counter)

first = h_list[0]
last = h_list[-1]


# print(h_list)

start = a[:first+1]
middle = a[first+1:last-1]
ends = a[last:]

# print(start)
# print(middle)
# print(ends)

middle2 = middle.replace("h", "H")


# print(middle2)
print(start,middle2,ends)
