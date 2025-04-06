public class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    
    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10 && numero % 2 == 0) {
            return true;
        }
        System.out.println("numero invalido, Debe ser un numero par entre 0 y 10");
        return false;
    }
}

