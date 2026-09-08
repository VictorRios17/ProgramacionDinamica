#include <iostream>

using namespace std;

int numeros(int input[], int s, int targetEle){
   for(int j = 0; j < s; j++) {
    if(input[j] == targetEle) {
        return j;
    }
   }
   return -1;
}

   int main(){
   
   int arreglo[10] = {1,2,3,4,5,6,7,8,9,0};
   int encontrar = 6;
   int log = sizeof(arreglo) / sizeof(arreglo[0]);
   
   int idx = numeros(arreglo, log, encontrar);
   
   if(idx != -1) {
    cout << "El elemento se encuentra en la posicion: " << idx << endl; 
   }else {
    cout << "El numero no se encuentra" << endl;
   }
   
   return 0;
}