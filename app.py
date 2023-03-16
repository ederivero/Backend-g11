from flask import Flask
from flask_migrate import Migrate
from db import conexion

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = ''
conexion.init_app(app)

Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)