from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def inicial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods = ['GET', 'POST'])
def alumnos():
    if request.method == 'GET':
        # me conecto a la bd
        conexion = connect(host='localhost', database='pruebas', user='postgres', password='root')
        
        # creo un cursor que es el responsable de hacer lecturas y escrituras a la bd
        cursor = conexion.cursor()
        
        # ejecuto la query
        cursor.execute('SELECT * FROM alumnos;')

        # extraigo la informacion de la ejecucion de la query
        resultado = cursor.fetchall()

        print(resultado)
        return {
            'message': 'Yo soy el GET'
        }
    
    elif request.method == 'POST':
        return {
            'message': 'Yo soy el POST'
        }


if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)