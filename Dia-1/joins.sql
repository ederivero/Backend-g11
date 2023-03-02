INSERT INTO direcciones (direccion, numero, referencia, alumno_id) 
                VALUES ('Calle los Tulipanes', 429, 'Al costado de la bodega', NULL);

SELECT * FROM direcciones INNER JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones LEFT JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones RIGHT JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones FULL JOIN alumnos ON direcciones.alumno_id = alumnos.id;


-- Crear una tabla llamada cursos en la cual vamos a tener lo siguiente 
-- nombre TEXT, descripcion VARCHAR(100), habilitado BOOLEAN (id SERIAL)

CREATE TABLE cursos(
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion VARCHAR(100),
    habilitado BOOLEAN
);

-- Un alumno puede tener varios cursos y ademas un curso puede tener varios alumnos
-- Crear una tabla intermedia alumnos_cursos cuyas columnas seran las sgtes:
-- id SERIAL PK, alumno_id INT, curso_id INT y crear su LLaves foraneas 

CREATE TABLE alumnos_cursos(
    id SERIAL PRIMARY KEY,
    alumno_id INT NOT NULL,
    curso_id INT NOT NULL,
    UNIQUE (alumno_id, curso_id),
    CONSTRAINT fk_alumnos FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    CONSTRAINT fk_cursos FOREIGN KEY (curso_id) REFERENCES cursos(id)
);


INSERT INTO cursos (nombre, descripcion, habilitado) VALUES
                    ('Matematica', 'Matematica con algebra', true),
                    ('CTA', 'Cienta Tecnologia y Ambiente', true),
                    ('Comunicacion', 'Letras', true),
                    ('Arte', 'Artes plasticas', false),
                    ('Ingles', 'English for kids', true);

INSERT INTO alumnos_cursos (alumno_id, curso_id) VALUES
                               (1,     1),
                               (2,     1),
                               (1,     3),
                               (3,     4),
                               (3,     2),
                               (3,     3);


-- Haciendo un join desde la tabla alumnos, pasando por la tabla alumnos_cursos y terminando en la tabla cursos
SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id;

-- Si queremos colocar alias a los nombres de las tablas seria de la sgte manera:

SELECT a.nombre FROM
alumnos AS a INNER JOIN alumnos_cursos AS ac
ON a.id = ac.alumno_id
INNER JOIN cursos AS c
ON ac.curso_id = c.id;

-- SELECCIONAR los nombre y apellidos de los alumnos que tenga el curso de comunicacion
SELECT a.nombre, a.apellido
FROM alumnos AS a INNER JOIN alumnos_cursos AS ac ON a.id = ac.alumno_id
INNER JOIN cursos AS c ON ac.curso_id = c.id
WHERE c.nombre = 'Comunicacion';

-- SELECCIONAR todos los cursos que lleve el alumno Eduardo
SELECT c.nombre
FROM alumnos AS a INNER JOIN alumnos_cursos AS ac ON a.id = ac.alumno_id
INNER JOIN cursos AS c ON ac.curso_id = c.id
WHERE a.nombre = 'Eduardo';

-- SELECCIONAR los alumnos cuyos cursos esten habilitados (true) y ademas que esten matriculados (true)
SELECT a.nombre, c.nombre
FROM alumnos AS a INNER JOIN alumnos_cursos AS ac ON a.id = ac.alumno_id
INNER JOIN cursos AS c ON ac.curso_id = c.id
WHERE c.habilitado = true AND a.matriculado = true;
-- Lo mismo pero sin ALIAS
SELECT alumnos.nombre, cursos.nombre
FROM alumnos INNER JOIN alumnos_cursos  ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos ON alumnos_cursos.curso_id = cursos.id
WHERE cursos.habilitado = true AND alumnos.matriculado = true;