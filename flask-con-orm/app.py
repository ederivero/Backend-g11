from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

load_dotenv() # es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno 

app = Flask(__name__)
# dialecto://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
conexion = SQLAlchemy(app=app)

if __name__ == '__main__':
    app.run(debug=True)