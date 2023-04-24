#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*Tenemos que hacer una tienda similar a la de un juego.Lo primero debemos preguntar al usuario cuanto dinero tiene antes de entrar a la tienda
despues crer un menu desde el que poder comprar objetos de un juego, el menu tiene que permitir al usuario ver los objetos disponibles, 
cuantos hay y sus precios, debe haber una opcion para comprar los objetos y si ya no hay entonces no se le debe permitir comprarlo, 
tampoco si no le alcanza el dinero Ha de haber otra opcion para ver que hemos comprado, y por ultimo una opcion de salir*/

struct commisary_INV {
	
	struct COMMISARY_DRINKS {
		int water;
		int soda;
		int alcohol;
		int juice;
		};
	struct COMMISARY_SNACKS {
		int candy;
		int chips;
		int chocolate;
		int ice_cream;
		int popcorn;
	};
	bool MAYOR_de_EDAD;
	struct COMMISARY_ADULT {
		int adultmags;
		int beers;
		int whiskey;
		int wines;
		int ciggarettes;
		int chewing_tobacco;

	};
	


};



int main() {

	bool wanting = 1;
	float budget;

	cout << "Welcome to the commisary" << endl;
	cout << endl;

	cout << "do you want something from the store?" << endl;
	cin >> wanting;
	cout << endl;

	cout << "what's your budget?" << endl;
	cin >> budget;
	while (wanting == 1){
		
	


		cout << "do you need anything else?" << endl;
		cin >> wanting;

		cout << "what do you need?" << endl;
	}


	
	if (wanting != 1)
	{
		cout << "No Problem you can visit anytime" << endl;
		cout << endl;

	}




	system("pause");
}