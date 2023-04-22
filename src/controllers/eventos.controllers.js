import { EventoModel } from "../models/eventos.model.js";

export const crearEvento = async (req, res) => {
  const data = req.body;

  try {
    const nuevoEvento = await EventoModel.create(data);

    return res.status(201).json({
      message: "Evento creado exitosamente",
      content: nuevoEvento,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el evento",
      content: error.message,
    });
  }
};
