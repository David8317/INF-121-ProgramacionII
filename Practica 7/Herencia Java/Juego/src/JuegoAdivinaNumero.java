import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    
    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    
    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega(Scanner scanner) {
        reiniciaPartida();
        Random rand = new Random();
        numeroAAdivinar = rand.nextInt(11);

        System.out.println("adivina un numero entre 0 y 10");

        while (true) {
            int intento = scanner.nextInt();
            if (!validaNumero(intento)) {
                System.out.println("numero invalido, intenta de nuevo");
                continue;
            }
            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                break;
            } else {
                if (!quitaVida()) {
                    System.out.println("Has perdido, El numero era: " + numeroAAdivinar);
                    break;
                }
                System.out.println("numero incorrecto. " + (intento < numeroAAdivinar ? "es mayor." : "es menor."));
            }
        }
    }
}



