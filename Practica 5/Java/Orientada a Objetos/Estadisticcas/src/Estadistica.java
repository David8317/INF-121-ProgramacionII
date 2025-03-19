import java.util.Scanner;
//Programacion Orientada a Objetos.
class Estadisticas {
    private double[] numeros;

    public Estadisticas(double[] numeros) {
        this.numeros = numeros;
    }

    public double getPromedio() {
        double suma = 0;
        for (double num : numeros) suma += num;
        return suma / numeros.length;
    }

    public double getDesviacion() {
        double promedio = getPromedio();
        double suma = 0;
        for (double num : numeros) suma += Math.pow(num - promedio, 2);
        return Math.sqrt(suma / (numeros.length - 1));
    }

    public void mostrarResultados() {
        System.out.println("El promedio es " + getPromedio());
        System.out.println("La desviación estándar es " + getDesviacion());
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];
        System.out.print("Ingrese 10 números: ");
        for (int i = 0; i < 10; i++) numeros[i] = scanner.nextDouble();
        scanner.close();

        Estadisticas estadisticas = new Estadisticas(numeros);
        estadisticas.mostrarResultados();
    }
}
