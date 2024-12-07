import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit,QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QGroupBox, QRadioButton, QListWidget, QListWidgetItem
#priorytety
one = "normalnie"
two = "na spokojnie"
three = "WAŻNE!"

app = QApplication([])

window = QWidget()
window.setWindowTitle("Task Manager")
window.setGeometry(300, 300, 700, 700)

mainLayoutV = QVBoxLayout()

#region PASEK GÓRA
layoutTopH = QHBoxLayout()

#WPROWADŹ ZADANIE
zadanieInput = QLineEdit()
zadanieInput.setPlaceholderText("Wprowadź nazwe zadania...")
layoutTopH.addWidget(zadanieInput)

#USTAW PRIORYTET
SetPriority = QComboBox()
SetPriority.addItem(one)
SetPriority.addItem(two)
SetPriority.addItem(three)
layoutTopH.addWidget(SetPriority)

#DODAJ ZADANIE
AddZadanie = QPushButton()
AddZadanie.setText("dodaj zadanie")
def DodajZadanie():
    nazwaZadania = zadanieInput.text().strip()
    priorytet = SetPriority.currentText()

    if nazwaZadania:
        Informacja.setText(f" DODANO ZADANIE!: {nazwaZadania} ({priorytet})")
        item = QListWidgetItem(f"{nazwaZadania} ({priorytet})")
        ListaZadan.addItem(item)
        zadanieInput.clear()
        IloscZadan.setText(f" LICZBA ZADAŃ: {ListaZadan.count()}")
        print(item.text())

AddZadanie.clicked.connect(DodajZadanie)
layoutTopH.addWidget(AddZadanie)

##ZEPNIJ W CAŁOŚĆ
mainLayoutV.addItem(layoutTopH)

#SORTUJ
        #sortuj po priorytecie
lyt = QHBoxLayout()
sortowanie = QPushButton()
sortowanie.setText("sortuj")
lyt.addWidget(sortowanie)

zapisz = QPushButton()
zapisz.setText("zapisz")
lyt.addWidget(zapisz)

wczytaj = QPushButton()
wczytaj.setText("wczytaj")
lyt.addWidget(wczytaj)

def zapisz_do_pliku():
    Informacja.setStyleSheet("color: green;")
    with open("zadania.txt", "w", encoding="utf-8") as file:
        for i in range(ListaZadan.count()):
            item = ListaZadan.item(i)
            file.write(item.text() + "\n")
    Informacja.setText("Zadania zostały zapisane!")

def wczytaj_z_pliku():
    Informacja.setStyleSheet("color: green;")
    try:
        with open("zadania.txt", "r", encoding="utf-8") as file:
            ListaZadan.clear()
            for line in file:
                item = QListWidgetItem(line.strip())
                ListaZadan.addItem(item)
        Informacja.setText("Zadania zostały wczytane!")
    except FileNotFoundError:
        Informacja.setStyleSheet("color: red;")
        Informacja.setText("Plik z zadaniami nie został znaleziony!")
    IloscZadan.setText(f" LICZBA ZADAŃ: {ListaZadan.count()}")

def sortuj():
    items = []
    for i in range(ListaZadan.count()):
        items.append(ListaZadan.item(i).text())

    priority_order = {one: 1, two: 2, three: 3}
    items.sort(key=lambda task: (task.split(" ")[-1].strip("()"), task))

    ListaZadan.clear()
    for item in items:
        ListaZadan.addItem(item)


zapisz.clicked.connect(zapisz_do_pliku)
wczytaj.clicked.connect(wczytaj_z_pliku)
sortowanie.clicked.connect(sortuj)


mainLayoutV.addItem(lyt)

#endregion

#region LISTA ZADAŃ
ListaZadan = QListWidget()
mainLayoutV.addWidget(ListaZadan)

#ETYKIETA QLABEL Z INFORMACJĄ
Informacja = QLabel()
Informacja.setStyleSheet("color: green;")
Informacja.setText(" ")
mainLayoutV.addWidget(Informacja)
#endregion

#region PASEK DÓŁ
layoutBottomH = QHBoxLayout()
#USUŃ ZADANIE
DelTask = QPushButton()
DelTask.setText("Usuń zadanie")
def UsunZadanie():
    Informacja.setStyleSheet("color: green;")
    item = ListaZadan.currentItem()
    if item:
        Informacja.setText(f" USUNIETO ZADANIE!: {item.text()})")
        task = ListaZadan.row(item)
        ListaZadan.takeItem(task)
        zadanieInput.clear()
        IloscZadan.setText(f" LICZBA ZADAŃ: {ListaZadan.count()}")

DelTask.clicked.connect(UsunZadanie)
layoutBottomH.addWidget(DelTask)

#LICZBA ZADAŃ
IloscZadan = QLabel()
IloscZadan.setText(f" LICZBA ZADAŃ: {ListaZadan.count()}")

HowToEdit = QLabel()
HowToEdit.setText("aby edytować: \n - 1. kliknij na zadanie \n - 2. wpisz nową nazwę lub zmień priorytet \n - 3. kliknij edytuj zadanie")
mainLayoutV.addWidget(IloscZadan)
mainLayoutV.addWidget(HowToEdit)

#EDYTUJ ZADANIE
EditTask = QPushButton()
EditTask.setText("Edytuj zadanie")
def EdytujZadanie():
    Informacja.setStyleSheet("color: green;")
    item = ListaZadan.currentItem()
    nazwaZadania = zadanieInput.text().strip()
    priorytet = SetPriority.currentText()
    if item:
        if nazwaZadania:
            Informacja.setText(f" ZAKTUALIZOWANO ZADANIE:{item.text()} na {nazwaZadania} ({priorytet})")
            
        elif priorytet:
            Informacja.setText(f" ZAKTUALIZOWANO PRIORYTET:{item.text()} na ({priorytet})")
            nazwaZadania = " ".join(item.text().split()[:-1])
        
        task = ListaZadan.row(item)
        ListaZadan.takeItem(task)
        item = QListWidgetItem(f"{nazwaZadania} ({priorytet})")
        ListaZadan.addItem(item)
        zadanieInput.clear()
        IloscZadan.setText(f" LICZBA ZADAŃ: {ListaZadan.count()}")

EditTask.clicked.connect(EdytujZadanie)
layoutBottomH.addWidget(EditTask)
##ZEPNIJ W CAŁOŚĆ
mainLayoutV.addItem(layoutBottomH)
#endregion

window.setLayout(mainLayoutV)
window.show()
sys.exit(app.exec())