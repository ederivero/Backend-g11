import express from "express";

const servidor = express();

servidor.get("/saludar", (req, res) => {
  // req > toda la info entrante
  // res > la forma en la cual respondere al cliente

  console.log("Entraron a mi API!");
  res.json({
    message: "Hola bienvenido a mi API",
  });
});

servidor.get("/saludar/:nombre", (req, res) => {
  console.log(req.params);
  const { nombre } = req.params;
  res.json({
    message: `Hola ${nombre}`,
  });
});

servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente en el puerto 3000");
});
