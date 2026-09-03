inputArr= [1, 2, 3, 4, 5, 6 ,7 ,8]
#posiciones:0, 1, 2, 3,4, 5, 6, 7
posicion = 3

print("Ante de la eliminacion el arreglo es: ")
for j in range (len(inputArr)): #saber que j empieza en 0 y cubre hasta el rango 8 que es el rango del arreglo 
    print (inputArr[j], end= " ") #imprime el valor de j que empieza con 0 pero se le va sumando 1 asi que se imprime el valor ahi que es 1 y se detendra hasta que llegue al rango 8  
del inputArr[posicion] #elimina en el arreglo la posicion 3 que seria el num 4
print("\nDespues de la eliminacion , el array es: ") 
for j in range(len(inputArr)): #aqui hara lo mismo de que imprimira j perooo esta ves siendo eliminado el 4 
    print(inputArr[j], end=" ") # end = " " signfica que cada salto que de le ponga un espacio entre esos numeros de j 