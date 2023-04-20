import { Router } from "express";
import * as controllers from "../controllers/usuarios.controllers.js";

export const usuarioRouter = Router();

usuarioRouter.post("/registro", controllers.registroUsuario);
usuarioRouter.post("/login", controllers.loginUsuario);
