import javax.swing.*;
import java.awt.*;

public class circulo extends JPanel {
    private double cx, cy, radio;

    public circulo(double cx, double cy, double radio) {
        this.cx = cx;
        this.cy = cy;
        this.radio = radio;
    }

    public String toString() {
        return "Centro: (" + cx + ", " + cy + "), Radio: " + radio;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        int centerX = (int) (cx * 50); 
        int centerY = getHeight() - (int) (cy * 50); 
        int diameter = (int) (radio * 50 * 2); 

        // Dibuja el círculo
        g2d.drawOval(centerX - (int)(radio * 50), centerY - (int)(radio * 50), diameter, diameter);

        g2d.setColor(Color.RED);
        g2d.fillOval(centerX - 5, centerY - 5, 10, 10);

        g2d.setColor(Color.BLACK);
        g2d.drawString("Centro: (" + cx + ", " + cy + ")", centerX + 10, centerY);
    }

    public static void main(String[] args) {
        circulo c = new circulo(3.0, 4.0, 4.0);
        System.out.println(c.toString());

        JFrame frame = new JFrame("Dibujo de Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(c);

        frame.setVisible(true);
    }
}
