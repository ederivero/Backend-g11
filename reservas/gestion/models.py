from django.db import models

class Categoria(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#module-django.db.models.fields
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)

    class Meta:
        # sirve para modificar alguna configuracion de la tabla en nuestra bd
        db_table = 'categorias'