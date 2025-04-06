import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juego2 = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juego3 = new JuegoAdivinaImpar(3);

        System.out.println("Juego de adivinanza numeros");
        juego1.juega(scanner);
        
        System.out.println("Juego de adivinanza de numeros pares");
        juego2.juega(scanner);
        
        System.out.println(" Juego de adivinanza de numeros impares");
        juego3.juega(scanner);
        
        scanner.close();
    }
}
