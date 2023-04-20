import prisma from "@prisma/client";

export const Prisma = new prisma.PrismaClient({ log: ["info"] });
