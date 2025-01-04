import sys
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery, QSqlDatabase 
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QAbstractItemView, QDialog
import bcrypt
import json


def add_person(name, surname):
    query = QSqlQuery()
    query.prepare("INSERT INTO osoby (Name, Surname) VALUES (?, ?)")
    query.addBindValue(name)
    query.addBindValue(surname)
    if not query.exec():
        infoLabel.setText("Nie udalo sie dodac osoby:", query.lastError().text())
    else:
        infoLabel.setText("DODANO OSOBĘ!")
        
def edit_person(OsID, NewName, NewSurname):
    query = QSqlQuery()
    query.prepare("UPDATE osoby SET name = ?, surname = ? WHERE PersonID = ?")
    query.addBindValue(NewName)
    query.addBindValue(NewSurname)
    query.addBindValue(OsID)
    if not query.exec():
        infoLabel.setText("Nie udalo sie edytowac osoby:", query.lastError().text())
    else:
        infoLabel.setText("edytowano osobę!")
        
def add_book(title, author):
    query = QSqlQuery()
    query.prepare("INSERT INTO ksiazki (Title, Author) VALUES (?, ?)")
    query.addBindValue(title)
    query.addBindValue(author)
    if not query.exec():
        infoLabel.setText("Nie udalo sie dodac ksiazki:", query.lastError().text())
    else:
        infoLabel.setText("DODANO KSIĄŻKĘ!")

def edit_book(BookID, NewTitle, NewAuthor):
    query = QSqlQuery()
    query.prepare("UPDATE ksiazki SET title = ?, author = ? WHERE BookID = ?")
    query.addBindValue(NewTitle)
    query.addBindValue(NewAuthor)
    query.addBindValue(BookID)
    if not query.exec():
        infoLabel.setText("Nie udalo sie edytowac ksiazki:", query.lastError().text())
    else:
        infoLabel.setText("edytowano książkę!")

def add_wypozycznia(osID, ksiazkaID):
    query = QSqlQuery()
    query.prepare("INSERT INTO wypozyczenia (PersonID, BookID) VALUES (?, ?)")
    query.addBindValue(osID)
    query.addBindValue(ksiazkaID)
    if not query.exec():
        infoLabel.setText("Nie udalo sie dodac wypozyczneia:", query.lastError().text())
    else:
        infoLabel.setText("DODANO WYPOŻYCZENIE!")

def del_wypozycznia(wypID):
    query = QSqlQuery()
    query.prepare("DELETE FROM wypozyczenia WHERE LoanID = ?")
    query.addBindValue(wypID)
    if not query.exec():
        infoLabel.setText("Nie udalo sie usunac wypozyczenia:", query.lastError().text())
    else:
        infoLabel.setText("USUNUĘTO WYPOŻYCZENIE!")

def add_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query = QSqlQuery()
    query.prepare("INSERT INTO users (Username, Password) VALUES (?, ?)")
    query.addBindValue(username)
    query.addBindValue(hashed_password.decode('utf-8'))
    if not query.exec():
        infoLabel.setText("Nie udało się dodać użytkownika:", query.lastError().text())
    else:
        infoLabel.setText("")

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
        infoLabel.setText("Nie udalo sie stworzyc tabeli:", query.lastError().text())
    
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
        infoLabel.setText("Nie udalo sie stworzyc tabeli:", query.lastError().text())

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
        infoLabel.setText("Nie udało się stworzyć tabeli wypożyczeń:", query.lastError().text())

