def findEle(arr, l, h, targetValue):
    while l <= h:
        mid = l + (h-l) // 2

        if arr[mid] == targetValue:
            return mid
        elif arr[mid] < targetValue:
            l = mid + 1
        else:
            h = mid - 1
    return -1

if __name__ == '__main__':
    inputArr = [1,2,3,4,5,6,7,8,9,0]
    targetElement = 6
    s = len(inputArr)

    idx = findEle(inputArr, 0, s - 1, targetElement)

    if idx != -1:
        print("El elemento se encuentra en la posicion: " + str(idx + 1))
    else:
        print("El elemento no se encuentra")