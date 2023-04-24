#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <time.h>


using namespace std;

int main() {

	srand(time(NULL));
	string VARIABLE_INTERMITENTE;	
	int TUS_NUMEROS;
	int ARRAY_ENTRANTE[5];

	cout << " Bienvenido a la loteria electronica \n";
	cout << " \n";
	cout << " tienes que escoger 6 numeros, tienes desde el 1 hasta el 49 para escoger.. \n";
	cout << "FIRE AWAY \n";

	for (int i = 0; i < 6; i++)
	{
		cout << i + 1 << " # ";
		cin >> ARRAY_ENTRANTE[0];
		cin >> ARRAY_ENTRANTE[1];
		
		if (ARRAY_ENTRANTE[1] == ARRAY_ENTRANTE[0])
		{
			cout << "YA LO ESCRIBISTES TRY AGAIN";
			cin >> ARRAY_ENTRANTE[1];
		}
		cin >> ARRAY_ENTRANTE[2];
		if (ARRAY_ENTRANTE[2] == ARRAY_ENTRANTE[1] || ARRAY_ENTRANTE [2] == ARRAY_ENTRANTE [0])
		{
			cout << "YA LO ESCRIBISTES TRY AGAIN";
			cin >> ARRAY_ENTRANTE[2];
		}

	}
	cout << "tus numeros ganadores son : ";

	for (int a = 0; a < 6; a++)
	{
		
		cout << rand() % 49<<", ";
	}








	system("pause");
}