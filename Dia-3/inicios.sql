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


-- SELECCIONA todas las columnas de los registros cuyo sexo sea MASCULINO
SELECT * FROM alumnos WHERE sexo='MASCULINO';

-- SELECCIONA todos los alumos cuyo sexo sea masculino y la matricula sea verdadera
SELECT * FROM alumnos WHERE sexo='MASCULINO' AND matriculado=true;


-- SELECIONA todos los alumnos que contenga la letra o en cualquier parte del nombre
SELECT * FROM alumnos WHERE nombre LIKE '%o%';

-- SELECCION todos los alumnos cuyo nombre en la tercera posicion tenga la letra o,
-- NOTA: el '_' sirve para indicar cuantas posiciones no deseo saber que hay 
SELECT * FROM alumnos WHERE nombre LIKE '__o%';

-- SELECCIONA todos los alumnos cuyo nombre en la tercera posicion sea la letra 'u' o la letra 'h'
SELECT * FROM alumnos WHERE nombre LIKE '__u%' OR nombre LIKE '__h%';

-- SELECCIONA todos los alumnos cuyo nombre tenga la letra 'x' o cuyo sexo sea PANSEXUAL
SELECT * FROM alumnos WHERE nombre LIKE '%x%' OR sexo = 'PANSEXUAL';


-- Asi se crea una tabla con relacion entre la tabla alumnos y su columna id
CREATE TABLE direcciones(
    id SERIAL PRIMARY KEY,
    direccion TEXT,
    numero int,
    referencia TEXT,
    alumno_id INT, -- El tipo de dato tiene que ser el mismo que la otra columna sino dara error
    CONSTRAINT fk_alumnos FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);

-- DDL (ALTER)


-- TAREA
-- PASOS: Primero ingresar los datos y luego resolver las siguientes queries:
-- DIRECCION            NUM     REFERENCIA              ALUMNO_ID
'Calle los Girasoles', 750, 'Al costado de la polleria', 1
'Calle Los aviadores', 1050, NULL,2
'Av El Sol', 125, 'Del ovalo a media cuadra', 1
'Av Los Gallos', 777, NULL, 3
'Av Tupac Yupanqui', 123, NULL, 7
'Av Siempre viva', 7840, 'Al frente de la ferreteria', 8
'Calle Los martires', 6520, NULL, 5
'Pasaje de las flores', 526, NULL, 4
'Alameda Chabuca', 740, 'Dos cuadras de la piscina', 6
'Callejon Bravo', 14, 'A dos casas de la reja', 3


-- 1. Buscar todas las direcciones que sean calles
-- 2. Listar todas las direcciones sin referencia
-- 3. Listar todas las direcciones que sean menores que 1000
-- 4. Listar todas las direcciones que sean o Av o Pasaje
-- 5. Listar todas las direcciones de los alumnos 1 o que vivan en calles o que no tengan referencias
-- 6. Listar todas las direcciones que sean calle y que su referencia no sea nula y que su alumno sea el 1


-- Para borrar una tabla
DROP TABLE nombre_tabla

