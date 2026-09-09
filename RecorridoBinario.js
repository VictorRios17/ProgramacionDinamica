
function findEle(arr, l, h, targetValue) {
    while (l <= h) {
        
        let mid = Math.floor(l + (h - l) / 2);

        if (arr[mid] === targetValue) {
            return mid;
        }
        
        else if (arr[mid] < targetValue) {
            l = mid + 1;
        }
      
        else {
            h = mid - 1;
        }
    }
    return -1; 
}


const inputArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]; 
const targetElement = 3;
const s = inputArr.length;

const idx = findEle(inputArr, 0, s - 1, targetElement);

if (idx !== -1) {
    console.log("El elemento se encuentra en la posición: " + (idx + 1));
} else {
    console.log("El elemento no se encuentra.");
}