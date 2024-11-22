#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <stack>
#include <sstream>
#include <cctype>
#include <math.h>

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

    void on_pushButton_0_clicked();
    void on_pushButton_1_clicked();
    void on_pushButton_2_clicked();
    void on_pushButton_3_clicked();
    void on_pushButton_4_clicked();
    void on_pushButton_5_clicked();
    void on_pushButton_6_clicked();
    void on_pushButton_7_clicked();
    void on_pushButton_8_clicked();
    void on_pushButton_9_clicked();

    void on_pushButton_plus_clicked();
    void on_pushButton_substract_clicked();
    void on_pushButton_multiply_clicked();
    void on_pushButton_divide_clicked();
    void on_pushButton_calc_clicked();

    void on_pushButton_del_clicked();

    void on_pushButton_sin_clicked();
    void on_pushButton_cos_clicked();
    void on_pushButton_tg_clicked();
    void on_pushButton_ctg_clicked();

    //void on_pushButton_percentage_clicked();
    void on_pushButton_abs_clicked();
    void on_pushButton_pow_clicked();

    //void ResetCalculator(QString errorMessage);
    //void ClearStacks();

private:
    Ui::MainWindow *ui;
    QString calculatorString;
    std::stack<char> operators;
    std::stack<double> numbers;
    std::stringstream ss;
    double wynikDouble;
};
#endif // MAINWINDOW_H
