let a = 3, b = 2;
let z = a + b;
console.log("Resultado de la suma: " + z);

z = a - b;
console.log("Resultado de la resta: " + z);

z = a * b;
console.log("Resultado de la multiplicación: " + z);

z = a / b;
console.log("Resultado de la división: " + z);

z = a % b;
console.log("Resultado del módulo (residuo): " + z);

z = a ** b;
console.log("Resultado del exponente: " + z);

//Incremento:
//Pre-incremento (el operador ++ antes de la variable):
z = ++a; //a = 3
console.log(a);
console.log(z);

//Post-incremento (el operador ++ despues de la variable):
z = b++; // b = 2
console.log(b);
console.log(z);

//Decremento:
//Pre-decremento:
z = --a; //a = 3
console.log(a);
console.log(z);

//Post-decremento:
z = b--; // b = 3
console.log(b);
console.log(z);

//---------------------------------------------------------------------------

//Operadores de comparación:
let x = 3, y = '3';

//== controla el valor sin importar el tipo
z = x == y;
console.log(z);

//=== controla el valor y el tipo
z = x === y;
console.log(z);

//Distinto de:
z = x != y;
console.log(z);

z = x !== y;
console.log(z);

//---------------------------------------------------------------------------

//Operadores relacionales:
x = 3, y = 4;

z = x < y;
console.log(z);

z = x >= y;
console.log(z);

//---------------------------------------------------------------------------

//Operador ternario:
let numero = 9;
resultado = (numero % 2 == 0) ? "Número par" : "Número impar";
console.log(resultado);

//---------------------------------------------------------------------------

//Convertir String a Number:
let miEdad = "17";
console.log(typeof miEdad);

let edad = Number(miEdad);
console.log(typeof edad);

//---------------------------------------------------------------------------

//Función isNaN (is not a number):
let valorString = "18x";
let valorNumerico = Number (valorString);
console.log(valorNumerico);

if (isNaN(valorNumerico)){  //Validamos que en un principio sea un valor numérico
    console.log("No es un valor numérico");
}
else{  //Si pasa la validación, entra en el "else"
    resultado = (valorNumerico % 2 == 0) ? "Número par" : "Número impar";
    console.log(resultado);
}

