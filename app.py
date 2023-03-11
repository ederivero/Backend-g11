from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from controllers.usuario_controller import UsuariosController, LoginController

from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tareas'
# Variable de configuracion para JWT
app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'

api = Api(app)

conexion.init_app(app)

Migrate(app = app,db = conexion)
JWTManager(app)

# definir mis rutas del proyecto
api.add_resource(UsuariosController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)