-- Para crear una base de datos
CREATE DATABASE pruebas;
-- Lista las bases de datos en el servidor
-- Comandos para PSQL (https://www.postgresql.org/docs/current/app-psql.html)
\l

-- Nos cambia a la base de datos que queremos
\c pruebas


-- Se crea un enumerable que sirve para dar unas determinadas opciones
CREATE TYPE tipo_sexo AS ENUM('MASCULINO', 'FEMENINO', 'PANSEXUAL', 'DONUTSEXUAL', 'OTRES');

-- Se crea una tabla en la base de datos
CREATE TABLE alumnos (
id SERIAL NOT NULL PRIMARY KEY,
nombre TEXT NOT NULL,
apellido VARCHAR(50),
sexo tipo_sexo DEFAULT 'OTRES', -- Si utilizamos un ENUM se puede utilizar un valor por defecto dentro de los valores del ENUM, caso contrario lanzara un error
fecha_creacion TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP, -- Es la fecha y hora actual del servidor
matriculado BOOLEAN DEFAULT FALSE
);


-- Mostrar todas las tablas de la base de datos
\dt

-- Mostrar el detalle de la tabla (columnas tipo de datos e informacion de las columnas)
\d alumnos

-- Mostrar todas las tablas y sus indices (mostrara la llave primaria de la tabla que es un indice)
\d 

-- Para visualizar los valores de un enum
SELECT enum_range(NULL::tipo_sexo)

-- Inserta un registro a la base de datos utilizando los valores por defecto
INSERT INTO alumnos (id, nombre, apellido, sexo, fecha_creacion, matriculado) VALUES
                     (DEFAULT, 'Eduardo', 'de Rivero', 'MASCULINO', DEFAULT, true);


-- Inserta utilizando solamente columnas que no tengan valores por defecto
INSERT INTO alumnos (nombre, apellido) VALUES
                     ('Victor', 'Mayta');

-- Insertar varios registros
INSERT INTO alumnos (nombre, apellido) VALUES
                     ('Juana', 'Martinez'),
                     ('Robert', 'Juarez'),
                     ('Mariagracia', 'Quispe');

INSERT INTO alumnos (nombre, apellido, sexo, matriculado) VALUES
                     ('Johana', 'Zuniga', 'FEMENINO', false),
                     ('Martin', 'Zea', 'PANSEXUAL', false),
                     ('Roxana', 'Cutipo', 'DONUTSEXUAL', true);