def create_table_users():
    query = QSqlQuery()

    query.exec("DROP TABLE IF EXISTS users")
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username VARCHAR(255) UNIQUE,
        Password VARCHAR(255)
    )
    """
    if not query.exec(create_table_sql):
        infoLabel.setText("Nie udało się stworzyć tabeli użytkowników:", query.lastError().text())

def login_popup():
    dialog = QDialog()
    dialog.setWindowTitle("Logowanie")
    dialog.setGeometry(400, 300, 300, 150)

    layout = QVBoxLayout()

    username_label = QLabel("Nazwa użytkownika")
    username_input = QLineEdit()
    password_label = QLabel("Hasło")
    password_input = QLineEdit()
    password_input.setEchoMode(QLineEdit.EchoMode.Password)
    login_button = QPushButton("Zaloguj")
    info_label = QLabel("")
    tip_label = QLabel("Psssst... Spróbuj: \n login: admin \n hasło: admin \n :)")

    layout.addWidget(username_label)
    layout.addWidget(username_input)
    layout.addWidget(password_label)
    layout.addWidget(password_input)
    layout.addWidget(login_button)
    layout.addWidget(info_label)
    layout.addWidget(tip_label)

    dialog.setLayout(layout)

    def authenticate_user(username, password):
        query = QSqlQuery()
        query.prepare("SELECT Password FROM users WHERE Username = ?")
        query.addBindValue(username)
        if query.exec() and query.next():
            stored_password = query.value(0)
            return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
        return False

    def handle_login():
        username = username_input.text().strip()
        password = password_input.text().strip()
        if username and password:
            if authenticate_user(username, password):
                dialog.accept()
            else:
                info_label.setText("Nie udało się zalogować!")
        else:
            info_label.setText("Wprowadź dane logowania!")

    login_button.clicked.connect(handle_login)

    if not dialog.exec():
        sys.exit(0) 

app = QApplication([])

window = QWidget()
window.setWindowTitle("Book Borrow")
window.setGeometry(300, 300, 700, 700)

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("book_borrow.db")

if not db.open():
    sys.exit(1)
infoLabel = QLabel()
create_table_osoby()
create_table_ksiazki()
create_table_wypozyczenia()
create_table_users()

#add_person("Jacek", "Soplica")
#add_person("Ksiadz", "Robak")

#add_book("Lalka", "Prus")
#add_book("Ferdydurke", "Gombrowicz")

#add_wypozycznia(1,1)
#add_wypozycznia(2,1)

add_user("admin", "admin")

login_popup()

#osoby
model = QtSql.QSqlTableModel()
model.setTable("osoby")
model.select()

view = QTableView()
view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
view.setModel(model)
#

#ksiazki
model2 = QtSql.QSqlTableModel()
model2.setTable("ksiazki")
model2.select()

view2 = QTableView()
view2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
view2.setModel(model2)
#

#wypozyczenia
model3 = QtSql.QSqlQueryModel()
query3 = """
    SELECT w.LoanID, o.Name, o.Surname, k.Title, k.Author
    FROM wypozyczenia w
    JOIN osoby o ON w.PersonID = o.PersonID
    JOIN ksiazki k ON w.BookID = k.BookID
