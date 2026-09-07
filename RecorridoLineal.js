function elementos(input, s, targetEle) {
    for (let j = 0; j < s; j++) {
        if (input[j] === targetEle) {
            return j;
        }
    }
    return -1;
}

let inputArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
let targetElement = 5;
let s = inputArr.length;

let idx = elementos(inputArr, s, targetElement);

if (idx !== -1) {
    console.log("El elemento se encuentra en la posicion: " + (idx + 1));
} else {
    console.log("No se encuentra el elemento");
}