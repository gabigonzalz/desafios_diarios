#include <iostream> // libreria de entrada y salida

using namespace std;

int main(){

    // Suma de dos numeros en C++
    int numero1, numero2, suma;

    // Pedimos al usuario dos numeros
    cout << "Ingrese un numero: " << endl;
    cin >> numero1;

    cout << "Ingrese otro numero: " << endl;
    cin >> numero2;

    // Sumamos los numeros
    suma = numero1 + numero2;

    // Imprimimos el resultado
    cout << "La suma de " << numero1 << " y " << numero2 << " es: " << suma << endl;

    return 0;
}