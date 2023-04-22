import { Router } from "express";
import * as controller from "../controllers/eventos.controllers.js";

export const eventoRouter = Router();

eventoRouter.route("/eventos").post(controller.crearEvento);
