# Entornos virtuales python

## Crear un entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
```

## Desactivar el entorno virtual

```
deactivate
```

# Flask

## Instalar flask

```
pip install Flask
```

## Verificamos que flask se haya instalado

```
pip freeze
```

## Listar las librerias en el archivo `requirements.txt`

```
pip freeze > requirements.txt
```

## Instalar las librerias que están listados en nuestro `requirements.txt`

```
pip install -r requirements.txt
```