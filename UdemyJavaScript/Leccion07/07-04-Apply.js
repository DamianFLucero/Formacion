let persona1 = {
    nombre : 'Juan',
    apellido : 'Pérez',
    nombreCompleto: function(titulo, tel){
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
    }
}

let persona2 = {
    nombre : 'Carlos',
    apellido : 'Lara'
}

//Imprimimos la función y pasamos los parámetros:
console.log(persona1.nombreCompleto('Ing', '55667788'));

//Creamos un arreglo con los nuevos valores y los pasamos como parámetro junto a 'persona2':
let arreglo = ['Dr.', '11223344'];
console.log(persona1.nombreCompleto.apply(persona2, arreglo));
//Variante:
console.log(persona1.nombreCompleto.apply(persona2, ['Dr.', '11223344']));
