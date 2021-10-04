

function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(op1, op2, funcionCallback){
    let res = op1 + op2;
    funcionCallback(`Resultado: ${res}`);
}

sumar(5, 3, imprimir);

//Llamadas asíncronas con uso setTimeout

function miFuncionCallback(){
    console.log('Saludo asíncrono después de 8 seg');
}

setTimeout(miFuncionCallback, 8000);