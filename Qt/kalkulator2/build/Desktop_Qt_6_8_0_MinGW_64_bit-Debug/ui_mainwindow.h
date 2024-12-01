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
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton_1;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_8;
    QPushButton *pushButton_7;
    QPushButton *pushButton_6;
    QPushButton *pushButton_5;
    QPushButton *pushButton_4;
    QPushButton *pushButton_9;
    QLabel *wynik;
    QPushButton *pushButton_0;
    QPushButton *pushButton_dot;
    QPushButton *pushButton_calc;
    QPushButton *pushButton_plus;
    QPushButton *pushButton_substract;
    QPushButton *pushButton_multiply;
    QPushButton *pushButton_divide;
    QPushButton *pushButton_del;
    QLabel *title;
    QLabel *historia;
    QPushButton *pushButton_log;
    QPushButton *pushButton_pow;
    QPushButton *pushButton_abs;
    QPushButton *pushButton_sin;
    QPushButton *pushButton_cos;
    QPushButton *pushButton_tg;
    QPushButton *pushButton_ctg;
    QLabel *error;
    QPushButton *pushButton_clearh;
    QPushButton *pushButton_back;
    QPushButton *pushButton_sqrt;
    QPushButton *pushButton_ln;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(840, 460);
        MainWindow->setMinimumSize(QSize(840, 460));
        MainWindow->setMaximumSize(QSize(840, 460));
        MainWindow->setStyleSheet(QString::fromUtf8("QWidget{\n"
"background-color: rgb(0,0,0)\n"
"}\n"
"\n"
"QPushButton{\n"
"border: none;\n"
"border: 3px solid rgb(90,102,80);\n"
"border-radius:15px;\n"
"background-color: rgb(14,64,45);\n"
"color: rgb(159,204,46);\n"
"}\n"
"QLabel{\n"
"color: rgb(159,204,46);\n"
"border: 3px solid rgb(159,204,46);\n"
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        pushButton_1 = new QPushButton(centralwidget);
        pushButton_1->setObjectName("pushButton_1");
        pushButton_1->setGeometry(QRect(270, 330, 64, 64));
        QFont font;
        font.setPointSize(15);
        pushButton_1->setFont(font);
        pushButton_2 = new QPushButton(centralwidget);
        pushButton_2->setObjectName("pushButton_2");
        pushButton_2->setGeometry(QRect(330, 330, 64, 64));
        pushButton_2->setFont(font);
        pushButton_3 = new QPushButton(centralwidget);
        pushButton_3->setObjectName("pushButton_3");
        pushButton_3->setGeometry(QRect(390, 330, 64, 64));
        pushButton_3->setFont(font);
        pushButton_8 = new QPushButton(centralwidget);
        pushButton_8->setObjectName("pushButton_8");
        pushButton_8->setGeometry(QRect(330, 210, 64, 64));
        pushButton_8->setFont(font);
        pushButton_7 = new QPushButton(centralwidget);
        pushButton_7->setObjectName("pushButton_7");
        pushButton_7->setGeometry(QRect(270, 210, 64, 64));
        pushButton_7->setFont(font);
        pushButton_6 = new QPushButton(centralwidget);
        pushButton_6->setObjectName("pushButton_6");
        pushButton_6->setGeometry(QRect(390, 270, 64, 64));
        pushButton_6->setFont(font);
        pushButton_5 = new QPushButton(centralwidget);
        pushButton_5->setObjectName("pushButton_5");
        pushButton_5->setGeometry(QRect(330, 270, 64, 64));
        pushButton_5->setFont(font);
        pushButton_4 = new QPushButton(centralwidget);
        pushButton_4->setObjectName("pushButton_4");
        pushButton_4->setGeometry(QRect(270, 270, 64, 64));
        pushButton_4->setFont(font);
        pushButton_9 = new QPushButton(centralwidget);
        pushButton_9->setObjectName("pushButton_9");
        pushButton_9->setGeometry(QRect(390, 210, 64, 64));
        pushButton_9->setFont(font);
        wynik = new QLabel(centralwidget);
        wynik->setObjectName("wynik");
        wynik->setGeometry(QRect(10, 50, 521, 71));
        QFont font1;
        font1.setPointSize(25);
        font1.setBold(true);
        wynik->setFont(font1);
        wynik->setFrameShape(QFrame::Shape::Box);
        wynik->setFrameShadow(QFrame::Shadow::Plain);
        wynik->setLineWidth(2);
        wynik->setScaledContents(false);
        wynik->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);
        pushButton_0 = new QPushButton(centralwidget);
        pushButton_0->setObjectName("pushButton_0");
        pushButton_0->setGeometry(QRect(330, 390, 64, 64));
        pushButton_0->setFont(font);
        pushButton_dot = new QPushButton(centralwidget);
        pushButton_dot->setObjectName("pushButton_dot");
        pushButton_dot->setGeometry(QRect(390, 390, 64, 64));
        pushButton_dot->setFont(font);
        pushButton_calc = new QPushButton(centralwidget);
        pushButton_calc->setObjectName("pushButton_calc");
        pushButton_calc->setGeometry(QRect(470, 390, 64, 64));
        pushButton_calc->setFont(font);
        pushButton_calc->setCheckable(false);
        pushButton_plus = new QPushButton(centralwidget);
        pushButton_plus->setObjectName("pushButton_plus");
        pushButton_plus->setGeometry(QRect(470, 310, 64, 64));
        pushButton_plus->setFont(font);
        pushButton_substract = new QPushButton(centralwidget);
        pushButton_substract->setObjectName("pushButton_substract");
        pushButton_substract->setGeometry(QRect(470, 250, 64, 64));
        pushButton_substract->setFont(font);
        pushButton_multiply = new QPushButton(centralwidget);
        pushButton_multiply->setObjectName("pushButton_multiply");
        pushButton_multiply->setGeometry(QRect(470, 190, 64, 64));
        pushButton_multiply->setFont(font);
        pushButton_divide = new QPushButton(centralwidget);
        pushButton_divide->setObjectName("pushButton_divide");
        pushButton_divide->setGeometry(QRect(470, 130, 64, 64));
        pushButton_divide->setFont(font);
        pushButton_del = new QPushButton(centralwidget);
        pushButton_del->setObjectName("pushButton_del");
        pushButton_del->setGeometry(QRect(130, 130, 64, 64));
        QFont font2;
        font2.setPointSize(15);
        font2.setBold(false);
        font2.setUnderline(false);
        pushButton_del->setFont(font2);
        pushButton_del->setCursor(QCursor(Qt::CursorShape::ArrowCursor));
        pushButton_del->setStyleSheet(QString::fromUtf8(""));
        title = new QLabel(centralwidget);
        title->setObjectName("title");
        title->setGeometry(QRect(10, 10, 821, 31));
        QFont font3;
        font3.setPointSize(12);
        font3.setBold(true);
        title->setFont(font3);
        title->setFrameShape(QFrame::Shape::Box);
        title->setFrameShadow(QFrame::Shadow::Plain);
        title->setLineWidth(2);
        title->setScaledContents(false);
        title->setAlignment(Qt::AlignmentFlag::AlignCenter);
        historia = new QLabel(centralwidget);
        historia->setObjectName("historia");
        historia->setGeometry(QRect(540, 130, 291, 321));
        QFont font4;
        font4.setPointSize(16);
        font4.setBold(true);
        historia->setFont(font4);
        historia->setFrameShape(QFrame::Shape::Box);
        historia->setFrameShadow(QFrame::Shadow::Plain);
        historia->setLineWidth(2);
        historia->setScaledContents(false);
        historia->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTop|Qt::AlignmentFlag::AlignTrailing);
        pushButton_log = new QPushButton(centralwidget);
        pushButton_log->setObjectName("pushButton_log");
        pushButton_log->setGeometry(QRect(130, 270, 64, 64));
        pushButton_log->setFont(font);
        pushButton_pow = new QPushButton(centralwidget);
        pushButton_pow->setObjectName("pushButton_pow");
        pushButton_pow->setGeometry(QRect(410, 130, 64, 64));
        pushButton_pow->setFont(font);
        pushButton_abs = new QPushButton(centralwidget);
        pushButton_abs->setObjectName("pushButton_abs");
        pushButton_abs->setGeometry(QRect(10, 270, 64, 64));
        pushButton_abs->setFont(font);
        pushButton_sin = new QPushButton(centralwidget);
        pushButton_sin->setObjectName("pushButton_sin");
        pushButton_sin->setGeometry(QRect(10, 210, 64, 64));
        pushButton_sin->setFont(font);
        pushButton_cos = new QPushButton(centralwidget);
        pushButton_cos->setObjectName("pushButton_cos");
        pushButton_cos->setGeometry(QRect(70, 210, 64, 64));
        pushButton_cos->setFont(font);
        pushButton_tg = new QPushButton(centralwidget);
        pushButton_tg->setObjectName("pushButton_tg");
        pushButton_tg->setGeometry(QRect(130, 210, 64, 64));
        pushButton_tg->setFont(font);
        pushButton_ctg = new QPushButton(centralwidget);
        pushButton_ctg->setObjectName("pushButton_ctg");
        pushButton_ctg->setGeometry(QRect(190, 210, 64, 64));
        pushButton_ctg->setFont(font);
        error = new QLabel(centralwidget);
        error->setObjectName("error");
        error->setGeometry(QRect(540, 50, 291, 71));
        error->setFont(font3);
        error->setFrameShape(QFrame::Shape::Box);
        error->setFrameShadow(QFrame::Shadow::Plain);
        error->setLineWidth(2);
        error->setScaledContents(false);
        error->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);
        pushButton_clearh = new QPushButton(centralwidget);
        pushButton_clearh->setObjectName("pushButton_clearh");
        pushButton_clearh->setGeometry(QRect(10, 130, 121, 64));
        pushButton_clearh->setFont(font2);
        pushButton_clearh->setCursor(QCursor(Qt::CursorShape::ArrowCursor));
        pushButton_clearh->setStyleSheet(QString::fromUtf8(""));
        pushButton_back = new QPushButton(centralwidget);
        pushButton_back->setObjectName("pushButton_back");
        pushButton_back->setGeometry(QRect(190, 130, 64, 64));
        pushButton_back->setFont(font2);
        pushButton_back->setCursor(QCursor(Qt::CursorShape::ArrowCursor));
        pushButton_back->setStyleSheet(QString::fromUtf8(""));
        pushButton_sqrt = new QPushButton(centralwidget);
        pushButton_sqrt->setObjectName("pushButton_sqrt");
        pushButton_sqrt->setGeometry(QRect(70, 270, 64, 64));
        pushButton_sqrt->setFont(font);
        pushButton_ln = new QPushButton(centralwidget);
        pushButton_ln->setObjectName("pushButton_ln");
        pushButton_ln->setGeometry(QRect(190, 270, 64, 64));
        pushButton_ln->setFont(font);
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        pushButton_calc->setDefault(false);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "KALKULATOREK", nullptr));
        pushButton_1->setText(QCoreApplication::translate("MainWindow", "1", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "2", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "3", nullptr));
        pushButton_8->setText(QCoreApplication::translate("MainWindow", "8", nullptr));
        pushButton_7->setText(QCoreApplication::translate("MainWindow", "7", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", "6", nullptr));
        pushButton_5->setText(QCoreApplication::translate("MainWindow", "5", nullptr));
        pushButton_4->setText(QCoreApplication::translate("MainWindow", "4", nullptr));
        pushButton_9->setText(QCoreApplication::translate("MainWindow", "9", nullptr));
        wynik->setText(QString());
        pushButton_0->setText(QCoreApplication::translate("MainWindow", "0", nullptr));
        pushButton_dot->setText(QCoreApplication::translate("MainWindow", ".", nullptr));
        pushButton_calc->setText(QCoreApplication::translate("MainWindow", "=", nullptr));
        pushButton_plus->setText(QCoreApplication::translate("MainWindow", "+", nullptr));
        pushButton_substract->setText(QCoreApplication::translate("MainWindow", "-", nullptr));
        pushButton_multiply->setText(QCoreApplication::translate("MainWindow", "x", nullptr));
        pushButton_divide->setText(QCoreApplication::translate("MainWindow", "/", nullptr));
        pushButton_del->setText(QCoreApplication::translate("MainWindow", "C", nullptr));
        title->setText(QCoreApplication::translate("MainWindow", "KALKULATOREK", nullptr));
        historia->setText(QString());
        pushButton_log->setText(QCoreApplication::translate("MainWindow", "log", nullptr));
        pushButton_pow->setText(QCoreApplication::translate("MainWindow", "^", nullptr));
        pushButton_abs->setText(QCoreApplication::translate("MainWindow", "|x|", nullptr));
        pushButton_sin->setText(QCoreApplication::translate("MainWindow", "sin", nullptr));
        pushButton_cos->setText(QCoreApplication::translate("MainWindow", "cos", nullptr));
        pushButton_tg->setText(QCoreApplication::translate("MainWindow", "tg", nullptr));
        pushButton_ctg->setText(QCoreApplication::translate("MainWindow", "ctg", nullptr));
        error->setText(QString());
        pushButton_clearh->setText(QCoreApplication::translate("MainWindow", "C history", nullptr));
        pushButton_back->setText(QCoreApplication::translate("MainWindow", "<-", nullptr));
        pushButton_sqrt->setText(QCoreApplication::translate("MainWindow", "sqrt", nullptr));
        pushButton_ln->setText(QCoreApplication::translate("MainWindow", "log", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
