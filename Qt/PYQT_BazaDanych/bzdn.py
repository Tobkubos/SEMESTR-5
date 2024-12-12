import sys
from PyQt6 import QtSql
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout
import sqlite3

# Funkcja do stworzenia tabeli
def create_table():
    # Połączenie z bazą danych SQLite
    conn = sqlite3.connect('example.db')  # Używamy pliku example.db
    cursor = conn.cursor()

    # Tworzenie tabeli, jeśli jeszcze nie istnieje
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabela (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );
    ''')

    # Zatwierdzenie zmian
    conn.commit()

    # Zamknięcie połączenia
    conn.close()

    print("Tabela została utworzona.")

# Tworzymy tabelę przed otwarciem połączenia w PyQt6
create_table()

# Inicjalizacja aplikacji PyQt6
app = QApplication([])

# Utworzenie głównego okna
window = QWidget()
window.setWindowTitle("Task Manager")
window.setGeometry(300, 300, 700, 700)

# Połączenie z bazą danych SQLite za pomocą PyQt6
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("example.db")  # Łączenie z istniejącą bazą danych example.db

if not db.open():
    print("Nie udało się połączyć z bazą danych.")
    sys.exit(1)

# Tworzymy model i ustawiamy tabelę
model = QtSql.QSqlTableModel()
model.setTable("tabela")  # Łączenie z tabelą 'tabela'
model.select()  # Ładujemy dane z tabeli

# Dodawanie rekordu na sztywno ("Adam Kowalski")
def add_record():
    # Wstawiamy dane na sztywno
    first_name = "Adam"
    last_name = "Kowalski"

    # Dodajemy nowy wiersz do modelu
    row = model.rowCount()
    model.insertRow(row)

    # Ustawiamy dane w nowym wierszu
    model.setData(model.index(row, 1), first_name)  # Kolumna 1 (imię)
    model.setData(model.index(row, 2), last_name)   # Kolumna 2 (nazwisko)

    # Zatwierdzamy zmiany do bazy danych
    model.submitAll()

    # Odświeżamy model, aby dane były widoczne w tabeli
    model.select()

# Wywołanie funkcji dodającej rekord
add_record()

# Utworzenie widoku tabeli
table_view = QTableView()
table_view.setModel(model)

# Tworzenie layoutu i dodanie widoku do okna
layout = QVBoxLayout()
layout.addWidget(table_view)

# Ustawienie layoutu w oknie
window.setLayout(layout)

# Wyświetlenie okna
window.show()

# Uruchomienie aplikacji
sys.exit(app.exec())