//Declaración arreglos antigua:
//let autos = new Array('BMW', 'Mercedes Benz', 'Volvo');

//Como se debe delcarar un arreglo:
const autos = ['BMW', 'Mercedes Benz', 'Volvo'];

//Impresión:
console.log(autos);

//Acceso a elementos en un array:
console.log(autos[0]);

//Acceder a todos los elementos de un array y su posición:
for (let i = 0; i < autos.length; i++){
    console.log(i + ' : ' + autos[i]);
}

//Modificar un valor de un array:
autos [1] = 'Renault';
console.log(autos);

//Ingresar un nuevo valor al array:
autos.push('Honda');
console.log(autos);

//Imprimir la cantidad de elementos de un array:
console.log(autos.length);

//Agregar un elemento al final de nuestra array:
autos[autos.length] = 'Cadillac';
console.log(autos);

//Agregar un elemento dejando espacios en el array:
autos[6] = 'Porsche';
console.log(autos);
