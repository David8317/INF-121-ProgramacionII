public class Lineal {
    private double x, y, z;

    public Lineal(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Lineal sumar(Lineal otro) {
        return new Lineal(this.x + otro.x, this.y + otro.y, this.z + otro.z);
    }

    public Lineal restar(Lineal otro) {
        return new Lineal(this.x - otro.x, this.y - otro.y, this.z - otro.z);
    }

    public Lineal multiplicar(double escalar) {
        return new Lineal(this.x * escalar, this.y * escalar, this.z * escalar);
    }

    public double productoEscalar(Lineal otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }

    public Lineal productoVectorial(Lineal otro) {
        return new Lineal(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }

    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public boolean esPerpendicular(Lineal otro) {
        return Math.abs(this.productoEscalar(otro)) < 1e-9;
    }

    public boolean esParalelo(Lineal otro) {
        return this.productoVectorial(otro).magnitud() == 0;
    }

    public Lineal proyeccionSobre(Lineal otro) {
        double factor = this.productoEscalar(otro) / (otro.magnitud() * otro.magnitud());
        return otro.multiplicar(factor);
    }

    public double componenteEnDireccion(Lineal otro) {
        return this.productoEscalar(otro) / otro.magnitud();
    }

    public String toString() {
        return "Lineal(" + x + ", " + y + ", " + z + ")";
    }

    public static void main(String[] args) {
        Lineal a = new Lineal(1, 2, 3);
        Lineal b = new Lineal(4, 5, 6);

        System.out.println("a) Perpendicular: |a + b| = |a - b| " + (Math.abs(a.sumar(b).magnitud() - a.restar(b).magnitud()) < 1e-9));
        System.out.println("b) Perpendicular: |a - b| = |b - a| " + (Math.abs(a.restar(b).magnitud() - b.restar(a).magnitud()) < 1e-9));
        System.out.println("c) Perpendicular: a · b = 0 " + (a.productoEscalar(b) == 0));
        System.out.println("d) Perpendicular: |a + b|² = |a|² + |b|² " + (Math.abs(Math.pow(a.sumar(b).magnitud(), 2) - (Math.pow(a.magnitud(), 2) + Math.pow(b.magnitud(), 2))) < 1e-9));
        System.out.println("e) Paralelo: a = r * b " + a.esParalelo(b));
        System.out.println("f) Paralelo: a × b = 0 " + (a.productoVectorial(b).magnitud() == 0));
        System.out.println("g) Proyección de a sobre b: " + a.proyeccionSobre(b));
        System.out.println("h) Componente de a en la dirección de b: " + a.componenteEnDireccion(b));
    }
}
