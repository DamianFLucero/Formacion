let persona1 = {
    nombre : 'Juan',
    apellido : 'Pérez',
    nombreCompleto: function(){
        return this.nombre + ' ' + this.apellido;
    }
}

let persona2 = {
    nombre : 'Carlos',
    apellido : 'Lara'
}

//Uso de 'Call' para utilizar métodos en un objeto definidos en otro:
console.log(persona1.nombreCompleto.call(persona2));
