import { Prisma } from "../prisma.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";

export const registroUsuario = async (req, res) => {
  // { nombre : 'Eduardo', apellido: 'De Rivero', correo: 'xxxx@gmail.com', pass...}
  const data = req.body;

  try {
    const password = bcrypt.hashSync(data.password, 10);

    const usuarioCreado = await Prisma.usuario.create({
      data: { ...data, password },
    });

    return res.status(201).json({
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error.message,
    });
  }
};

export const loginUsuario = async (req, res) => {
  const { correo, password } = req.body;

  try {
    const usuarioEncontrado = await Prisma.usuario.findUnique({
      where: {
        correo,
      },
    });

    if (!usuarioEncontrado) {
      throw new Error("El usuario no existe");
    }

    // compara el texto con el hash y es retorna true caso contrario retorna false
    const resultado = bcrypt.compareSync(password, usuarioEncontrado.password);
    if (resultado === true) {
      // jti > identificador de la token (a quien le pertenece)
      const token = jwt.sign(
        { jti: usuarioEncontrado.id, nombre: usuarioEncontrado.nombre },
        process.env.JWT_SECRET,
        { expiresIn: "1h" }
      );

      return res.json({
        content: token,
      });
    } else {
      throw new Error("Credenciales incorrectas");
    }
  } catch (error) {
    return res.status(400).json({
      message: "Error al autenticar al usuario",
      content: error.message,
    });
  }
};
