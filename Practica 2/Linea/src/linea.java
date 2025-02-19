import javax.swing.*;
import java.awt.*;

public class linea extends JPanel {
    private double x1, y1, x2, y2;

    public linea(double x1, double y1, double x2, double y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public String toString() {
        return "Punto 1: (" + x1 + ", " + y1 + "), Punto 2: (" + x2 + ", " + y2 + ")";
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        int invertedY1 = getHeight() - (int) (y1 * 50);
        int invertedY2 = getHeight() - (int) (y2 * 50);

        g2d.drawLine((int) x1 * 50, invertedY1, (int) x2 * 50, invertedY2);

        g2d.setColor(Color.RED);
        g2d.fillOval((int) x1 * 50 - 5, invertedY1 - 5, 10, 10); // Punto 1
        g2d.fillOval((int) x2 * 50 - 5, invertedY2 - 5, 10, 10); // Punto 2

        g2d.setColor(Color.BLACK);
        g2d.drawString("Punto 1: (" + x1 + ", " + y1 + ")", (int) x1 * 50 + 10, invertedY1);
        g2d.drawString("Punto 2: (" + x2 + ", " + y2 + ")", (int) x2 * 50 + 10, invertedY2);
    }


    public static void main(String[] args) {
        linea l = new linea(1.0, 2.0, 4.0, 6.0);
        System.out.println(l.toString());

        JFrame frame = new JFrame("Dibujo de Línea");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(l); 

        // la ventana
        frame.setVisible(true);
    }
}
