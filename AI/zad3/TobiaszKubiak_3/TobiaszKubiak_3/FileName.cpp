//#include <iostream>
//#include <random>
//#include <cmath>
//
//double f(double x);
//void Network(int*);
//
//using namespace std;
//
//class DataPack
//{
//public:
//	DataPack()
//	{
//		p = nullptr;
//		t = 0;
//	}
//	DataPack(int* pin, int tin)
//	{
//		p = pin;
//		t = tin;
//	}
//
//	int* p;
//	int t;
//};
//
//int main()
//{
//	int t1[35] = { 0,1,0,1,1,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					0,0,0,0,0,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					1,1,1,0,0 };
//
//	int t2[35] = { 1,0,1,1,0,
//					0,0,0,0,1,
//					0,0,0,0,1,
//					1,1,0,1,0,
//					1,0,0,0,1,
//					0,0,0,0,1,
//					1,0,0,0,0 };
//
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//	Network(t1);	//0
//
//	Network(t1);	//0
//
//	int x;
//	cin >> x;
//	return 0;
//}
//
//double f(double x)
//{
//	return (1. / (1 + exp(-x)));
//}
//
//void Network(int* test)
//{
//	mt19937 rng(random_device{}());
//	uniform_real_distribution<double> dist(-1.0, 1.0);
//
//	const int ins = 35;
//	const double Emax = 0.0001;
//	const double Cmax = 2000;
//	const double N = 0.01;
//	double C = 0;
//	double E = 0;
//
//	//Zestawy testowe l=[p,t]
//	int l = 2;
//	int i = 0;
//	int p1[ins] = { 1,1,1,1,1,
//					1,0,0,0,1,
//					1,0,0,0,1,
//					1,1,1,1,1,
//					1,0,0,0,1,
//					1,0,0,0,1,
//					1,0,0,0,1 };
//
//	int p2[ins] = { 1,1,1,1,1,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					1,0,0,0,0,
//					1,1,1,1,1 };
//
//	DataPack L1(p1, 1);
//	DataPack L2(p2, 0);
//
//	//wagi
//	double w[ins];
//	double wp[ins];
//	for (int i = 0; i < ins; i++)
//	{
//		wp[i] = dist(rng);
//	}
//
//
//	C = 0;
//
//	//nauka
//	for (int cycle = 0; cycle < Cmax; cycle++)
//	{
//		E = 0;
//		i = 0;
//		DataPack* packs = new DataPack[2];
//		if (rand() % 2 == 0)
//		{
//			packs[0] = L1;
//			packs[1] = L2;
//		}
//		else
//		{
//			packs[0] = L2;
//			packs[1] = L1;
//		}
//
//		for (int img = 0; img < l; img++)
//		{
//
//			//przeklejam tablice
//			for (int i = 0; i < ins; i++)
//			{
//				w[i] = wp[i];
//			}
//
//			//sumuje
//			double x = 0;
//			for (int i = 0; i < ins; i++)
//			{
//				x += w[i] * packs[img].p[i];
//			}
//			double y = f(x);	//funkcja aktywacji
//
//			//poprawka wag
//			for (int i = 0; i < ins; i++)
//			{
//				wp[i] = w[i] + N * (packs[img].t - y) * (1 - y) * y * packs[img].p[i];
//			}
//
//			//warunki
//			E += (pow((packs[img].t - y), 2)) / 2;
//			if (E < Emax)
//			{
//				cout << "Training converged at cycle: " << cycle << endl;
//				break;
//			}
//		}
//	}
//
//	//test
//	double x = 0;
//	for (int i = 0; i < ins; i++)
//	{
//		x += w[i] * test[i];
//	}
//	double y = f(x);	//funkcja aktywacji
//	cout << "Wynik testu to: " << y << endl << endl;
//}