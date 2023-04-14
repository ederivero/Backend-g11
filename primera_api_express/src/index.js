import express from "express";

const servidor = express();

// sirve para indicar un middleware > es un controlador que va a interactuar con todas las peticiones que ingresen a mi API
// json() > sirve para indicar que mi aplicacion podra 'entender' los JSON entrantes por el body y lo convertira a un json legible
servidor.use(express.json());

const productos = [
  {
    nombre: "Martillo",
    precio: 7.5,
    disponible: true,
  },
  {
    nombre: "Cincel",
    precio: 18.0,
    disponible: true,
  },
  {
    nombre: "Cinta aislante",
    precio: 3.8,
    disponible: false,
  },
];

const PORT = 3000;

servidor
  .route("/productos")
  .get((req, res) => {
    res.status(200).json({
      content: productos,
    });
  })
  .post((req, res) => {
    console.log(req.body);
    // convierto el JSON a un string y por ende si el valor es '{}' significa que esta vacio
    //   if (JSON.stringify(req.body) === "{}") {
    // { nombre : 'Eduardo' } > Object.keys({...}) > ['nombre', '...']
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
    if (Object.keys(req.body).length === 0) {
      res.status(400).json({
        message: "Informacion incorrecta",
      });
    }

    productos.push(req.body);

    res.status(201).json({
      message: "Producto agregado exitosamente",
      content: req.body,
    });
  });

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
