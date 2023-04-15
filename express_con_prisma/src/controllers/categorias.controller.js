import { Prisma } from "../prisma.js";

export const crearCategoria = async (req, res) => {
  const body = req.body;

  const resultado = await Prisma.categoria.create({
    data: body,
  });

  console.log(resultado);

  res.status(201).json({
    message: "La categoria se creo exitosamente",
  });
};

export const listarCategoria = async (req, res) => {
  const categorias = await Prisma.categoria.findMany();

  res.json({
    content: categorias,
  });
};

export const devolverCategoria = async (req, res) => {
  // 127.0.0.1:3000/categoria/1 > /:id
  const { id } = req.params;

  const categoria = await Prisma.categoria.findFirst({
    where: {
      id: +id,
    },
    include: {
      // productos: true, // seleccionamos toda la info de los productos
      productos: {
        // indicamos que columnas queremos visualizar
        select: {
          id: true,
          nombre: true,
        },
      },
    },
  });

  if (!categoria) {
    return res.status(400).json({
      message: "La categoria no existe",
    });
  }

  return res.status(200).json({
    content: categoria,
  });
};

export const actualizarCategoria = async (req, res) => {
  const data = req.body;
  const { id } = req.params;

  // SELECT * FROM categorias;
  // SELECT id FROM categorias;
  const categoria = await Prisma.categoria.findFirst({
    where: {
      id: +id,
    },
    select: {
      id: true,
    },
  });

  if (!categoria) {
    return res.status(400).json({
      message: "La categoria no existe",
    });
  }

  const categoriaActualizada = await Prisma.categoria.update({
    where: {
      id: categoria.id,
    },
    data: data,
  });

  return res.json({
    message: "Categoria actualizada exitosamente",
    content: categoriaActualizada,
  });
};

export const eliminarCategoria = async (req, res) => {
  const { id } = req.params;

  const categoria = await Prisma.categoria.findFirst({
    where: {
      id: +id,
    },
    select: {
      id: true,
    },
  });

  if (!categoria) {
    return res.status(400).json({
      message: "La categoria no existe",
    });
  }

  const categoriaEliminada = await Prisma.categoria.delete({
    where: { id: +id },
  });

  return res.json({
    message: "Categoria eliminada exitosamente",
    content: categoriaEliminada,
  });
};
