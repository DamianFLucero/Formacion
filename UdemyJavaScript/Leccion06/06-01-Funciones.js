//Llamado a la función antes de la declaración (Hoisting):
miFuncion(2, 9);

//Declaración de función: 
function miFuncion(a, b){
    console.log("Suma: "+(a+b));
}

//Llamando a la función:
miFuncion(3, 7);

//Declaración de función tipo expresión:
let x = function (a, b){return a + b};
resultado = x(2,4);
console.log(resultado);

//Función que se llama a si misma
(function (a, b){
    console.log("Ejecutando función: "+ (a+b));
})(3,4);

//Función tipo flecha:
//Omite palabras reservadas como 'function' o 'return' y llaves entre otras cosas.
const sumarTipoFlecha = (a, b) => a + b;
result = sumarTipoFlecha(8, 9);
console.log(result)