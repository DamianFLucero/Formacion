'use strict'
let resultado = '';

try{
    //Con throw lanzamos nuestros propios mensajes de errores
    if(isNaN(resultado)) throw 'No es un número';
    else if (resultado === '') throw 'Es una cadena vacía';
    else if (resultado < 0) throw 'Valor negativo';
}
catch(error){
    console.log(error);
}