# Generated by Django 4.1.7 on 2023-03-31 02:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_cree_tabla_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('sexo', models.TextField(choices=[('HEMBRA', 'HEMBRA'), ('MACHO', 'MACHO')])),
                ('fechaNacimiento', models.DateField(db_column='fecha_nacimiento')),
                ('alergias', models.TextField()),
                ('foto', cloudinary.models.CloudinaryField(max_length=255, verbose_name='foto')),
                ('cliente', models.ForeignKey(db_column='cliente_id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mascotas',
            },
        ),
    ]
