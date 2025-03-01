class pila {
    private long[] arreglo;
    private int top;
    private int n;

    public pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (!isFull()) {
            arreglo[++top] = e;
        } else {
            System.out.println("Pila llena");
        }
    }

    public long pop() {
        if (!isEmpty()) {
            return arreglo[top--];
        }
        System.out.println("Pila vacía");
        return -1;
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[top];
        }
        System.out.println("Pila vacía");
        return -1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
       pila pila = new pila(5);
        pila.push(10);
        pila.push(20);
        pila.push(30);
        System.out.println(pila.pop()); // 30
        System.out.println(pila.pop()); // 20
        System.out.println(pila.peek()); // 10
    }
}
