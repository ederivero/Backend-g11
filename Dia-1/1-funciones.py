def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print(saludo)

saludar('Eduardo')

def saludar_varios(*args):
    # cuandos nosotros colocamos en un parametro el '*' significa que no hay limite de ese parametro, este parametro debe de ir al ultimo
    # todos los valores que le pasemos a este parametro se almacenaran en una tupla
    # NOTA: las tuplas, a diferencia de los arreglos, no se pueden modificar osea una vez creadas sus valos no pueden cambiar
    print(args)
    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)

saludar_varios('Roxana', 'Juana', 'Martin', 'Roberto')
saludar_varios('Pedro', 'Luis')
saludar_varios()
saludar_varios('Eduardo', 20, True, 10.5)

def informacion_usuario(**kwargs):
    # kwargs > keyboard argument o se le pasan parametros por llaves
    print(kwargs)
    # .get('llave') > devolver el valor si es que existe la llave, sino existe entonces devolvera None o el segundo parametro que le colocaremos (opcional)
    print(kwargs.get('estatura','NO HAAAAAY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Eduardo', edad= 30, estado_civil='soltero', estatura= 1.88)
informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Colombiana', fecha_nacimiento='31/06/1999')
print('ADIOOOOOOOS')


# recibir dos valores y hacer la division (dividendo / divisor) y retornar su resultado
def dividir(dividendo, divisor):
    # si la division da un error entonces retornar un mensaje que diga 'Division incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        # aqui ingresara cuando la division sea entre 0
        return 'No puede haber division entre 0'
        
    except TypeError:
        # ingresara si la division tiene algun caracter
        return 'Las divisiones solamente pueden ser entre dos numeros'

    except:
        # ingresara si no es ninguno de los dos errores anteriores
        return 'Error desconocido'

valor = dividir(10,5)
print(valor)

valor = dividir(10,0)
print(valor)

valor = dividir('a', 'h')
print(valor)


try:
    valor = dividir(5,)
    print(valor)
except TypeError:
    print('Estuvo mal llamar asi a la funcion')