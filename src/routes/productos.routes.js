import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";

export const productoRouter = Router();

productoRouter.post("/productos", controllers.crearProducto);
