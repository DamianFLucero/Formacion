class Empleado{
    constructor(nombre,sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    //Definimos un método en la clase padre
    obtenerDetalles(){
        return `Nombre empleado: ${this.nombre} - Sueldo: ${this.sueldo}`
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre,sueldo);
        this.departamento = departamento;
    }
    //Sobreescribimos exactamente el mismo método de la clase padre
    obtenerDetalles(){
        return `Gerente - ${super.obtenerDetalles()} - Departamento: ${this.departamento}`;
    }
}

//Creamos una función de impresión
function imprimir(tipo){
    console.log(tipo.obtenerDetalles());
    //Usamos 'instanceof' para que nos devuelva el tipo de objeto creado. Siempre de menor a mayor jerarquía
    if(tipo instanceof Gerente){
        console.log("Es del tipo Gerente");
    }
    else{
        console.log("Es del tipo Empleado");
    }
}

//Accedemos al método desde la clase padre
let empleado1 = new Empleado('Esteban', 6000, 'Sistemas');

//Accedemos al método desde la clase hija
let gerente1 = new Gerente('Carlos', 5000, 'Sistemas');

imprimir(empleado1);
imprimir(gerente1);