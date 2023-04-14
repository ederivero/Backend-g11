import express from "express";

const servidor = express();

const productos = [
  {
    nombre: "Martillo",
    precio: 7.5,
    disponible: true,
  },
  {
    nombre: "Cincel",
    precio: 18.0,
    disponible: true,
  },
  {
    nombre: "Cinta aislante",
    precio: 3.8,
    disponible: false,
  },
];
const PORT = 3000;

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
