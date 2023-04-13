const data = {
  nombre: "Eduardo",
  correo: "ederiveroman@gmail.com",
  hobbies: [
    {
      nombre: "Ir al estadio",
      intensidad: "Normal",
    },
    {
      nombre: "Programar",
      intensidad: "Alta",
    },
  ],
};

// Destructuracion > extraer parte de una clase, funcion, variable, etc

// Creo una variable 'nombre' con la informacion que tiene la propiedad nombre del JSON data
const { nombre } = data;

const correo = "juanito_el_mas_naky_kentucky@hotmail.com";

// La forma mas sencilla
const correo_usuario = data.correo;

// Usando destructuracion puedo reutilizar la propiedad de una variable pero al momento de crear la nueva variable utilizar un nombre completamente diferente
const { correo: nuevo_correo } = data;

// ...otro > extraigo la informacion de la variable y lo guardo en una nueva variable con un nuevo espacio de memoria
const { hobbies, ...otro } = data;

console.log(nombre);
console.log(correo_usuario);
console.log(nuevo_correo);
console.log(otro);
