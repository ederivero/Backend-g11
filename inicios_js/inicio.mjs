// https://nodejs.org/api/esm.html
import { restar, sumar, secreto } from "./funciones.mjs";

console.log("Hola Mundo");
const nombre = "Eduardo";

function saludar() {
  console.log("Buenas noches");
}

saludar();

const resultado = restar(10, 5);
console.log(resultado);
