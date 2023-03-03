from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ

load_dotenv() # es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno 

app = Flask(__name__)
# dialecto://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# si quiero crear mi conexion en otro archivo e inicializar la configuracion de mi conexion tengo que utilizar el metodo init_app y es aca donde le pasare el parametro de mi instancia de la clase Flask
conexion.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)