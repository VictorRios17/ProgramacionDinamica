def elementos(inpuptArr, s, targetEle):
    for j in range(s):
        if(inpuptArr[j] == targetEle):
            return j 

    return -1
if __name__ == '__main__':
    inpuptArr = [1,2,3,4,5,6,7,8,9,0]
    targetElement = 6
    s = len(inpuptArr)

    idx = elementos(inpuptArr, s, targetElement)
    if idx != -1:
        print("El elemento se encuentra en la posicion: " + str(idx + 1))
    else:
        print("No se encuentra el elemento")