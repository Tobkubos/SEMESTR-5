import sys
from PyQt6 import QtSql
from PyQt6.QtSql import QSqlQuery, QSqlDatabase 
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QHBoxLayout

def add_person(name, surname):
    query = QSqlQuery()
    query.prepare("INSERT INTO osoby (Name, Surname) VALUES (?, ?)")
    query.addBindValue(name)
    query.addBindValue(surname)
    if not query.exec():
        print("Nie udalo sie dodac osoby:", query.lastError().text())
        
def add_book(title, author):
    query = QSqlQuery()
    query.prepare("INSERT INTO ksiazki (Title, Author) VALUES (?, ?)")
    query.addBindValue(title)
    query.addBindValue(author)
    if not query.exec():
        print("Nie udalo sie dodac ksiazki:", query.lastError().text())

def add_wypozycznia(osID, ksiazkaID):
    query = QSqlQuery()
    query.prepare("INSERT INTO wypozyczenia (PersonID, BookID) VALUES (?, ?)")
    query.addBindValue(osID)
    query.addBindValue(ksiazkaID)
    if not query.exec():
        print("Nie udalo sie dodac ksiazki:", query.lastError().text())


def create_table_osoby():
    query = QSqlQuery()
    
    query.exec("DROP TABLE osoby")
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS osoby (
        PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255),
        Surname VARCHAR(255)
    )
    """
    if not query.exec(create_table_sql):
        print("Nie udalo sie stworzyc tabeli:", query.lastError().text())
    
def create_table_ksiazki():
    query = QSqlQuery()
    
    query.exec("DROP TABLE ksiazki")
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ksiazki (
        BookID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title VARCHAR(255),
        Author VARCHAR(255)
    )
    """
    if not query.exec(create_table_sql):
        print("Nie udalo sie stworzyc tabeli:", query.lastError().text())

def create_table_wypozyczenia():
    query = QSqlQuery()
    
    query.exec("DROP TABLE IF EXISTS wypozyczenia")
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS wypozyczenia (
        LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
        PersonID INTEGER,
        BookID INTEGER,
        FOREIGN KEY (PersonID) REFERENCES osoby(PersonID),
        FOREIGN KEY (BookID) REFERENCES ksiazki(BookID)
    )
    """
    if not query.exec(create_table_sql):
        print("Nie udało się stworzyć tabeli wypożyczeń:", query.lastError().text())
        
app = QApplication([])

window = QWidget()
window.setWindowTitle("Book Borrow")
window.setGeometry(300, 300, 700, 700)

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("book_borrow.db")

if not db.open():
    print("Polaczenie nie udane:", db.lastError().text())
    sys.exit(1)

create_table_osoby()
create_table_ksiazki()
create_table_wypozyczenia()
add_person("John", "Doe")
add_person("Jane", "Smith")

add_book("krzyzacy", "sienkiewicz")
add_book("bandyta", "remi mroz")

add_wypozycznia(1,1)
add_wypozycznia(2,1)


#
model = QtSql.QSqlTableModel()
model.setTable("osoby")
model.select()

view = QTableView()
view.setModel(model)
#

#
model2 = QtSql.QSqlTableModel()
model2.setTable("ksiazki")
model2.select()

view2 = QTableView()
view2.setModel(model2)
#

#
model3 = QtSql.QSqlQueryModel()
query = """
    SELECT o.Name, o.Surname, k.Title, k.Author
    FROM wypozyczenia w
    JOIN osoby o ON w.PersonID = o.PersonID
    JOIN ksiazki k ON w.BookID = k.BookID
"""
model3.setQuery(query)

view3 = QTableView()
view3.setModel(model3)
view3.show()
#

layout = QHBoxLayout()
layout.addWidget(view)
layout.addWidget(view2)
layout.addWidget(view3)
window.setLayout(layout)

window.show()

sys.exit(app.exec())