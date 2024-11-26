#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QString"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    ,calculatorString()
    ,operators()
    ,numbers()
    ,ss()
    ,wynikDouble()
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
    wynikDouble = 0;
}


double makeOperation(double a, double b, char operation){
    if(operation == '+'){
        return a + b;
    }

    if(operation == '-'){
        return a - b;
    }

    if(operation == '/'){
        return a / b;
    }

    if(operation == '*'){
        return a * b;
    }

    if(operation == '^'){
        return pow(a, b);
    }

    return 0;
}

bool isOperator(char o){
    if(o == '+' || o == '-' || o == '*' || o == '/' || o == '^'){
        return true;
    }
    return false;
}

int operatorImportance(char o){
    if(o == '+' || o == '-')
        return 1;
    if(o == '*' || o == '/')
        return 2;
    if(o == '^')
        return 3;
    return 0;
}

void MainWindow::on_pushButton_calc_clicked()
{
    ss.str("");
    ss.clear();
    ss << calculatorString.toStdString();

    if (calculatorString.trimmed().isEmpty()) {
        //ui->error->setText("brak wyrażenia");
        clearDisplay = true;
        return;
    }

    if (calculatorString.length() == 1) {
        char singleNumber = calculatorString[0].toLatin1();
        if (isdigit(singleNumber)) {
            double number = singleNumber - '0';
            numbers.push(number);
            wynikDouble = number;
            ui->wynik->setText(QString::number(number));
            if (showResultInHistory) {
                ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(number) + "\n");
            }
        } else {
            ui->error->setText("niepoprawne wyrażenie");
        }
        clearDisplay = true;
        return;
    }

    if(calculatorString[calculatorString.length()-2] == '-' ||
        calculatorString[calculatorString.length()-2] == '+' ||
        calculatorString[calculatorString.length()-2] == '/' ||
        calculatorString[calculatorString.length()-2] == '*' ||
        calculatorString[calculatorString.length()-2] == '^'){
        ui->error->setText("błąd");
        wynikDouble = 0;
        calculatorString.clear();
        ui->wynik->setText(calculatorString);
        clearDisplay = true;
        return;
    }

    std::string t;
    while (getline(ss, t, ' ')) {
        if (t.empty())
            continue;

        qDebug() << "Fragment stringa (t):" << QString::fromStdString(t);

        if ((t[0] == '-' && t.length() > 1 && isdigit(t[1])) || isdigit(t[0])) {
            double number;
            std::stringstream(t) >> number;
            numbers.push(number);
        }
        else if (isOperator(t[0])) {
            char oprtr = t[0];

            while (!operators.empty() && operatorImportance(operators.top()) >= operatorImportance(oprtr)) {
                if (numbers.size() < 2) {
                    ui->error->setText("niepoprawne działanie");
                    wynikDouble = 0;
                    calculatorString.clear();
                    ui->wynik->setText(calculatorString);
                    clearDisplay = true;
                    return;
                }

                double b = numbers.top();
                numbers.pop();
                double a = numbers.top();
                numbers.pop();
                char topOprtr = operators.top();
                operators.pop();

                if (topOprtr == '/' && b == 0) {
                    ui->error->setText("dzielenie przez 0!");
                    calculatorString.clear();
                    ui->wynik->setText(calculatorString);
                    clearDisplay = true;
                    return;
                }

                numbers.push(makeOperation(a, b, topOprtr));
            }
            operators.push(oprtr);
        }
    }

    while(!operators.empty()){

        if (numbers.size() < 2) {
            ui->error->setText("niepoprawne dzialanie");
            //wynikDouble = 0;
            calculatorString.clear();
            ui->wynik->setText(calculatorString);
            clearDisplay = true;
            return;
        }

        double b = numbers.top();
        numbers.pop();
        double a = numbers.top();
        numbers.pop();
        char oprtr = operators.top();
        operators.pop();

        if (oprtr == '/' && b == 0) {
            ui->error->setText("dzielenie przez 0!");
            calculatorString.clear();
            ui->wynik->setText(calculatorString);
            clearDisplay = true;
            return;
        }
        numbers.push(makeOperation(a,b,oprtr));
    }

    if(!numbers.empty()){
        wynikDouble = numbers.top();
    }else{
        wynikDouble = 0;
    }


    ui->wynik->setText(QString::number(wynikDouble));

    if(showResultInHistory){
      ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    }

    calculatorString = QString::number(wynikDouble);
}



