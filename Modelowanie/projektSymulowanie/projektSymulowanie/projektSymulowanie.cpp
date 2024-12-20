
#include <iostream>
#include <random>
#include <vector>
#include <algorithm> 

using namespace std;

int main()
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> disStart(3, 15); //ilosc maszyn
    std::uniform_real_distribution<> dis1(75, 100); //jakosc maszyn
    std::normal_distribution<> dis2(100, 10); //predkosc maszyn

    std::normal_distribution<> StartProd(90, 10);

    std::discrete_distribution<> d({ 5, 8, 12, 75 }); //oba defekty, funkcjonalny, kosmetyczny, brak defektu

    std::normal_distribution<> pd1(10,2);             //poprawa jakosci kiedy defekt kosmetyczny i funkcyjny
    std::normal_distribution<> pd2(5,1.5);            //poprawa jakosci kiedy defekt funkcyjny
    std::normal_distribution<> pd3(2,1);              //poprawa jakosci kiedy defekt kosmetyczny

    //ETAP 1 - LOSOWANIE ILOSCI MASZYN DO WYPRODUKOWANIA PRODUKTU
    int numOfMachines = disStart(gen);

    //ETAP 2 - LOSOWANIE JAKOSCI MASZYN W PROCESIE PRODUKCJI PRODUKTU
    vector<double> machinesQuality;
    for (int j = 0; j < numOfMachines; j++) {
        double r1 = dis1(gen);
        machinesQuality.push_back(r1);
        //cout << r1 << endl;
    }

    //ETAP 3 - LOSOWANIE PREDKOSCI PRACY MASZYN W PROCESIE PRODUKCJI PRODUKTU
    vector<double> machinesSpeed;
    for (int j = 0; j < numOfMachines; j++) {
        double r2 = dis2(gen);
        machinesSpeed.push_back(r2);
        //cout << r2 << endl;
    }

    //obliczanie wspolczynnika skutecznosci maszyn
    double maxQuality = *std::max_element(machinesQuality.begin(), machinesQuality.end());
    double maxSpeed = *std::max_element(machinesSpeed.begin(), machinesSpeed.end());
    double efficiencyFactor = 0;

    for (int j = 0; j < numOfMachines; j++) {
        efficiencyFactor += (machinesQuality[j] + machinesSpeed[j]) / (maxQuality + maxSpeed);
        //cout << efficiencyFactor << endl;
    }
    efficiencyFactor = efficiencyFactor / numOfMachines;

    for (int i = 0; i < 5000; i++) {
        //ETAP 4 - LOSOWANIE STARTOWEJ JAKOSCI PRODUKTU
        double product = StartProd(gen);
        product *= efficiencyFactor;

        //ETAP 5 - LOSOWANIE CZY PRODUKT JEST USZKODZONY - KONTROLA JAKOSCI
        int isFix = d(gen);
        double f1 = 0, f2 = 0, f3 = 0;
        switch (isFix)
        {
        case 0:
            f1 = pd1(gen);
            product -= f1;
            break;
        case 1:
            f2 = pd2(gen);
            product -= f2;
            break;
        case 2:
            f3 = pd3(gen);
            product -= f3;
            break;
        case 3:
            break;
        }
        cout << product << " ";
    }
}
