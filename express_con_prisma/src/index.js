import express from "express";
import * as rutas from "./routes/index.js";

const servidor = express();
servidor.use(express.json());

const PORT = 3000;

servidor.use(rutas.categoriaRouter);
servidor.use(rutas.productoRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
