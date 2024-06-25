#include <iostream>
#include <algorithm>
using namespace std;

bool esPalindromo(const std::string& str) {
    // eliminamos los espacios y convertimos a minusculas
    string procesada;
    for(char c : str) {
        if(c != ' ') {
            procesada += tolower(c);
        }
    }

    // comprobamos si la cadena procesada es igual a su reverso
    string reversa = procesada;
    reverse(reversa.begin(), reversa.end());

    return procesada == reversa; // devuelve true or false
}

int main()
{
    // Palíndromo: Escribir un programa que determine si una cadena 
    // de caracteres ingresada por el usuario es un palíndromo 
    // ¡Pero hazlo en C++! :)
    
    string input;
    cout << "Ingrese una cadena de caracteres: ";
    getline(cin, input);

    if(esPalindromo(input)) { // si es true
        cout << "La cadena es un palíndromo." << endl;
    } else { // si es falso
        cout << "La cadena no es un palíndromo." << endl;
    }

    return 0;
}