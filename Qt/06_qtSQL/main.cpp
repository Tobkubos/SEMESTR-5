#include <QCoreApplication>
#include <QtSql>
#include <iostream>
using namespace std;

void DisplayQuery(QSqlDatabase& _db, QString _q);

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    // Utworzenie bazy danych SQLite w pamięci
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE", "bazatestowa");
    db.setDatabaseName(":memory:"); // Baza danych w pamięci

    if (!db.open())
    {
        cout << "Error: Unable to open SQLite database!" << endl;
        return -1;
    }

    cout << "Connection established with SQLite database.\n";

    // Tworzenie tabeli i wstawianie rekordów
    QSqlQuery query(db);
    query.exec("CREATE TABLE osoba (id INT PRIMARY KEY, imie VARCHAR(20), nazwisko VARCHAR(20))");

    query.exec("INSERT INTO osoba VALUES (101, 'Jan', 'Kowalski')");
    query.exec("INSERT INTO osoba VALUES (102, 'Mariusz', 'Nowak')");
    query.exec("INSERT INTO osoba VALUES (103, 'Krzysztof', 'Nowak')");
    query.exec("INSERT INTO osoba VALUES (104, 'Robert', 'Kowalski')");
    query.exec("INSERT INTO osoba VALUES (105, 'Marek', 'Cybulski')");
    query.exec("INSERT INTO osoba VALUES (106, 'Wacek', 'Nowak')");

    // Wyświetlenie rekordów z tabeli "osoba"
    DisplayQuery(db, "SELECT * FROM osoba");

    // Zamknięcie połączenia
    db.close();
    QSqlDatabase::removeDatabase("bazatestowa");

    return a.exec();
}

void DisplayQuery(QSqlDatabase& _db, QString _q)
{
    cout << "---------------------\n"
         << "  Query to database\n"
         << "---------------------\n";

    QSqlQuery query(_q, _db);

    while (query.next())
    {
        for (int i = 0; i < query.record().count(); i++)
        {
            cout << ((const char*)query.value(i).toString().toLatin1()) << " ";
        }
        cout << endl;
    }

    query.finish();
    cout << "---------------------\n";
}
