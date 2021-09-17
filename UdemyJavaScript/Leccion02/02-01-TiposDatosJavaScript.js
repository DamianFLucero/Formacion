//String:
var nombre = "Damián";
console.log(nombre);
console.log(typeof nombre);

//Number:
var numero = 1000;
console.log(numero);
console.log(typeof numero);

/*Las variables son dinámicas.
Pueden cambiar de tipo de variable*/
var numero = "Damián";
console.log(numero);
console.log(typeof numero);

//Object:
var objeto = {
    nombre : "Juan",
    apellido: "Perez",
    telefono: "123456789"
}
console.log(objeto);
console.log(typeof objeto);

//Boolean:
var bandera = true;
console.log(bandera);
console.log(typeof bandera);

//Function:
function miFuncion(){}
console.log(miFuncion);
console.log(typeof miFuncion);

//Symbol:
var simbolo = Symbol("mi simbolo");
console.log(simbolo);
console.log(typeof simbolo);

//Clase (function):
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);
console.log(typeof Persona);

//Undefined:
/*Por defecto si no asignamos un valor a la variable, esta es de tipo "undefined":*/
var x;
console.log(x);
console.log(typeof x);

/*También podemos definir la variable como "undefined":*/
x = undefined;
console.log(x);
console.log(typeof x);

//Null:
var y = null;
console.log(y);
console.log(typeof y);

//Arrays (object):
var autos = ['BMW','Audi','Volvo'];
console.log(autos);
console.log(typeof autos);

