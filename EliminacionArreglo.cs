using System;
using System.Globalization;
using System.Linq;

int [] numeros = {1, 2, 3, 4, 5}; //hacemos un arreglo 
int posicion = 3; //POSICION A ELIMINAR

Console.WriteLine("Tu arreglo antes de borrar la posicion seria: ");
for (int J = 0; J < numeros.Length; J++) //aqui me rompi la cabeza un poco por que el for es diferente a como es python pero sigue teniendo las mismas parte 
{

    Console.WriteLine(numeros[J]);
    

}
numeros = numeros.Where(x => x != posicion).ToArray(); //aqui estuve buscando como eliminarlo como si fuera en python solo que no hace la misma manera ya que 
//NO SOLO ES DEL y listo Where = un metodo en LINQ que filtra una coleccion x = es cada numero del arreglo  != es una condicion que x sea diferente a posicion entonces lo imprime
//.Toarray funciona como regresa el arreglo a un tipo int ya que where no lo regresa como tal cual es 
Console.WriteLine("El arreglo eliminando su posicion seria: ");

for(int j = 0; j < numeros.Length; j++)
{
    Console.WriteLine(numeros[j]);

}
