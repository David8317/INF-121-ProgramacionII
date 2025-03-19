import java.util.Scanner;
// #Modular-Estructura
public class Estadistica {
    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) suma += num;
        return suma / numeros.length;
    }

    public static double desviacion(double[] numeros, double promedio) {
        double suma = 0;
        for (double num : numeros) suma += Math.pow(num - promedio, 2);
        return Math.sqrt(suma / (numeros.length - 1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];
        System.out.print("Ingrese 10 números: ");
        for (int i = 0; i < 10; i++) numeros[i] = scanner.nextDouble();
        scanner.close();

        double prom = promedio(numeros);
        System.out.println("El promedio es " + prom);
        System.out.println("La desviación estándar es " + desviacion(numeros, prom));
    }
}
