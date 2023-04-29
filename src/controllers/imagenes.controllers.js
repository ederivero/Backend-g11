import {
  subirImagenes,
  devolverUrlFirmada,
  eliminarArchivo,
} from "../utils/s3.js";
import fs from "fs";

export const subirImagen = async (req, res) => {
  const archivo = req.file;
  //   console.log(req.file);
  //   console.log(req.files);

  const respuesta = await subirImagenes(archivo);
  console.log(respuesta);
  // sirve para eliminar archivos de nuestro proyecto
  fs.unlinkSync(archivo.path);
  // TODO: agregar esa Key al evento al BD
  return res.json({
    message: "Imagen subida exitosamente",
    content: respuesta.Key,
  });
};

export const devolverImagen = (req, res) => {
  const { nombre } = req.params;
  try {
    const url = devolverUrlFirmada(nombre);

    return res.status(200).json({
      content: url,
    });
  } catch (error) {
    return res.status(400).json({
      message: "La imagen no existe",
    });
  }
};

export const eliminarImagen = (req, res) => {
  const { nombre } = req.params;
  eliminarArchivo(nombre);

  return res.status(204).send();
};
