from models import Student

def wyswietl_menu():
    print("Menu:")
    print("1. Dodaj studenta")
    print("2. Wyświetl wszystkich studentów")
    print("3. Wyszukaj studenta")
    print("4. Usuń studenta")
    print("0. Wyjście")
    print("==========================")

def pobierz_dane_studenta():
     print("\n--- Dodawanie nowego studenta ---")
     imie = input("Podaj imię: ")
     nazwisko = input("Podaj nazwisko: ")
     adres = input("Podaj adres: ")
     nr_indeksu = input("Podaj numer indeksu: ")
     pesel = input("Podaj PESEL: ")
     plec = input("Podaj płeć (M/K): ").upper()

     return Student(imie, nazwisko, adres, nr_indeksu, pesel, plec)





def main():
    

    
        wyswietl_menu()


if __name__ == "__main__":
    main()
