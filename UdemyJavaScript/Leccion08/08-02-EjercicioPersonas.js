/*
PERSONA
_idPersona: number
_nombre: string
_apellido: string
_edad: number
contadorPersonas
getIdPersona(): number
getNombre(): string
setNombre(string)
getApellido(): string
setApellido(string)
getEdad(): Number
setEdad(string)
toString()

ExtendsPersona
CLIENTE
_idCliente: number
_fechaRegistro: Date
getIdCliente
getFechaRegistro(): Date
setFechaRegistro(Date)
toString()

Extends Persona
EMPLEADO
_idEmpleado: Long
_sueldo: number
getIdEmpleado(): number
getSueldo(): number
setSueldo(number)
toString()
*/


class Persona{

    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get idPersona(){
        return this._idPersona;
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }

    get edad(){
        return this._edad;
    }
    set edad(edad){
        this._edad = edad;
    }

    toString(){
        return 'id:' + this._idPersona + ' - ' + this._apellido + ', ' + this._nombre + ' - ' + this._edad + ' años';
    }
}


class Empleado extends Persona{

    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get sueldo(){
        return this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }

    toString(){
        return super.toString() + ' - idEmp: ' + this._idEmpleado + ' - sueldo: ' + this._sueldo
    }
}


class Cliente extends Persona{

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente(){
        return this._idCliente;
    }

    get fechaRegistro(){
        return this._fechaRegistro;
    }
    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro;
    }

    toString(){
        return super.toString() + ' | idCli: ' + this._idCliente + ' - ' + this._fechaRegistro
    }
}


//Pruebas:
let persona1 = new Persona('Damián', 'Lucero', 30);
console.log(persona1.toString());

let empleado1 = new Empleado('Ludmila', 'Cantero', 25, 46000);
console.log(empleado1.toString());

let empleado2 = new Empleado('Gastón', 'Lottero', 36, 35000);
console.log(empleado2.toString());

let cliente1 = new Cliente('Jimena', 'Colombo', 28, new Date());
console.log(cliente1.toString());
