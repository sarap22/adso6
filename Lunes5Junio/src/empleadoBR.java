import javax.swing.*;
public class empleadoBR {
    private String tipoEmpleado;
    private float ventaMes;
    private int horasExtra;
    private double salarioBase;
    public empleadoBR() {
    }
    public empleadoBR(String tipoEmpleado, float ventaMes, int horasExtra) {
        this.tipoEmpleado = tipoEmpleado;
        this.ventaMes = ventaMes;
        this.horasExtra = horasExtra;
    }

    public String getTipoEmpleado() {
        return tipoEmpleado;
    }

    public void setTipoEmpleado(String tipoEmpleado) {
        this.tipoEmpleado = tipoEmpleado;
    }

    public float getVentaMes() {
        return ventaMes;
    }

    public void setVentaMes(float ventaMes) {
        this.ventaMes = ventaMes;
    }

    public int getHorasExtra() {
        return horasExtra;
    }

    public void setHorasExtra(int horasExtra) {
        this.horasExtra = horasExtra;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public float calcularSalarioBruto() throws Exception {
        int horas = horasExtra * 20;
        if(tipoEmpleado.equals("vendedor") || tipoEmpleado.equals("encargado")){
            switch (tipoEmpleado){
                case "vendedor" -> salarioBase = 1000;
                case "encargado" -> salarioBase = 1500;
            }
            if (ventaMes > 1000 && ventaMes < 1500) {
                salarioBase += 100;
            } else if (ventaMes >= 1500) {
                salarioBase += 200;
            }
        } else {
            throw new Exception("El tipo de empleado tiene que ser VENDEDOR o ENCARGADO");
        }
        return (float) salarioBase + horas;
    }
    public float CalculaSalarioNeto() throws Exception {
        //System.out.println(getTipoEmpleado()+"\n venta Mes "+ getVentaMes()+"\n horas "+ getHorasExtra()+"\n salario "+ calcularSalarioBruto());
        if (calcularSalarioBruto()>=0 && calcularSalarioBruto()<1000){
            return calcularSalarioBruto();
        }
        else if(calcularSalarioBruto()>=1000 && calcularSalarioBruto()<1500){
            return (float) (calcularSalarioBruto()-(calcularSalarioBruto()*0.16));
        }
        else if(calcularSalarioBruto()>=1500){
            return (float) (calcularSalarioBruto()-(calcularSalarioBruto()*0.18));
        }
        else{
            throw new Exception("El salario es menor a 0");
        }
    }

}