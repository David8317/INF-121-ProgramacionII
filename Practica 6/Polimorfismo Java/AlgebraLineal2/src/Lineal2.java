public class Lineal2 {
    private double x, y, z;

    public Lineal2(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Lineal2 sumar(Lineal2 otro) {
        return new Lineal2(this.x + otro.x, this.y + otro.y, this.z + otro.z);
    }

    public Lineal2 multiplicar(double escalar) {
        return new Lineal2(this.x * escalar, this.y * escalar, this.z * escalar);
    }

    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public Lineal2 normalizar() {
        double magnitud = this.magnitud();
        return new Lineal2(this.x / magnitud, this.y / magnitud, this.z / magnitud);
    }

    public double productoEscalar(Lineal2 otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }

    public Lineal2 productoVectorial(Lineal2 otro) {
        return new Lineal2(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }

    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }

    public static void main(String[] args) {
        Lineal2 a = new Lineal2(1, 2, 3);
        Lineal2 b = new Lineal2(4, 5, 6);

        System.out.println("a) Suma de vectores: " + a.sumar(b));
        System.out.println("b) Multiplicación por escalar (2): " + a.multiplicar(2));
        System.out.println("c) Magnitud de a: " + a.magnitud());
        System.out.println("d) Vector normalizado de a: " + a.normalizar());
        System.out.println("e) Producto escalar: " + a.productoEscalar(b));
        System.out.println("f) Producto vectorial: " + a.productoVectorial(b));
    }
}
