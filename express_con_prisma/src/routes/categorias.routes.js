import { Router } from "express";
import {
  crearCategoria,
  listarCategoria,
  devolverCategoria,
  actualizarCategoria,
  eliminarCategoria,
} from "../controllers/categorias.controller.js";

export const categoriaRouter = Router();

categoriaRouter.route("/categorias").post(crearCategoria).get(listarCategoria);

categoriaRouter
  .route("/categoria/:id")
  .get(devolverCategoria)
  .patch(actualizarCategoria)
  .put(actualizarCategoria)
  .delete(eliminarCategoria);
