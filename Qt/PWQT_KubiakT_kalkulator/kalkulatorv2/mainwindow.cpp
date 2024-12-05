#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    ,calculatorString()
    ,operators()
    ,numbers()
    ,ss()
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
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

bool isOperator(QChar o){
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
            ui->wynik->setText(QString::number(number));
            if (showResultInHistory) {
                ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(number) + "\n");
            }
        } else {
            ui->error->setText("niepoprawne wyrażenie");
            calculatorString.clear();
            ui->wynik->setText(calculatorString);
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
        calculatorString.clear();
        ui->wynik->setText(calculatorString);
        clearDisplay = true;
        return;
    }

    std::string t;
    while (getline(ss, t, ' ')) {
        if (t.empty())
            continue;

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
        ui->wynik->setText(QString::number(numbers.top()));
    }else{
        //calculatorString.clear();
        //ui->wynik->setText(calculatorString);
    }


    ui->wynik->setText(QString::number(numbers.top()));

    if(showResultInHistory){
        ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    }

    calculatorString = QString::number(numbers.top());
}



void MainWindow::on_pushButton_sin_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "sin( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(sin(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_cos_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "cos( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(cos(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_tg_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "tg( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(sin(numbers.top()) / cos(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_ctg_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "ctg( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(cos(numbers.top()) / sin(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_abs_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "| " + QString::number(numbers.top()) + " |";
    wynik = QString::number(abs(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}


void MainWindow::on_pushButton_log_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "log( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(log10(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_ln_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "ln( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(log(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}


void MainWindow::on_pushButton_sqrt_clicked()
{
    QString wynik;
    MainWindow::ClearErrorContent();
    showResultInHistory = false;
    MainWindow::on_pushButton_calc_clicked();
    calculatorString = "sqrt( " + QString::number(numbers.top()) + " )";
    wynik = QString::number(sqrt(numbers.top()));
    numbers.pop();
    numbers.push(wynik.toDouble());

    ui->historia->setText(ui->historia->text() += calculatorString + " = " + QString::number(numbers.top()) + "\n");
    calculatorString = QString::number(numbers.top());
    ui->wynik->setText(calculatorString);
    showResultInHistory = true;
}

void MainWindow::on_pushButton_del_clicked()
{
    calculatorString.clear();
    ui->wynik->setText(calculatorString);
    while(operators.empty() == false){
        operators.pop();
    }
    while(numbers.empty() == false){
        numbers.pop();
    }
}

void MainWindow::on_pushButton_back_clicked()
{
    if(!calculatorString.isEmpty()){
        if(isOperator(calculatorString.back()) || calculatorString.back() == " "){
            while(isOperator(calculatorString.back()) || calculatorString.back() == " "){
                calculatorString.removeLast();
            }
        }
        else if(calculatorString.size()>0){
            calculatorString.removeLast();
        }
        ui->wynik->setText(calculatorString);
    }
}
void MainWindow::on_pushButton_0_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "0";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;

}

void MainWindow::on_pushButton_1_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "1";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_2_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "2";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_3_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "3";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_4_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "4";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_5_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "5";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_6_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "6";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_7_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "7";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_8_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "8";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
}

void MainWindow::on_pushButton_9_clicked()
{
    MainWindow::ClearErrorContent();
    calculatorString += "9";
    ui->wynik->setText(calculatorString);
    IsLastOperation = false;
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
    if(!IsLastOperation){
        MainWindow::ClearErrorContent();
        calculatorString += " + ";
        ui->wynik->setText(calculatorString);
        IsLastOperation = true;
    }
}

void MainWindow::on_pushButton_substract_clicked()
{
    if(!IsLastOperation){
        if (calculatorString.isEmpty() || calculatorString.endsWith(" ")) {
            calculatorString += "-";
        } else {
            calculatorString += " - ";
        }
        ui->wynik->setText(calculatorString);
        IsLastOperation = true;
    }
}

void MainWindow::on_pushButton_divide_clicked()
{
    if(!IsLastOperation){
        MainWindow::ClearErrorContent();
        calculatorString += " / ";
        ui->wynik->setText(calculatorString);
        IsLastOperation = true;
    }
}

void MainWindow::on_pushButton_multiply_clicked()
{
    if(!IsLastOperation){
        MainWindow::ClearErrorContent();
        calculatorString += " * ";
        ui->wynik->setText(calculatorString);
        IsLastOperation = true;
    }
}

void MainWindow::on_pushButton_pow_clicked()
{
    if(!IsLastOperation){
        MainWindow::ClearErrorContent();
        calculatorString += " ^ ";
        ui->wynik->setText(calculatorString);
    IsLastOperation = true;
    }
}


void MainWindow::ClearErrorContent(){
    if(clearDisplay){
        ui->error->setText("");
        calculatorString.clear();
        ui->wynik->setText(calculatorString);
        clearDisplay = false;
        IsLastOperation = false;
    }
}



void MainWindow::on_pushButton_clearh_clicked(){
    ui->historia->setText("");
}


