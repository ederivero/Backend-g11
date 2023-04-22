import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import mongoose from "mongoose";
import { usuarioRouter } from "./routes/usuarios.routes.js";
import { eventoRouter } from "./routes/eventos.routes.js";

dotenv.config();

const servidor = express();
// Operador logico OR
const PORT = process.env.PORT || 3000;

servidor.use(
  cors({
    methods: ["GET", "POST", "PUT", "DELETE"],
    origin: "*",
  })
);
servidor.use(express.json());

servidor.use(usuarioRouter);
servidor.use(eventoRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
  conectarBD();
});

function conectarBD() {
  mongoose
    .connect(process.env.MONGODB_URI)
    .then(() => {
      console.log("Base de datos conectada 🔌");
    })
    .catch((e) => {
      console.error("Error al conectarse a la base de datos");
      console.error(e.message);
    });
}
