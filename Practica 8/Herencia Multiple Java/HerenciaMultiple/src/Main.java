public class Main {
    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        System.out.println(d);

        d.incrementaXYZ();
        System.out.println(d);

        d.incrementaXZ();
        System.out.println(d);

        d.incrementaYZ();
        System.out.println(d);

        d.incrementaZ();
        System.out.println(d);
    }
}
