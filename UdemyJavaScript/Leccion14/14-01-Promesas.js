let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = false;
    if(expresion)
        resolver('Promesa resuelta');
    else
        rechazar('Se produjo un error');
}); 

miPromesa.then(valor => console.log(valor),error => console.log(error));

//Variante 'catch'
miPromesa.then(valor => console.log(valor)).catch(error => console.log(error));


//Función setTimeout y promesa
let promesa = new Promise((resolver) => {
    setTimeout(()=> resolver('Saludos con promesa y timeout'), 3000);
});

promesa.then(valor => console.log(valor));


//async indica que una función regresa una promesa
async function miFuncionConPromesa(){
    return 'saludos con promesa y async';
}

miFuncionConPromesa().then(valor => console.log(valor));


//async/await - La expresión await provoca que la ejecución de una función async sea pausada hasta que una Promise sea terminada o rechazada
async function funcionConPromesaYAwait(){
    let miPromesa = new Promise(resolver => {resolver('Promesa con await');});
    console.log(await miPromesa);
}

funcionConPromesaYAwait();


//promesas, await, async y setTimeout
async function funcionConPromesaAwaitTimeout(){
    let miPromesa = new Promise(resolver => {setTimeout(() => resolver ('promesa con await y timeout'), 3000);});
    console.log(await miPromesa);
}

funcionConPromesaAwaitTimeout();