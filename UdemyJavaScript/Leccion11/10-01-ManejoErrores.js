'use strict'

try{
    //Creamos una variable sin declarar
    x = 10;
}
catch(error){
    //Atrapamos el error
    console.log(error);
}
finally{
    //Finally siempre se ejecuta, independientemente de si se atrapa o no un error. Es opcional
    console.log('Termina la revisión de errores')
}

//El programa se sigue ejecutando (no se 'rompe')
console.log('continua...');