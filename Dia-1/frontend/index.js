const pedirAlumnos = async () => {
  const respuesta = await fetch("http://localhost:5000/alumnos", {
    method: "GET",
  });

  const data = await respuesta.json();

  console.log(data);
};

pedirAlumnos();
