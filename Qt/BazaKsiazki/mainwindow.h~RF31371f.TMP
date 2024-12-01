#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QCoreApplication>
#include <QtSql>
#include<QRadioButton>
#include <QVBoxLayout>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_osobaAdd_clicked();
    void on_ksiazkaAdd_clicked();
    void on_wypozycz_clicked();
    void on_oddaj_clicked();


private:
    Ui::MainWindow *ui;
    QSqlDatabase db;
    void CreatePerson(QSqlQuery &query, QString imie, QString nazwisko);
    void CreateBook(QSqlQuery &query, QString tytul, QString autor);
    void CreateWypozyczenie(QSqlQuery &query, int osobaId, int ksiazkaId);
    void UpdateTables(QSqlQuery &query);
    void ResetTables();

    QRadioButton* LastPressedPerson;
    QRadioButton* LastPressedBook;
    QRadioButton* LastPressedWypo;
};
#endif // MAINWINDOW_H
