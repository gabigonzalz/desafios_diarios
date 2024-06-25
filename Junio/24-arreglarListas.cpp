/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    // Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)
    
    // Creamos un array (lista)
    int miLista[] = { 5, 4, 1, 2, 3 };

    // Imprimimos la lista antes de arrgelar
    cout << "Mi lista antes de arreglar: ";
    for (int i = 0; i < 5; i++) {
        cout << miLista[i] << " ";
    }
    
    cout << endl;

    // Arreglamos la lista con sort() de la libreria algorithm
    sort(miLista, miLista + 5);

    // Imrimimos la lista despues de haberla arreglada
    cout << "Mi lista despues de arreglar: ";
    for (int i = 0; i < 5; i++) {
        cout << miLista[i] << " ";
    }
    
    cout << endl;

    return 0;
}