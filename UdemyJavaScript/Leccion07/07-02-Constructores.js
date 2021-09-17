//Función constructor de objetos de tipo 'Persona':
function Persona(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}

//Creamos e imprimimos objetos:
let padre = new Persona('Juan', 'Pérez', 'jperez@mail.com');
console.log(padre);

let madre = new Persona('Estefanía', 'Linares', 'elinares@mail.com');
console.log(madre);

//Agregamos un parámetro y un valor por defecto al objeto 'Persona':
Persona.prototype.telefono = 'No definido';
console.log(padre.telefono);
//Modificamos el parámetro:
padre.telefono = 3624252525;
console.log(padre.telefono);


//Formas de crear objetos en JS:
//Objeto:
let miObjeto1 = new Object();
let miObjeto2 = {};

//String:
let miCadena1 = new String('Hola');
let miCadena2 = 'Hola';

//Number:
let miNumero1 = new Number(1);
let miNumero2 = 1;

//Boolean:
let miBooleano1 = new Boolean(false);
let miBooleano2 = false;

//Array:
let miArreglo1 = new Array();
let miArreglo2 = [];

//Function:
let miFuncion1 = new Function();
let miFuncion2 = function(){};