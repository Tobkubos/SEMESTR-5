/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QTextEdit *KsiazkaTyt;
    QTextEdit *KsiazkaAutor;
    QLabel *label;
    QLabel *label_2;
    QTextEdit *OsobaNazw;
    QTextEdit *OsobaImie;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QPushButton *osobaAdd;
    QPushButton *ksiazkaAdd;
    QGroupBox *osoby;
    QGroupBox *ksiazki;
    QGroupBox *wypozyczenia;
    QPushButton *wypozycz;
    QPushButton *oddaj;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1298, 623);
        MainWindow->setMinimumSize(QSize(1298, 623));
        MainWindow->setMaximumSize(QSize(1298, 623));
        MainWindow->setStyleSheet(QString::fromUtf8("QWidget{\n"
"background-color: rgb(16, 0, 43);\n"
"border: 2px solid rgb(199, 125, 255);\n"
"border-radius: 15px;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"}\n"
"\n"
"QLabel{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(157, 78, 221);\n"
"color: rgb(16, 0, 43);\n"
"}\n"
"\n"
"QRadioButton{\n"
"border: none;\n"
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        centralwidget->setMinimumSize(QSize(1298, 623));
        centralwidget->setMaximumSize(QSize(1298, 623));
        centralwidget->setBaseSize(QSize(1298, 623));
        KsiazkaTyt = new QTextEdit(centralwidget);
        KsiazkaTyt->setObjectName("KsiazkaTyt");
        KsiazkaTyt->setGeometry(QRect(10, 260, 321, 31));
        KsiazkaAutor = new QTextEdit(centralwidget);
        KsiazkaAutor->setObjectName("KsiazkaAutor");
        KsiazkaAutor->setGeometry(QRect(10, 320, 321, 31));
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(10, 240, 321, 16));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(10, 300, 321, 16));
        OsobaNazw = new QTextEdit(centralwidget);
        OsobaNazw->setObjectName("OsobaNazw");
        OsobaNazw->setGeometry(QRect(10, 120, 321, 31));
        OsobaImie = new QTextEdit(centralwidget);
        OsobaImie->setObjectName("OsobaImie");
        OsobaImie->setGeometry(QRect(10, 60, 321, 31));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(10, 100, 321, 16));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(10, 40, 321, 16));
        label_5 = new QLabel(centralwidget);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(10, 20, 321, 16));
        label_6 = new QLabel(centralwidget);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(10, 220, 321, 16));
        osobaAdd = new QPushButton(centralwidget);
        osobaAdd->setObjectName("osobaAdd");
        osobaAdd->setGeometry(QRect(250, 160, 80, 24));
        ksiazkaAdd = new QPushButton(centralwidget);
        ksiazkaAdd->setObjectName("ksiazkaAdd");
        ksiazkaAdd->setGeometry(QRect(250, 360, 80, 24));
        osoby = new QGroupBox(centralwidget);
        osoby->setObjectName("osoby");
        osoby->setGeometry(QRect(360, 40, 191, 541));
        ksiazki = new QGroupBox(centralwidget);
        ksiazki->setObjectName("ksiazki");
        ksiazki->setGeometry(QRect(560, 40, 201, 541));
        wypozyczenia = new QGroupBox(centralwidget);
        wypozyczenia->setObjectName("wypozyczenia");
        wypozyczenia->setGeometry(QRect(770, 40, 521, 541));
        wypozycz = new QPushButton(centralwidget);
        wypozycz->setObjectName("wypozycz");
        wypozycz->setGeometry(QRect(360, 590, 401, 24));
        oddaj = new QPushButton(centralwidget);
        oddaj->setObjectName("oddaj");
        oddaj->setGeometry(QRect(770, 590, 521, 24));
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Nazwa Ksi\304\205\305\274ki", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Autor", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Nazwisko", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Imi\304\231", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Wprowad\305\272 osob\304\231 do bazy", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Wprowad\305\272 ksi\304\205\305\274k\304\231 do bazy", nullptr));
        osobaAdd->setText(QCoreApplication::translate("MainWindow", "dodaj", nullptr));
        ksiazkaAdd->setText(QCoreApplication::translate("MainWindow", "dodaj", nullptr));
        osoby->setTitle(QCoreApplication::translate("MainWindow", "Osoby", nullptr));
        ksiazki->setTitle(QCoreApplication::translate("MainWindow", "Ksi\304\205\305\274ki", nullptr));
        wypozyczenia->setTitle(QCoreApplication::translate("MainWindow", "Wypo\305\274yczenia", nullptr));
        wypozycz->setText(QCoreApplication::translate("MainWindow", "Wypo\305\274ycz!", nullptr));
        oddaj->setText(QCoreApplication::translate("MainWindow", "Oddaj!", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
