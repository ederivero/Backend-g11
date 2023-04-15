import express from "express";
import * as rutas from "./routes/index.js";
import cors from "cors";

const servidor = express();
servidor.use(express.json());
servidor.use(
  cors({
    origin: ["http://127.0.0.1:5500"],
    methods: ["GET", "POST", "PUT", "PATCH", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

const PORT = 3000;

servidor.use(rutas.categoriaRouter);
servidor.use(rutas.productoRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
