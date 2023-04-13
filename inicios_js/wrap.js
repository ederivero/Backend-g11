function sumar(x, y) {
  return x + y;
}

function restar(x, y) {
  return x - y;
}
// CALLBACKS > es la ejecucion de una funcion dentro de otra funcion tambien se le suele conocer como un wrap de funciones en JS
function operacion(funcion, parametro1, parametro2) {
  const resultado = funcion(parametro1, parametro2);
  console.log(resultado);
}

operacion(sumar, 1, 5);

operacion(restar, 10, 5);

operacion(
  (x, y) => {
    return x * y;
  },
  5,
  6
);
