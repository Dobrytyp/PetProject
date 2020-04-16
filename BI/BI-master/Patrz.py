imie_nazwisko = "Maciej Pińczewski"
kwota_lokaty = 20000

class Lokata:
    def __init__(self, imie_nazwisko, stan, status, okres, procent):
        self.imie_nazwisko = imie_nazwisko
        self.stan = stan
        self.status = status
        self.okres = okres
        self.procent = procent

    def description(self):
        return f"Witaj {self.imie_nazwisko}. Twoja lokata jest {self.status} znajduje się na niej {self.stan} złotych \nBędzie trwała {self.okres} miesiąc. \nOprocentowanie wynosi {self.procent}%\n"

    def open_depo(self, stan, okres, procent):
        self.stan = stan
        self.okres = okres
        self.procent = procent

    def stan_lokaty(self):
        return self.stan



empty_depo_list = ["user_depo1", "user_depo2", "user_depo3", "user_depo4"]
depo_list = []  


empty_depo_list[0] = Lokata(imie_nazwisko, kwota_lokaty, "otwarte", 1, 1.5, )
depo_list.append(empty_depo_list[0])
empty_depo_list.remove(empty_depo_list[0])



empty_depo_list[0] = Lokata(imie_nazwisko, kwota_lokaty, "otwarte", 3, 1.8, )
depo_list.append(empty_depo_list[0])
empty_depo_list.remove(empty_depo_list[0])

for i in depo_list:
    print(i.description())
