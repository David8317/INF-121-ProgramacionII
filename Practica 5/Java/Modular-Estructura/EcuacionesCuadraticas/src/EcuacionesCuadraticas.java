import java.util.Scanner;
//Modular-Estructura
public class EcuacionesCuadraticas {
    public static double getDiscriminante(double a, double b, double c) {
        return (b * b) - (4 * a * c);
    }

    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        scanner.close();

        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            System.out.println("La ecuación tiene dos raíces: " + getRaiz1(a, b, discriminante) + " y " + getRaiz2(a, b, discriminante));
        } else if (discriminante == 0) {
            System.out.println("La ecuación tiene una raíz: " + getRaiz1(a, b, discriminante));
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }
}
