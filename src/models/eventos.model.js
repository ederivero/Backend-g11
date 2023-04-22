import mongoose from "mongoose";
// https://www.mongodb.com/docs/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/
const eventoSchema = new mongoose.Schema({
  titulo: {
    type: mongoose.Schema.Types.String,
    required: true,
  },
  descripcion: mongoose.Schema.Types.String,
  dia: {
    type: mongoose.Schema.Types.Date,
  },
  horaInicio: {
    type: mongoose.Schema.Types.String,
    alias: "hora_inicio",
  },
  horaFin: {
    type: mongoose.Schema.Types.String,
    alias: "hora_fin",
  },
  foto: {
    type: mongoose.Schema.Types.String,
  },
  usuario: {
    type: mongoose.Schema.Types.ObjectId,
    required: true,
  },
});

export const EventoModel = mongoose.model("eventos", eventoSchema);
