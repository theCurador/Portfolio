#include <iostream>
#include <cstdlib>
#include <ctime>
#include <time.h>
#include <string>

using namespace std;

int letterFill(char, string, string&);

int main() {
	//variables
	bool intento_inicial = true;
	//variable de intentos
	const int MAX_TRIES = 3;
	int numero_de_intentos = 0;
	//palabras educacion caridad averiguao palmolive presentao
	string word;
	string words[] = { "educacion" , "confirmar" , "averiguao" ,"palmolive" , "presentao", };
	int a;
	char letter;

	//_________________________________________________________________________________________________


	cout << " bienvenidos al hangman" << endl;
	cout << "__________________" << endl;
	cout << "| 1. educacion   |" << endl;
	cout << "| 2. confirmar   |" << endl;
	cout << "| 3. averiguao   |" << endl;
	cout << "| 4. palmolive   |" << endl;
	cout << "| 5. presentao   |" << endl;
	cout << "__________________" << endl;
	cout << "que palabra deseas adivinar?" << endl;
	cin >> a;

	
	system("CLS");
	//_____________________________________________________
	
	int n = rand() % 10;
	word = words[n];
	string unknown(words[n].length(), '*');
	//___________________________________________________________

	while (numero_de_intentos < MAX_TRIES)
	{
		cout << "te creistess que te iba a dar la palabra numero " << a << endl;
		cout << "\n\n" << unknown;
		cout << "\n\n Adivina la letra please: ";
		cin >> letter;
		//_____________________________________________________
		if (letterFill(letter, word, unknown) == 0)
		{
			cout << endl << "eso no va ahi sorry!" << endl;
			numero_de_intentos++;
		}
		//__________________________________________________________________________
		else
		{
			cout << endl << "ESOOOO EHHHHH PUERTO RICO PUERTO RICO!" << endl;
		}
		// _____________________________________________________________________
		cout << "hasta el momento te quedan " << MAX_TRIES - numero_de_intentos;
		cout << " intentos." << endl;
		// ______________________________________________________________________
		if (word == unknown)
		{
			cout << word << endl;
			cout << "me quito el sombrero tramposo!";
			break;
		}
	}
	//_______________________________________________________
	if (numero_de_intentos == MAX_TRIES)
	{
		cout << "\nSorry, perdiste no lo lograstes hahaha." << endl;
		cout << "la palabra era : " << word << endl;
	}
	cin.ignore();
	cin.get();
	system("pause");
}

int letterFill(char guess, string secretword, string &guessword)
{

	int i;
	int matches = 0;
	int len = secretword.length();
	for (i = 0; i< len; i++)
	{
		// ____________________________________________
		if (guess == guessword[i])
			return 0;
		// ______________________________________________
		if (guess == secretword[i])
		{
			guessword[i] = guess;
			matches++;
		}
	}
	return matches;
}





