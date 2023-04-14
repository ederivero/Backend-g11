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

servidor
  .route("/producto/:id")
  .get((req, res) => {
    // en base al id que sera la posicion del arreglo devolver el producto
    const { id } = req.params;
    const resultado = productos[id];

    if (resultado) {
      //   const id = req.params.id;
      res.status(200).json({
        content: resultado,
      });
    } else {
      res.status(404).json({
        message: "El producto no existe",
      });
    }
  })
  .put((req, res) => {
    const { id } = req.params;
    const body = req.body;

    const resultado = productos[id];

    if (!resultado) {
      res.status(404).json({
        message: "El producto no existe",
      });
    }

    productos[id] = body;

    res.status(201).json({
      message: "Producto actualizado exitosamente",
      content: productos[id],
    });
  })
  .patch((req, res) => {
    // TODO: Hacer la actualizacion parcial Por ejemplo si solo quiero cambiar el nombre o si solo quiero cambiar el nombre y el precio
  })
  .delete((req, res) => {
    const { id } = req.params;
    const resultado = productos[id];

    if (!resultado) {
      res.status(404).json({
        message: "El producto no existe",
      });
    }
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
    productos.splice(id, 1);

    res.status(200).json({
      message: "Producto eliminado exitosamente",
    });
  });

servidor.route("/buscar-productos").get((req, res) => {
  console.log(req.query);
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
  let resultado = [];

  if (req.query.nombre) {
    resultado = [
      ...resultado,
      ...productos.filter((producto) => {
        // si en la posicion que estamos en el arreglo retorna true entonces se agregara ese elemento al nuevo arreglo
        return producto.nombre === req.query.nombre;
      }),
    ];
  }

  // Para que sea la busqueda de un inicio de una palabra mediante expresiones regulares
  if (req.query.patron) {
    resultado = [
      ...resultado,
      ...productos.filter((producto) => {
        // podemos utilizar expresiones regulares para hacer busqueda de patrones
        return new RegExp(`${req.query.patron}\w*`).test(producto.nombre);
      }),
    ];
  }

  if (req.query.disponible) {
    resultado = [
      ...resultado,
      ...productos.filter((producto) => {
        return String(producto.disponible) === req.query.disponible;
      }),
    ];
  }
  res.status(200).json({
    content: resultado,
  });
});

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
