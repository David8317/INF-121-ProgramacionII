public class Punto {
    private float x;
    private float y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public String coordCartesianas() {
        return "(" + x + ", " + y + ")";
    }

    public String coordPolares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.toDegrees(Math.atan2(y, x));
        return "(" + r + ", " + theta + "°)";
    }

    public String toString() {
        return "Punto(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println("Coordenadas cartesianas: " + p.coordCartesianas());
        System.out.println("Coordenadas polares: " + p.coordPolares());
        System.out.println("Representación: " + p);
    }
}
