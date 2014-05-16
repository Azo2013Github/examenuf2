__author__ = 'jordi martínez'

# ALUMNOS:"
# Desarrollar una clase para gestionar alumnos. Los datos que se quiere gestionar de cada alumno son los siguientes:"
#
# - DNI.
# - Apellidos.
# - Nombre.
# - Lista de asignaturas matriculadas.
# - Importe matrícula.
# - Alumno activo?
#
#El dato 'Alumno activo' sirve para marcar un alumno de forma que no salga en los listados de alumnos. Este marcaje
#se puede hacer con cualquier método que os parezca conveniente: con un caracter especial (*), con una letra (N),
#con un campo True/False, etc.
#
#La clase debe tener, al menos:
#"
# - un método para añadir un nuevo alumno. Los alumnos se añaden con lista de asignaturas vacía, importe matricula 0 y
# marcado como No Activo.
# - un método para mostrar los datos de un alumno si nos dan su DNI.
# - un método para marcar un alumno como activo o inactivo.
#
#Los datos de los alumnos se deben guardar en un único archivo de texto codificado mediante UTF-8.

import os


class Alumno:
    """Clase para gestionar alumnos según los requerimientos del enunciado 1."""


    def __init__(self, archivo):
        """
        Método que informa del archivo en el cual se almacenan los alumnos.
        :param archivo: string -> el nombre del archivo para almacenar alumnos.
        """
        self.archivo = archivo.rstrip()
        self.nombre = ''
        self.apellidos = ''
        self.dni = ''
        self.importe = 0
        self.activo = 'N'
        self.asignaturas = ''

    def nuevo_alumno(self, dni, nombre, apellidos):
        """
        Añade un nuevo alumno al archivo de alumnos (si no existe ya con el mismo DNI).
        :param dni: string -> el DNI del alumno
        :param nombre: string -> el nombre del alumno
        :param apellidos: string -> los apellidos del alumno
        """
        self.dni = dni.rstrip().upper()
        self.nombre = nombre.rstrip()
        self.apellidos = apellidos.rstrip()

        if not self.ver_alumno(dni):
            with open(self.archivo, mode='a', encoding='utf-8') as alumnos:
                nuevo = ''.join(
                    self.activo + ',' + self.dni + ',' + self.nombre + ',' + self.apellidos +
                    ',' + self.asignaturas + ',' + str(self.importe) + '\n')
                alumnos.write(nuevo)

    def ver_alumno(self, dni):
        """
        Muestra los datos almacenados en archivo de un alumno sabiendo su DNI.
        :param dni: string -> el DNI del alumna cuyos datos se van a mostrar.
        :return datos: dictionary -> diccionario con los datos del alumno.
        """
        self.dni = dni.rstrip().upper()
        datos = {}

        with open(self.archivo, mode='r', encoding='utf-8') as alumnos:
            for linea in alumnos:
                activo, dni, nombre, apellidos, asignaturas, importe = linea.rstrip().split(',')
                if dni == self.dni:
                    datos['dni'] = dni
                    datos['nombre'] = nombre.capitalize()
                    datos['apellidos'] = apellidos.capitalize()
                    datos['activo'] = activo.upper()
                    datos['importe'] = float(importe)
                    datos['asignaturas'] = [asignatura for asignatura in asignaturas.split(';')]
                    break

        if datos:
            return datos

    def cambiar_estado(self, dni, estado):
        """
        Cambia el estado del alumno cuyo DNI se indica.
        :param dni: string -> el DNI del alumno cuyo estado se quiere modificar.
        :param estado: character -> N (No activo), A (activo)
        """
        self.dni = dni.rstrip().upper()
        self.activo = estado.rstrip().upper()

        if self.activo in 'NA':
            with open(self.archivo, mode='r', encoding='utf-8') as alumnos, \
                    open('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt', mode='w',
                         encoding='utf-8') as temp:
                for linea in alumnos:
                    activo, dni, nombre, apellidos, asignaturas, importe = linea.split(',')
                    if dni == self.dni:
                        activo = self.activo
                        linea = ''.join(
                            activo + ',' + dni + ',' + nombre + ',' + apellidos + ',' + asignaturas +
                            ',' + str(importe))
                    temp.write(linea)
            os.remove('/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')
            os.rename('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt',
                      '/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')

a = Alumno('/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')
print(a.ver_alumno('37769484B'))