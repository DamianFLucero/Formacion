//Concatenar variables:
var nombre = "Damián";
var apellido = "Lucero";
var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);

//Concatenación directa:
var nombreCompleto2 = 'Damián' + ' ' + 'Lucero';
console.log(nombreCompleto2);

//Concatenar valores:
var x = nombre + 9 + 9;
console.log(x);

//Concatenar y sumar:
var x = nombre + 9 + 9;
console.log(x);

//Si concatenamos a la inversa nos toma como "number" y los suma primero:
var x = 9 + 9 + nombre;
console.log(x);