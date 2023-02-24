from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
  return "Mi primera API con Flask 😁"

@app.route("/alumno")
def alumno():
  return {
    'nombre': 'Eduardo',
    'edad': 30,
    'promedio': 18
  }

lista_alumnos = [
    {
      'nombre': 'Eduardo',
      'edad': 30,
      'promedio': 18
    },
    {
      'nombre': 'Guillermo',
      'edad': 25,
      'promedio': 18
    }
  ]

@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def alumnos():
  if request.method == 'GET':
    return lista_alumnos
  elif request.method == 'POST':
    # metodos para obtener el body (request.json) ó (request.get_json())
    lista_alumnos.append(request.json)
    return lista_alumnos

@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
  for alumno in lista_alumnos:
    if alumno['nombre'] == nombre:
      return alumno
  return {
    'message': 'El alumno no existe'
  }

@app.route("/html")
def html():
  return "<button>Dame click</button>"

# debug=True => Si realizamos algún cambio podremos verlo en tiempo real (se reiniciará el servidor)
app.run(debug=True)