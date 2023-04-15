// Usar el patron de diseño Singleton que indica que solo debe tener una sola instancia por todo el proyecto

import prisma from "@prisma/client";

export const Prisma = new prisma.PrismaClient();
