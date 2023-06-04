import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class empleadoBRTest {
    @Test
    public void TestcalcularSalarioBruto() throws Exception {
        System.out.println("Prueba del metodo que calcula el salario sin las retenciones");
        String empleado="encargado";
        float ventaMes= 1600;
        int horas= 10;
        empleadoBR empleadoB = new empleadoBR(empleado,ventaMes,horas);
        float esperado =2000;
        assertEquals(esperado,empleadoB.calcularSalarioBruto(),0.0);
    }
    @Test
    public void TestcalcularSalarioNeto() throws Exception {
        System.out.println("Prueba del metodo que calcula el salario total (con las retenciones)");
        String empleado="encargado";
        float ventaMes= 0;
        int horas= 0;
        empleadoBR empleadoB = new empleadoBR(empleado,ventaMes,horas);
        float esperado=1230;
        assertEquals(esperado,empleadoB.CalculaSalarioNeto(),0.0);
    }
}