/*
  Warnings:

  - A unique constraint covering the columns `[nombre,precio,categoria_id]` on the table `productos` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "productos_nombre_precio_categoria_id_key" ON "productos"("nombre", "precio", "categoria_id");
