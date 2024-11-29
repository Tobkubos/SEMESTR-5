#include "mainwindow.h"
#include "qlayoutitem.h"
#include "ui_mainwindow.h"
#include<iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    db = QSqlDatabase::addDatabase("QSQLITE", "bazatestowa");
    db.setDatabaseName(":memory:"); // Baza danych w pamięci

    if (!db.open())
    {
        cout << "Error: Unable to open SQLite database!" << endl;
        return;
    }

    cout << "Connection established with SQLite database.\n";

    // Dodanie przykładowych tabel i danych
    QSqlQuery query(db);
    query.exec("CREATE TABLE osoba (id INTEGER PRIMARY KEY, imie TEXT, nazwisko TEXT)");

    query.exec("CREATE TABLE ksiazka (id INTEGER PRIMARY KEY, tytul TEXT, autor TEXT)");

    query.exec("CREATE TABLE wypozyczenia (id INTEGER PRIMARY KEY, osoba_id INTEGER, ksiazka_id INTEGER, FOREIGN KEY(osoba_id) REFERENCES osoba(id), FOREIGN KEY(ksiazka_id) REFERENCES ksiazka(id) ");


//
    CreatePerson(query, "jas", "fasola");
//


    if (query.exec("SELECT * FROM osoba"))
    {
        while (query.next())
        {
            int id = query.value(0).toInt();
            QString imie = query.value(1).toString();
            QString nazwisko = query.value(2).toString();
            cout << "ID: " << id << ", Imie: " << imie.toStdString()
                 << ", Nazwisko: " << nazwisko.toStdString() << endl;
        }
    }
    else
    {
        cout << "Error: Failed to execute query!" << endl;
    }
}



void MainWindow::CreatePerson(QSqlQuery &query, QString imie, QString nazwisko){
    query.prepare("INSERT INTO osoba (imie, nazwisko) VALUES (:imie, :nazwisko)");

    query.bindValue(":imie", imie);
    query.bindValue(":nazwisko", nazwisko);

    if (query.exec()) {
        QString radioButtonName = imie + " " + nazwisko;

        // Tworzenie guzika
        QRadioButton *radioButton = new QRadioButton(radioButtonName, ui->osoby);

        if (!ui->osoby->layout()) {
            QVBoxLayout *layout = new QVBoxLayout(ui->osoby);
            ui->osoby->setLayout(layout);
        }

        //radiobutton
        ui->osoby->layout()->addWidget(radioButton);
    } else {
        cout << "Błąd: Nie udało się dodać osoby!" << endl;
    }
}

MainWindow::~MainWindow()
{
    QSqlDatabase db = QSqlDatabase::database("bazatestowa");
    if (db.isOpen())
    {
        db.close();
    }
    QSqlDatabase::removeDatabase("bazatestowa");

    delete ui;
}

void MainWindow::on_osobaAdd_clicked()
{
    QSqlQuery query(db);
    if(ui->OsobaImie->toPlainText().trimmed().isEmpty()){
        return;
    }
    if(ui->OsobaNazw->toPlainText().trimmed().isEmpty()){
        return;
    }

    QString imieOs = ui->OsobaImie->toPlainText().trimmed();
    QString nazwiskoOs = ui->OsobaNazw->toPlainText().trimmed();

    MainWindow::CreatePerson(query, imieOs, nazwiskoOs);
}


