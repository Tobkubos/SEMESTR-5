#include <iostream>
#include <vector>
#include <random>

using namespace std;

void TestP(const vector<double>& weights, const vector<vector<int>>& TestVector, int idx) {

    double x = 0;
    double y = 0;
    for (int i = 0; i < TestVector[idx].size(); i++) {
        x += TestVector[idx][i] * weights[i];
    }
    y = 1. / (1. + exp(-x));

    cout << "TEST DLA " << idx << "  " << y << endl;
}

void Learn(const vector<vector<int>>& p, int Cmax, double Emax, double learning_rate, const vector<int>& t, const vector<vector<int>>& testp, int textIdx) {

    mt19937 rng(random_device{}());
    uniform_real_distribution<double> dist(-1.0, 1.0);
    vector<double> weights;
    // Inicjalizacja wag
    for (int q = 0; q < p[0].size(); q++) {
        weights.push_back(dist(rng));
    }


    int c = 0; // licznik

    while (c < Cmax) {
        double E = 0; // Error

        std::vector<int> order = { 0, 1 };
        std::random_shuffle(order.begin(), order.end());
        //cout << order[0] << " " << order[1] << endl;
        for (int q = 0; q < 2; q++) { // Iteracja po losowej kolejności
            int obrazP = order[q];
            double x = 0;

            for (int i = 0; i < p[obrazP].size(); i++) {
                x += p[obrazP][i] * weights[i];
            }

            double y = 1. / (1. + exp(-x)); //sigmoidalna

            // Aktualizacja wag
            for (int i = 0; i < weights.size(); i++) {
                weights[i] = weights[i] + learning_rate * (t[obrazP] - y) * y * (1 - y) * p[obrazP][i];
            }

            // Obliczanie błędu
            E += pow(t[obrazP] - y, 2) / 2;
        }

        c++; // epoka++

        if (E < Emax) {
            //cout << "Uczenie zakończone po " << c << " epokach. Błąd: " << E << endl;
            break;
        }
    }

    if (c == Cmax) {
        //cout << "Osiągnięto maksymalną liczbę epok. Końcowy błąd: " << Emax << endl;
    }


   /* cout << "WAGI" << endl;
    for (int q = 0; q < weights.size(); q++) {
        cout << q << " " << weights[q] << endl;
    }*/

    TestP(weights, testp, textIdx);
    //TestP(weights, testp, 1);
    weights.clear();
}

int main() {
    vector<vector<int>> p = { {
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1}, // p1 = A
        {
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 1, 1, 1, 1} // p2 = C
    };

    vector<int> t = { 0, 1 };

    vector<vector<int>> testp = { {
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 1}, // testp1 = A
        {
        1, 1, 1, 1, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 0, 0, 1, 1} // testp2 = C
    };

    double learning_rate = 0.001;
    double Emax = 0.01; // error
    int Cmax = 20000; // epochs


    //testowanie dla A
    for (int i = 0; i < 7; ++i) {
        Learn(p, Cmax, Emax, learning_rate, t, testp, 0);
    }

    cout << endl;
    //testowanie dla C
    for (int i = 0; i < 7; ++i) {
        Learn(p, Cmax, Emax, learning_rate, t, testp, 1);
    }



    return 0;
}