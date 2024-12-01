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

    QSqlQuery query(db);
    query.exec("CREATE TABLE osoba (id INTEGER PRIMARY KEY, imie TEXT, nazwisko TEXT)");

    query.exec("CREATE TABLE ksiazka (id INTEGER PRIMARY KEY, tytul TEXT, autor TEXT)");

    query.exec("CREATE TABLE wypozyczenia (id INTEGER PRIMARY KEY, osoba_id INTEGER, ksiazka_id INTEGER, FOREIGN KEY(osoba_id) REFERENCES osoba(id), FOREIGN KEY(ksiazka_id) REFERENCES ksiazka(id)) ");

    QVBoxLayout *layout1 = new QVBoxLayout(ui->osoby);
    int margintop = 20;
    layout1->setAlignment(Qt::AlignTop);
    layout1->setContentsMargins(0, margintop, 0, 0);
    ui->osoby->setLayout(layout1);

    QVBoxLayout *layout2 = new QVBoxLayout(ui->ksiazki);
    layout2->setAlignment(Qt::AlignTop);
    layout2->setContentsMargins(0, margintop, 0, 0);
    ui->ksiazki->setLayout(layout2);

    QVBoxLayout *layout3 = new QVBoxLayout(ui->wypozyczenia);
    layout3->setAlignment(Qt::AlignTop);
    layout3->setContentsMargins(0, margintop, 0, 0);
    ui->wypozyczenia->setLayout(layout3);
}
void MainWindow::ResetTables(){
    QList<QWidget*> widgets1 = ui->osoby->findChildren<QWidget*>();
    QList<QWidget*> widgets2 = ui->ksiazki->findChildren<QWidget*>();
    QList<QWidget*> widgets3 = ui->wypozyczenia->findChildren<QWidget*>();

    for (QWidget* widget : widgets1) {
        delete widget;
    }
    for (QWidget* widget : widgets2) {
        delete widget;
    }
    for (QWidget* widget : widgets3) {
        delete widget;
    }
}
void MainWindow::UpdateTables(QSqlQuery &query){
    if (query.exec("SELECT * FROM osoba"))
    {
        while (query.next())
        {
            int id = query.value(0).toInt();
            QString imie = query.value(1).toString();
            QString nazwisko = query.value(2).toString();

            QString radioButtonName = QString::number(id) + ". " + imie + " " + nazwisko;
            QRadioButton *radioButton = new QRadioButton(radioButtonName, ui->osoby);
            connect(radioButton , &QRadioButton::clicked , this , [=](){
            LastPressedPerson = radioButton;
            cout<<radioButton->text().toStdString()<<endl;
            });

            //radiobutton
            ui->osoby->layout()->addWidget(radioButton);
        }
    }

    if (query.exec("SELECT * FROM ksiazka"))
    {
        while (query.next())
        {
            int id = query.value(0).toInt();
            QString tytul = query.value(1).toString();
            QString autor = query.value(2).toString();

            QString radioButtonName = QString::number(id) + ". " + tytul + " " + autor;
            QRadioButton *radioButton = new QRadioButton(radioButtonName, ui->ksiazki);
            connect(radioButton , &QRadioButton::clicked , this , [=](){
                LastPressedBook = radioButton;
                cout<<radioButton->text().toStdString()<<endl;
            });

            //radiobutton
            ui->ksiazki->layout()->addWidget(radioButton);
        }
    }

    if (query.exec("SELECT * FROM wypozyczenia"))
    {
        while (query.next())
        {
            int id = query.value(0).toInt();
            int idOsoby = query.value(1).toInt();
            int idKsiazki = query.value(2).toInt();

            QString osobaImieNazwisko;
            QString ksiazkaTytulAutor;

            QSqlQuery osobaQuery(db);
            osobaQuery.prepare("SELECT imie, nazwisko FROM osoba WHERE id = :id");
            osobaQuery.bindValue(":id", idOsoby);

            if (osobaQuery.exec() && osobaQuery.next()) {
                QString imie = osobaQuery.value(0).toString();
                QString nazwisko = osobaQuery.value(1).toString();
                osobaImieNazwisko = imie + " " + nazwisko;
            } else {
                osobaImieNazwisko = "Nieznane imię i nazwisko";
            }

            QSqlQuery ksiazkaQuery(db);
            ksiazkaQuery.prepare("SELECT tytul, autor FROM ksiazka WHERE id = :id");
            ksiazkaQuery.bindValue(":id", idKsiazki);

            if (ksiazkaQuery.exec() && ksiazkaQuery.next()) {
                QString tytul = ksiazkaQuery.value(0).toString();
                QString autor = ksiazkaQuery.value(1).toString();
                ksiazkaTytulAutor = tytul + " " + autor;
            } else {
                ksiazkaTytulAutor = "Nieznany tytuł i autor";
            }

            QString radioButtonName = QString::number(id) + ". " + osobaImieNazwisko + " wypożyczył/a: " + ksiazkaTytulAutor;
            QRadioButton *radioButton = new QRadioButton(radioButtonName, ui->wypozyczenia);
            connect(radioButton, &QRadioButton::clicked, this, [=]() {
                LastPressedWypo = radioButton;
                cout << radioButton->text().toStdString() << endl;
            });

            if (!ui->wypozyczenia->layout()) {
                QVBoxLayout *layout = new QVBoxLayout(ui->wypozyczenia);
                ui->wypozyczenia->setLayout(layout);
            }
            ui->wypozyczenia->layout()->addWidget(radioButton);
        }
    }

    LastPressedPerson = nullptr;
    LastPressedBook = nullptr;
    LastPressedWypo = nullptr;
}

