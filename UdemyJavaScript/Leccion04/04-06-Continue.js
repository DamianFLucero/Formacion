//Pregunta si el numero no es par y salta a la siguiente iteración con "continue"
for (let contador = 0; contador <=10; contador++){
    if (contador % 2 !== 0){
        continue;
    }
        console.log(contador);
}
console.log("Fin de ciclo")