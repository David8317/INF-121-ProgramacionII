public class D extends A {
    public int y;

    public D(int x, int y, int z) {
        super(x, z);
        this.y = y;
    }

    public void incrementaXYZ() {
        x = x + 1;
        y = y + 1;
        z = z + 1;
    }

    public void incrementaYZ() {
        y = y + 1;
        z = z + 1;
    }

    public String toString() {
        return x + " " + y + " " + z;
    }
}
