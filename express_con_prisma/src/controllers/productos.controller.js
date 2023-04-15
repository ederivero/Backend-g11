import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
  const data = req.body;

  const nuevoProducto = await Prisma.producto.create({
    data: {
      ...data,
      fechaVencimiento: new Date(data.fechaVencimiento),
    },
  });

  return res.status(201).json({
    message: "Producto creado exitosamente",
    content: nuevoProducto,
  });
};
