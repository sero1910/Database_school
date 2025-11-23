# main.py
import sys
from models import Student
from database import DatabaseManager
import validators

def wyswietl_menu():
    print("\n=== AKADEMICKA BAZA DANYCH ===")
    print("1. Dodaj studenta")
    print("2. Wyświetl wszystkich studentów")
    print("3. Wyszukaj studenta")
    print("4. Usuń studenta")
    print("0. Wyjście")
    print("==============================")

def pobierz_dane_studenta():
    """Pomocnicza funkcja do interakcji z użytkownikiem przy dodawaniu."""
    print("\n--- Dodawanie nowego studenta ---")
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    adres = input("Podaj adres: ")
    nr_indeksu = input("Podaj numer indeksu: ")
    
    while True:
        plec = input("Podaj płeć (K/M: ").upper()
        if plec in ["K", "M"]:
            break
        print("Błędna płeć. Wybierz K lub M")
    
    while True:
        pesel = input("Podaj PESEL: ")
        czy_ok, komunikat = validators.sprawdz_pesel(pesel)
        if czy_ok:
            break
        print(f"Błąd: {komunikat}")

    
    
    return Student(imie, nazwisko, adres, nr_indeksu, pesel, plec)

def main():
    db = DatabaseManager()
    
    while True:
        wyswietl_menu()
        wybor = input("Twój wybór: ")

        if wybor == "1":
            nowy_student = pobierz_dane_studenta()
            sukces, wiadomosc = db.dodaj_studenta(nowy_student)
            print(f"\n>> {wiadomosc}")
        
        elif wybor == "2":
            print("\n--- Lista studentów ---")
            lista = db.pobierz_wszystkich()
            
            if not lista:
                print("Baza jest pusta. Dodaj kogoś!")
            else:
                # Nagłówek tabeli (formatowanie f-stringiem dla równych odstępów)
                print(f"{'Indeks':<10} | {'Imię i Nazwisko':<25} | {'PESEL':<12} | {'Płeć'}")
                print("-" * 60)
                
                for s in lista:
                    print(f"{s.nr_indeksu:<10} | {s.imie + ' ' + s.nazwisko:<25} | {s.pesel:<12} | {s.plec}")
            
            input("\nNaciśnij ENTER, aby wrócić do menu...")
        elif wybor == "3":
            print("\n[INFO] Wyszukiwanie w budowie...")
            
        elif wybor == "4":
            print("\n[INFO] Usuwanie w budowie...")
            
        elif wybor == "0":
            print("Zamykanie programu...")
            sys.exit()
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()