void MainWindow::on_pushButton_sin_clicked()
{
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "sin( " + QString::number(wynikDouble) + " )";
    wynikDouble = sin(wynikDouble);

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    calculatorString = QString::number(wynikDouble);
    ui->wynik->setText(calculatorString);
    wynikDouble = 0;
    showResultInHistory = true;
}

void MainWindow::on_pushButton_cos_clicked()
{
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "cos( " + QString::number(wynikDouble) + " )";
    wynikDouble = cos(wynikDouble);

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    calculatorString = QString::number(wynikDouble);
    ui->wynik->setText(calculatorString);
    wynikDouble = 0;
    showResultInHistory = true;
}

void MainWindow::on_pushButton_tg_clicked()
{
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "tg( " + QString::number(wynikDouble) + " )";
    wynikDouble = tan(wynikDouble);

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    calculatorString = QString::number(wynikDouble);
    ui->wynik->setText(calculatorString);
    wynikDouble = 0;
    showResultInHistory = true;
}

void MainWindow::on_pushButton_ctg_clicked()
{
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "ctg( " + QString::number(wynikDouble) + " )";
    wynikDouble = 1 / tan(wynikDouble);

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    calculatorString = QString::number(wynikDouble);
    ui->wynik->setText(calculatorString);
    wynikDouble = 0;
    showResultInHistory = true;
}

void MainWindow::on_pushButton_abs_clicked()
{
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "| " + QString::number(wynikDouble) + " |";
    wynikDouble = abs(wynikDouble);

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(wynikDouble) + "\n");
    calculatorString = QString::number(wynikDouble);
    ui->wynik->setText(calculatorString);
    wynikDouble = 0;
    showResultInHistory = true;
}

void MainWindow::on_pushButton_del_clicked()
{
    calculatorString.clear();
    calculatorString = "";
    wynikDouble = 0;

    ui->wynik->clear();
    ui->wynik->setText(calculatorString);
    while(operators.empty() == false){
        operators.pop();
    }
    while(numbers.empty() == false){
        numbers.pop();
    }
}

void MainWindow::on_pushButton_0_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "0";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_1_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "1";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_2_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "2";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_3_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "3";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_4_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "4";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_5_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "5";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_6_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "6";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_7_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "7";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_8_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "8";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_9_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "9";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_dot_clicked()
{
        MainWindow::ClearErrorContent();

        QRegularExpression re("[+\\-*/^ ]");
        int lastOperatorIndex = calculatorString.lastIndexOf(re);

        QString currentNumber = calculatorString.mid(lastOperatorIndex + 1);

        if (currentNumber.contains(".")) {
            return;
        }
        if (currentNumber.isEmpty()) {
            calculatorString += "0.";
        } else {
            calculatorString += ".";
        }

        ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_plus_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += " + ";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_substract_clicked()
{
    if (calculatorString.isEmpty() || calculatorString.endsWith(" ")) {
        calculatorString += "-";
    } else {
        calculatorString += " - ";
    }
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_divide_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += " / ";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_multiply_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += " * ";
    ui->wynik->setText(calculatorString);
}

void MainWindow::on_pushButton_pow_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += " ^ ";
    ui->wynik->setText(calculatorString);
}


void MainWindow::ClearErrorContent(){
    if(clearDisplay){
        ui->error->setText("");
        calculatorString = "";
        wynikDouble = 0;
        ui->wynik->setText(calculatorString);
        clearDisplay = false;
    }
}



void MainWindow::on_pushButton_clearh_clicked(){
    ui->historia->setText("");
}


