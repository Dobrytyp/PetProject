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


# ====================== Klasa Lokata =================================

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
