class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this.nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this.apellido = apellido;
    }
    nombreCompleto(){
        return this._nombre + ' ' + this._apellido;
    }
    //Sobreescribiendo el metodo de la clase padre (Object)
    toString(){
        //Se aplica polimorfismo
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido); 
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //Sobreescritura:
    nombreCompleto(){
        return super.nombreCompleto() + '; ' + this._departamento;
    }
    static saludar(){
        console.log('Saludos desde el método static');
    }
}

let persona1 = new Persona('Damián', 'Lucero');
console.log(persona1.nombre);

let empleado1 = new Empleado('Esteban', 'Quito', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());
console.log(empleado1.toString());

persona1.saludar(); 