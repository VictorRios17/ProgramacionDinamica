public class RecorridoLineal {

    
    public static int numeros(int[] input, int log, int targetEle) {
        for (int j = 0; j < log; j++) {
            if (input[j] == targetEle) {
                return j;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arreglo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int encontrar = 6;

        int log = arreglo.length; 

        
        int idx = numeros(arreglo, log, encontrar);

        if (idx != -1) {
            System.out.println("El elemento se encuentra en la posicion: " + idx);
        } else {
            System.out.println("Tu elemento no se encuentra.");
        }
    }
}
