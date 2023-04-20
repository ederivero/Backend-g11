import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";
import { validarToken, esAdmin } from "../utils/wachiman.js";

export const productoRouter = Router();

productoRouter.post(
  "/productos",
  validarToken,
  esAdmin,
  controllers.crearProducto
);
