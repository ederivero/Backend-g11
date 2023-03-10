from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario_controller import UsuariosController

from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tareas'

api = Api(app)

conexion.init_app(app)

Migrate(app = app,db = conexion)

# definir mis rutas del proyecto
api.add_resource(UsuariosController, '/registro')

if __name__ == '__main__':
    app.run(debug=True)