/*El modo estricto no permite usar variables que no fueron declaradas anteriormente
se usa para las buenas prácticas, y ayuda a encontrar errores más facilmente.
Se debe declarar siempre en la primer linea del programa o dentro de una función*/
"use strict";

//X está declarada, por lo tanto imprime por consola:
let x = 10;
console.log(x);

//Y no está declarada, por lo tanto no nos imprime por consola:
y = 9;
console.log(y);

//Dentro de una función:
function miFuncion(){
    "use strict"
    z = 15;
    console.log(z);
}

miFuncion();