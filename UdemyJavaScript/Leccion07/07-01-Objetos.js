
//Crear un objeto:
let persona = {
    nombre : 'Damián',
    apellido : 'Lucero',
    email : 'damianflucero@hotmail.com',
    edad : 30,
    nombreCompleto : function(){
        return this.apellido + ' ' + this.nombre;
    }
}

//Imprimir propiedades especificas de nuestro objeto:
console.log(persona.apellido);
console.log(persona.nombre);
console.log(persona.email);
console.log(persona.edad);

//Imprimir todas las propiedades de nuestro objeto:
console.log(persona);

//Salida de nuestra función de objeto:
console.log(persona.nombreCompleto());

//Otra forma de crear un objeto (menos común):
let persona2 = new Object();
persona2.nombre = 'Carlos';
persona2.direccion = 'Saturno 15';
persona2.telefono = '55443322';

console.log(persona2.direccion);

//Variante de acceso a propiedad de un objeto:
console.log(persona['apellido']);

//Recorrer un objeto con un "for in":
for( nombrePropiedad in persona){
    console.log(nombrePropiedad);
    console.log(persona[nombrePropiedad]);
}

//Agregar propiedad a un objeto:
persona.tel = '3624662711';
console.log(persona.tel);

//Eliminar propiedad de un objeto:
delete persona.tel;
console.log(persona);

//Variantes para imprimir propiedades de un objeto 
//1 - Concatenar valores:
console.log(persona.nombre + ", " + persona.apellido);
//2 - For in:
for (i in persona){
    console.log(persona[i]);
}
//3 - Array:
let personaArray = Object.values(persona);
console.log(personaArray);
//4 - Json:
let personaString = JSON.stringify(persona);
console.log(personaString);

