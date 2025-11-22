import sqlite3
from models import Student

DB_NAME = "uczelnia.db"

class DatabaseManager:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS studenci (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie TEXT NOT NULL,
        nazwisko TEXT NOT NULL,
        adres TEXT , 
        nr_indeksu TEXT UNIQUE NOT NULL,
        pesel TEXT UNIQUE NOT NULL,
        plec TEXT
        );
        """
        with self._connect() as conn:
            conn.execute(query)

    def dodaj_studenta(self, student: Student):
        query = """
        INSERT INTO studenci (imie, nazwisko, adres, nr_indeksu, pesel, plec)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        try:
            with self._connect() as conn:
                conn.execute(query, (
                    student.imie,
                    student.nazwisko,
                    student.adres,
                    student.nr_indeksu,
                    student.pesel,
                    student.plec
                ))
            return True, " Student dodany pomyślnie."
        except sqlite3.IntegrityError:
            return False, " Błąd: Student o takim numerze indeksu lub PESEL już istnieje."
        except Exception as e:
            return False, f"Wystąpił błąd bazy danych : {e}"
        
