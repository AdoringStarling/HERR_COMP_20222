#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

/* Corchetes en c++ cambia a indentacion en python
cout equivalente a print en la consola
recordar colocar ;
funcion main retorna un entero, en este caso 0*/

//Declaro la funcion
//void fprima();
//en la funcion principal uno llama las otras
//void fprima(int a,int b){
//    return pow(a, b);
double myFunction(double mivarflotante,int mivarentera) {
    return pow(mivarflotante,mivarentera);
  // code to be executed
}

//}
int main(){
    //1.Inicializar dos variables globales (con valores escogidos por ustedes), una entera y otra flotante.
    int x = 2;
    double y= 2.21;
    //2. Imprimir los valores de las variables en un mensaje: "la primera tiene un valor de XX y la segunda variable tiene un
    //valor de YY"
    cout << "La primera tiene un valor de "<<x<<"y la segunda variable tiene un valor de "<<y ;
    //Calcular el valor de la segunda variable dividida por la primera e imprimir : "El resultado es ZZ"
    double z=x/y;
    cout << "\nEl resultado es "<<z<<"\n";
    srand(time(NULL));
  //  int arr[] = new int[300]
  //  unsigned int arr_length = 0;
  //  std::vector< int > arr;
    int arr1[300] = {};
    for (int i = 0; i < 300; i++)
        arr1[i]=rand()% 900 + 0;
        //arr.push_back(rand()% 900 + 0);
        //arr[arr_length++] = rand()% 900 + 0;
        //cout << rand()% 900 + 0 << " ";
    //int *arr1 = &arr[0];
    for (int i = 0; i < 300; i++) {
       cout << arr1[i] << "\n";}
    cout << "Quinto elemento del arreglo: " << arr1[5] <<"\n";
    cout << "La longitud del arreglo es: " << sizeof(arr1)/ sizeof(int) <<"\n";
    //Haga una función que reciba dos variables una flotante llamada mivarflotante y una entera llamada mivarentera
    double a= 17.5;
    int b=5 ;
    cout << a <<"^"<<b<<"==" <<myFunction(a,b);
    int n = sizeof(arr1) / sizeof(arr1[0]);
    cout << "\nMin Element = "
         << *min_element(arr1, arr1 + n)<<"\n";
    for (int i = 0; i < 300; i++) {
        if (arr1[i]%2!=0){
            cout << arr1[i]<<"\n";
            if (arr1[i]>=800){
            break;}
        }        
        else if (arr1[i]>=800){
            break;
        }
    };
    return 0;
    }
    
/* Mas control en el codigo (por ejemplo, en la variable)
tipos de datos en c++*/

