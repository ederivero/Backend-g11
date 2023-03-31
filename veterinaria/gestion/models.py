from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from cloudinary.models import CloudinaryField

class ManejoUsuario(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password, tipoUsuario):
        # este metodo se mandara a llamar cuando en la terminal se ponga 'python manage.py createsuperuser'
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        
        # normalize_email > sirve para llevar todo el correo a minusculas y ademas le quita espacios en blanco y verifica si los caracteres son validos 
        # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo = correo_normalizado, nombre = nombre, apellido = apellido, tipoUsuario = tipoUsuario)

        # generamos el hash de nuestra password
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        nuevo_usuario.set_password(password)
        # is_superuser > indica que el usuario tiene la totalidad de privilegios para hacer lo que desee en el panel administrativo
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)

    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    # CharField > varchar(LIMITE)
    # TextField > LIMITE no es necesario a nivel de base de datos
    tipoUsuario = models.TextField(choices=[('ADMIN','ADMIN'), ('CLIENTE', 'CLIENTE')], db_column='tipo_usuario')

    # campos netamente de auth_user
    # is_staff > sirve para indicar al panel administrativo que el usuario no pertenece al grupo de usuarios que pueden acceder
    is_staff = models.BooleanField(default=False)
    # is_active > sirve para indicar que el usuario esta activo y por ende puede ingresar al panel administrativo
    is_active = models.BooleanField(default=True)

    # si queremos ingresar al panel administrativo tenemos que indicar que columna usara para pedir el nombre de usuario
    USERNAME_FIELD = 'correo'

    # Cuando querramos crear un superusuario por la terminal tendremos que indicar que atributos son los que nos debe de solicitar
    # El correo no va porque ya esta definido en USERNAME_FIELD y si lo volvemos a poner nos dara un error, y el password es ya solicitado de manera automatica 
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    objects = ManejoUsuario()
    class Meta:
        db_table = 'usuarios'

class Mascota(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    sexo = models.TextField(choices=[('HEMBRA', 'HEMBRA'), ('MACHO', 'MACHO')])
    fechaNacimiento = models.DateField(db_column='fecha_nacimiento')
    alergias = models.TextField()
    
    # https://cloudinary.com/documentation/image_upload_api_reference#upload_method
    foto = CloudinaryField('foto')

    cliente = models.ForeignKey(to=Usuario, on_delete=models.RESTRICT, db_column='cliente_id')

    class Meta:
        db_table = 'mascotas'