using System;

 int busquedaL(int[] arr, int target)
{
    for(int i = 0; i < arr.Length; i ++)
    {
        if (arr[i] == target)
        {
            return i;
        }
    }
    return -1;

}

int[] numeros = [1,2,3,4,5,6,7,8,9];
int buscar = 2;
int indice = busquedaL(numeros, buscar);
if (indice != -1)
{
    Console.WriteLine($"El numero {buscar} esta en el indice: {indice}");
}
else
{
    Console.WriteLine($"El Numero {buscar} no se encuentra");
}

