class cola {
    private long[] arreglo;
    private int inicio, fin, n, elementos;

    public cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.elementos = 0;
    }

    public void insert(long e) {
        if (!isFull()) {
            fin = (fin + 1) % n;
            arreglo[fin] = e;
            elementos++;
        } else {
            System.out.println("Cola llena");
        }
    }

    public long remove() {
        if (!isEmpty()) {
            long valor = arreglo[inicio];
            inicio = (inicio + 1) % n;
            elementos--;
            return valor;
        }
        System.out.println("Cola vacía");
        return -1;
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        }
        System.out.println("Cola vacía");
        return -1;
    }

    public boolean isEmpty() {
        return elementos == 0;
    }

    public boolean isFull() {
        return elementos == n;
    }

    public int size() {
        return elementos;
    }

    public static void main(String[] args) {
        cola cola = new cola(5);
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);
        System.out.println(cola.remove()); // 10
        System.out.println(cola.remove()); // 20
        System.out.println(cola.peek());   // 30
    }
}
