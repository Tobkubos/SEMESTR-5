#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QString"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    ,calculatorString()
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_1_clicked()
{
    calculatorString += "1";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_2_clicked()
{
    calculatorString += "2";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_3_clicked()
{
    calculatorString += "3";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_4_clicked()
{
    calculatorString += "4";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_5_clicked()
{
    calculatorString += "5";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_6_clicked()
{
    calculatorString += "6";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_7_clicked()
{
    calculatorString += "7";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_8_clicked()
{
    calculatorString += "8";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_pushButton_9_clicked()
{
    calculatorString += "9";
    ui->lcdNumber->display(calculatorString);
}

void MainWindow::on_lcdNumber_overflow()
{

}





