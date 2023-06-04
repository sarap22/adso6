import javax.swing.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String empleado="encargado";
        float ventaMes= 0;
        int horas= 0;
        empleadoBR empleadoB = new empleadoBR(empleado,ventaMes,horas);
        //JOptionPane.showMessageDialog(null, empleadoB.calcularSalarioBruto());
        JOptionPane.showMessageDialog(null, "Su salario es de $"+empleadoB.CalculaSalarioNeto());
        
    }
}