void MainWindow::CreatePerson(QSqlQuery &query, QString imie, QString nazwisko){
    query.prepare("INSERT INTO osoba (imie, nazwisko) VALUES (:imie, :nazwisko)");

    query.bindValue(":imie", imie);
    query.bindValue(":nazwisko", nazwisko);

    if (query.exec()) {
        cout<< " dodano osobe"<<endl;
    } else {
        cout << "Błąd: Nie udało się dodać osoby!" << endl;
    }
    MainWindow::ResetTables();
    MainWindow::UpdateTables(query);
}

void MainWindow::CreateBook(QSqlQuery &query, QString tytul, QString autor){
    query.prepare("INSERT INTO ksiazka (tytul, autor) VALUES (:tytul, :autor)");

    query.bindValue(":tytul", tytul);
    query.bindValue(":autor", autor);

    if (query.exec()) {
        cout<< " dodano ksiazke"<<endl;
    } else {
        cout << "Błąd: Nie udało się dodać ksiazki!" << endl;
    }

    MainWindow::ResetTables();
    MainWindow::UpdateTables(query);
}

void MainWindow::CreateWypozyczenie(QSqlQuery &query, int osobaId, int ksiazkaId){
    query.prepare("INSERT INTO wypozyczenia (osoba_id, ksiazka_id) VALUES (:osoba_id, :ksiazka_id)");

    query.bindValue(":osoba_id", osobaId);
    query.bindValue(":ksiazka_id", ksiazkaId);

    if (query.exec()) {
        cout<< " dodano wypo"<<endl;
    } else {
        cout << "Błąd: Nie udało się dodać ksiazki!" << endl;
    }

    MainWindow::ResetTables();
    MainWindow::UpdateTables(query);
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

void MainWindow::on_ksiazkaAdd_clicked()
{
    QSqlQuery query(db);
    if(ui->KsiazkaTyt->toPlainText().trimmed().isEmpty()){
        return;
    }
    if(ui->KsiazkaAutor->toPlainText().trimmed().isEmpty()){
        return;
    }

    QString ksiazkaTyt = ui->KsiazkaTyt->toPlainText().trimmed();
    QString ksiazkaAutor = ui->KsiazkaAutor->toPlainText().trimmed();

    MainWindow::CreateBook(query, ksiazkaTyt, ksiazkaAutor);
}


void MainWindow::on_wypozycz_clicked()
{
    QSqlQuery query(db);

    if(LastPressedPerson && LastPressedBook){
        int osobaId = LastPressedPerson->text().split(".")[0].toInt();
        int ksiazkaId= LastPressedBook->text().split(".")[0].toInt();


        MainWindow::CreateWypozyczenie(query, osobaId, ksiazkaId);
    }
}


void MainWindow::on_oddaj_clicked()
{
    QSqlQuery query(db);

    if(LastPressedWypo){
        int wypozyczenieId = LastPressedWypo->text().split(".")[0].toInt();

        query.prepare("DELETE FROM wypozyczenia WHERE id = :id");
        query.bindValue(":id", wypozyczenieId);

        if (query.exec()) {
            cout << "oddano ksiazke" << endl;
        }

        MainWindow::ResetTables();
        MainWindow::UpdateTables(query);
    }

}
