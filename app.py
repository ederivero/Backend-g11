from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ
from db import conexion
from flask_restful import Api

from controllers.usuario_controller import RegistroController

load_dotenv()

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
conexion.init_app(app)

api = Api(app)

Migrate(app, conexion)


api.add_resource(RegistroController, '/registro')

if __name__ == '__main__':
    app.run(debug=True)