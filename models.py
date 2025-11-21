class Student:
    def __init__(self, imie, nazwisko, adres, nr_indeksu, pesel, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.nr_indeksu = nr_indeksu
        self.pesel = pesel
        self. plec = plec

    def __str__(self):
        return f"Student {self.imie} {self.nazwisko} mieszka na ulicy {self.adres}. Jego numer indekstu to {self.nr_indeksu}. Pesel: {self.pesel}. Płeć: {self.plec}"