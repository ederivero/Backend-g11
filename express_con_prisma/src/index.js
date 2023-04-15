import express from "express";
import { categoriaRouter } from "./routes/categorias.routes.js";

const servidor = express();
servidor.use(express.json());

const PORT = 3000;

servidor.use(categoriaRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
