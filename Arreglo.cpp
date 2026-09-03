#include <iostream>

using namespace std;

int main(){
     
    int arreglo [7] = {1, 2, 3, 4, 5, 6, 7};
    
    
    for (int i = 0; i < 7; i++) {
        cout << arreglo[i] << " ";
    }
    return 0;
}

//tarde un poco mas por que ponia directamente esto de imprimirlo
//osea un cout << arreglo; y me salia error hasta que busque que pasaba y es 
//por que el for se ocupa para estos casos