"""
model3.setQuery(query3)

view3 = QTableView()
view3.setModel(model3)
view3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
view3.show()

#
layout = QHBoxLayout()
layout.addWidget(view)
layout.addWidget(view2)
layout.addWidget(view3)


mainLayout = QVBoxLayout()
mainLayout.addLayout(layout)

Sections = QHBoxLayout()

#region DODAJ OSOBĘ
AddPersonLayout = QVBoxLayout()
imieLabel = QLabel("Imie")
imieLabel.setFixedHeight(30)
imie = QLineEdit()
imie.setFixedHeight(30)
AddPersonLayout.addWidget(imieLabel)
AddPersonLayout.addWidget(imie)

NazwiskoLabel = QLabel("Nazwisko")
NazwiskoLabel.setFixedHeight(30)
nazwisko = QLineEdit()
nazwisko.setFixedHeight(30)
AddPersonLayout.addWidget(NazwiskoLabel)
AddPersonLayout.addWidget(nazwisko)
AddPerson = QPushButton("DODAJ OSOBĘ")
def F_addPerson():
    if imie.text().strip() != "" and nazwisko.text().strip() != "":
        print(imie.text().strip(), nazwisko.text().strip())
        add_person(imie.text().strip(), nazwisko.text().strip())
        model.select()
    else:
        infoLabel.setText("NIE WPROWADZONO DANYCH!")
        
AddPerson.clicked.connect(F_addPerson)
AddPersonLayout.addWidget(AddPerson)

Sections.addLayout(AddPersonLayout,1)
#endregion
#region DODAJ KSIĄŻKĘ
AddBookLayout = QVBoxLayout()
TytulLabel = QLabel("Tytul")
TytulLabel.setFixedHeight(30)
tytul = QLineEdit()
tytul.setFixedHeight(30)
AddBookLayout.addWidget(TytulLabel)
AddBookLayout.addWidget(tytul)

AutorLabel = QLabel("Autor")
AutorLabel.setFixedHeight(30)
autor = QLineEdit()
autor.setFixedHeight(30)
AddBookLayout.addWidget(AutorLabel)
AddBookLayout.addWidget(autor)

AddBook = QPushButton("DODAJ KSIĄŻKĘ")
def F_addBook():
    if tytul.text().strip() != "" and autor.text().strip() != "":
        print(tytul.text().strip(), autor.text().strip())
        add_book(tytul.text().strip(), autor.text().strip())
        model2.select()
    else:
        infoLabel.setText("NIE WPROWADZONO DANYCH!")
        
AddBook.clicked.connect(F_addBook)
AddBookLayout.addWidget(AddBook)

Sections.addLayout(AddBookLayout,1)
#endregion
#region OPCJE - WYPOŻYCZ / USUŃ / POSORTUJ
Options = QVBoxLayout()
wypozycz = QPushButton("wypożycz")

def F_wypozycz():
    indexOsoby = view.selectionModel().currentIndex()
    indexKsiazki = view2.selectionModel().currentIndex()
    if indexOsoby.isValid() and indexKsiazki.isValid():
        personID = model.record(indexOsoby.row()).value("PersonID")
        bookID = model2.record(indexKsiazki.row()).value("BookID")
        
        add_wypozycznia(personID, bookID)
        model3.setQuery(query3)
        
    else:
        infoLabel.setText("NIE ZAZNACZONO OSOBY LUB KSIĄŻKI!")

wypozycz.clicked.connect(F_wypozycz)
wypozycz.setFixedHeight(30)
Options.addWidget(wypozycz)

delWyp = QPushButton("Usuń Wypożyczenie")

def F_delWyp():
    indexWyp = view3.selectionModel().currentIndex()
    if indexWyp.isValid():
        wypID = model3.record(indexWyp.row()).value("LoanID")
        
        del_wypozycznia(wypID)
        model3.setQuery(query3)
        
    else:
        infoLabel.setText("NIE ZAZNACZONO WYPOŻYCZENIA!")

delWyp.clicked.connect(F_delWyp)
delWyp.setFixedHeight(30)
Options.addWidget(delWyp)

sort = QComboBox()
sort.addItem("Sortuj wg Imienia (osoby)")
sort.addItem("Sortuj wg Nazwiska (osoby)")
sort.addItem("Sortuj wg Tytułu (książki)")
sort.addItem("Sortuj wg Autora (książki)")
sort.addItem("Sortuj wg Wypożyczenia (osoby)")
sort.addItem("Sortuj wg Wypożyczenia (książki)")

def F_sort(index):
    if index == 0:  # Sortuj po imieniu
        model.setSort(1, Qt.SortOrder.AscendingOrder)
        model.select()
    elif index == 1:  # Sortuj po nazwisku
        model.setSort(2, Qt.SortOrder.AscendingOrder)
        model.select()
    elif index == 2:  # Sortuj po tytule
        model2.setSort(1, Qt.SortOrder.AscendingOrder) 
        model2.select()
    elif index == 3:  # Sortuj po autorze
        model2.setSort(2, Qt.SortOrder.AscendingOrder) 
        model2.select()
    elif index == 4:  # Sortuj po osobie wypo
        model3.setQuery("""
            SELECT w.LoanID, o.Name, o.Surname, k.Title, k.Author
            FROM wypozyczenia w
            JOIN osoby o ON w.PersonID = o.PersonID
            JOIN ksiazki k ON w.BookID = k.BookID
            ORDER BY o.Name ASC
        """)
    elif index == 5:  # Sortuj po ksiazce wypo
        model3.setQuery("""
            SELECT w.LoanID, o.Name, o.Surname, k.Title, k.Author
            FROM wypozyczenia w
            JOIN osoby o ON w.PersonID = o.PersonID
            JOIN ksiazki k ON w.BookID = k.BookID
            ORDER BY k.Title ASC
        """)

sort.currentIndexChanged.connect(F_sort)
sort.setFixedHeight(30)
Options.addWidget(sort)


s1 = QLineEdit()
s1.setPlaceholderText("Wprowadź nowe dane...")
s2 = QLineEdit()
s2.setPlaceholderText("Wprowadź nowe dane...")
editPerson = QPushButton()
editBook = QPushButton()
editPerson.setText("edytuj osobę")
editBook.setText("edytuj książkę")

def F_editPerson():
    indexOsoby = view.selectionModel().currentIndex()
    if indexOsoby.isValid():
        personID = model.record(indexOsoby.row()).value("PersonID")
        if s1.text().strip() != "" and s2.text().strip() != "":
            print(s1.text().strip(), s2.text().strip())
            edit_person(personID,s1.text().strip(), s2.text().strip())
            model.select()
            model2.select()
            model3.setQuery(query3)
        else:
            infoLabel.setText("NIE WPROWADZONO DANYCH!")
def F_editBook():
    indexKsiazki = view2.selectionModel().currentIndex()
    if indexKsiazki.isValid():
        bookID = model2.record(indexKsiazki.row()).value("BookID")
        if s1.text().strip() != "" and s2.text().strip() != "":
            print(s1.text().strip(), s2.text().strip())
            edit_book(bookID ,s1.text().strip(), s2.text().strip())
            model.select()
            model2.select()
            model3.setQuery(query3)
        else:
            infoLabel.setText("NIE WPROWADZONO DANYCH!")

editPerson.clicked.connect(F_editPerson)
editBook.clicked.connect(F_editBook)
Options.addWidget(s1)
Options.addWidget(s2)
Options.addWidget(editPerson)
Options.addWidget(editBook)

Sections.addLayout(Options,1)
#endregion

info = QVBoxLayout()
info.addWidget(infoLabel)

mainLayout.addLayout(Sections)
mainLayout.addLayout(info)
window.setLayout(mainLayout)

model.select()
model2.select()
model3.setQuery(query3)

window.show()

sys.exit(app.exec())