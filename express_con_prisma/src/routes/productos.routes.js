import { Router } from "express";
import { crearProducto } from "../controllers/productos.controller.js";

export const productoRouter = Router();

// productoRouter.route('/productos').post(crearProducto)
productoRouter.post("/productos", crearProducto);
