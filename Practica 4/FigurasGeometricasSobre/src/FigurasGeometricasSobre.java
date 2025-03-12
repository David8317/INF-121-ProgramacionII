public class FigurasGeometricasSobre {

    public double area(double radio) {
        return Math.PI * radio * radio;
    }
    
    public double area(int base, int altura) {
        return base * altura;
    }
    
    public double area(double base, double altura) {
        return (base * altura) / 2.0;
    }
    
    public double area(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) * altura) / 2.0;
    }
    
    public double area(double base, int apotema) {
        return (base * apotema) / 2.0;
    }

    public static void main(String[] args) {
    	FigurasGeometricasSobre f1 = new FigurasGeometricasSobre();
    	FigurasGeometricasSobre f2 = new FigurasGeometricasSobre();
    	FigurasGeometricasSobre f3 = new FigurasGeometricasSobre();
    	FigurasGeometricasSobre f4 = new FigurasGeometricasSobre();
    	FigurasGeometricasSobre f5 = new FigurasGeometricasSobre();
        
        System.out.println(" círculo: " + f1.area(7));
        System.out.println(" rectángulo: " + f2.area(6, 4));
        System.out.println(" triángulo rectángulo: " + f3.area(4.0, 2.0));
        System.out.println(" trapecio: " + f4.area(3, 8, 3));
        System.out.println(" pentágono: " + f5.area(9.0, 4.0));
    }
}
