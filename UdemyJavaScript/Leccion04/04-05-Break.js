//Imprime solo el primer numero par y "break" corta el programa

for (let contador = 0; contador <= 10; contador++){
    if(contador % 2 == 0){
        console.log(contador);
        break;
    }
}
console.log("Fin de ciclo");