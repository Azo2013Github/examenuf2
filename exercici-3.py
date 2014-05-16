__author__ = 'jordi martínez'

# MATRICULAS:
# Desarrollar una aplicación que permita matricular alumnos. Para ello desarrollar:
#
# - una función matricular() que reciba un DNI y una asignatura y añada dicha asignatura a la lista de asignaturas
# de dicho alumno. Si el alumno está marcado como No Activo, entonces debe marcarse como activo. La asignatura
# debe existir dentro de la lista de asignaturas existentes. También debe añadir al Importe matrícula del alumno
# el importe de la asignatura, que se calcula multiplicando su número de horas por 6,00.
#
# - una función desmatricular() que reciba un DNI y una asignatura y, si dicha asignatura está en la lista de
# asignaturas # matriculadas del alumno, la elimine de dicha lista. Esto debe restar del Importe matrícula del alumno
# el número de horas de la asignatura por 6,00. Si el alumno no tiene ninguna asignatura, debe estar marcado como
# No Activo.
#
# Estas funciones se desarrollan creando una nueva clase Estudiante que herede todas las propiedas y métodos de
# la clase alumno y adaña los métodos matricular() y desmatricular().
#
# - una función matriculados() que reciba el nombre de una asignatura y muestre el listado de todos los alumnos que la
# hayan matriculado, ordenados por orden alfabético.
#
# Esta función se desarrolla añadiendo el método matriculados() en la clase existente Asignatura.
import os
import re


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


class Asignatura:
    """Clase para gestionar asignaturas según los requerimientos del enunciado 2."""

    def __init__(self, archivo):
        """
        Método que informa a la instancia del archivo de asignaturas.
        :param archivo: string -> el nombre del archivo donde almacenar asignaturas.
        """
        self.archivo = archivo.rstrip()
        self.nombre = ''
        self.horas = 0

    def nueva(self, nombre, horas):
        """
        Método que añade una nueva asignatura en el archivo.
        :param nombre: string -> el nombre de la asignatura.
        :param horas: integer -> el número de horas de la asignatura.
        """
        self.nombre = nombre.rstrip().capitalize()
        self.horas = str(horas).rstrip()

        if not self.ver_asignatura(self.nombre):
            with open(self.archivo, mode='a', encoding='utf-8') as asignaturas:
                nueva = ''.join(self.nombre+','+self.horas+'\n')
                asignaturas.write(nueva)

    def ver_asignatura(self, nombre):
        """
        Muestra los datos de la asignatura sabiendo su nombre.
        :param nombre: string -> el nombre de la asignatura a mostrar.
        :return: datos: dictionary -> los datos de la asignatura.
        """
        self.nombre = nombre.rstrip().capitalize()
        datos = {}

        with open(self.archivo, mode='r', encoding='utf-8') as asignaturas:
            for linea in asignaturas:
                nombre, horas = linea.rstrip().split(',')
                if nombre == self.nombre:
                    datos['nombre'] = nombre.capitalize()
                    datos['horas'] = int(horas)
                    break

        if datos:
            return datos

    def listar(self):
        """
        Muestra un listado ordenado alfabéticamente con las asignaturas existentes.
        """
        datos = []
        with open(self.archivo, mode='r', encoding='utf-8') as asignaturas:
            for linea in asignaturas:
                asignatura, horas = linea.rstrip().split(',')
                datos.append([asignatura, horas])

        ordenado = sorted(datos)
        for dato in ordenado:
            asignatura, horas = dato
            print(asignatura,':', horas, 'horas')

    def matriculados(self, materia):
        """
        Muestra un listado de los alumnos matriculados en una asignatura concreta.
        :param asignatura: string -> el nombre de la asignatura de la que se muestran los matriculados.
        """
        self.nombre = materia.capitalize().rstrip()
        datos_asignatura = self.ver_asignatura(self.nombre)

        if datos_asignatura:
            with open(self.archivo, mode='r', encoding='utf-8') as alumnos:
                for linea in alumnos:
                    activo, dni, nombre, apellidos, asignaturas, importe = linea.rstrip().split(',')
                    if asignaturas:
                        materias = [asignaturas for asignatura in asignaturas.split(';')]
                        if self.nombre in materias:
                            print(nombre+' '+apellidos)


class Estudiante(Alumno):
    """Clase para gestionar matrículas según los requerimientos del enunciado 3."""
    precio = 6.0
    nueva_materia = ''

    def __init__(self, alumnos, asignaturas):
        """
        Prepara los datos del estudiante y enlaza los archivos de alumnos y asignaturas.
        :param alumnos: string -> el archivo de alumnos
        :param asignaturas: string -> el archivo de asignaturas
        """
        super().__init__(alumnos.rstrip())
        self.materia = Asignatura(asignaturas.rstrip())

    def matricular(self, dni, nueva):
        """
        Incorpora la asignatura indicada en la lista de asignaturas del alumno y actualiza su coste de matrícula
        :param dni: string -> el DNI del alumno que se va a matricular
        :param nueva: string -> el nombre de la asignatura en la que se matricula el alumno
        """
        datos_asignatura = {}
        if self.ver_alumno(dni):
            self.dni = dni.upper().rstrip()
            self.nueva_materia = nueva.capitalize().rstrip()

            datos_asignatura = self.materia.ver_asignatura(self.nueva_materia)

            if datos_asignatura:
                with open(self.archivo, mode='r', encoding='utf-8') as alumnos, \
                        open('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt', mode='w',
                             encoding='utf-8') as temp:
                    for linea in alumnos:
                        activo, dni, nombre, apellidos, asignaturas, importe = linea.rstrip().split(',')
                        if dni == self.dni:
                            activo = 'A'
                            materias = [asignatura for asignatura in asignaturas.split(';')]
                            if asignaturas:
                                if self.nueva_materia not in asignaturas:
                                    coste = self.precio * datos_asignatura['horas']
                                    importe = float(importe) + coste
                            else:
                                importe = self.precio * datos_asignatura['horas']
                            materias.append(self.nueva_materia)
                            asignaturas = ';'.join(materias)

                            linea = ''.join(
                                activo + ',' + dni + ',' + nombre + ',' + apellidos + ',' + asignaturas + ',' + str(
                                    importe) + '\n')
                        temp.write(linea)
                os.remove('/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')
                os.rename('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt',
                          '/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')


    def desmatricular(self, dni, nueva):
        """
        Elimina la asignatura indicada de la lista de asignaturas matriculadas por el alumno indicado.
        :param dni: string -> el DNI del alumno a desmatricular
        :param asignatura: string -> la asignatura a eliminar
        """
        datos_asignatura = {}
        if self.ver_alumno(dni):
            self.dni = dni.upper().rstrip()
            self.nueva_materia = nueva.capitalize().rstrip()

            datos_asignatura = self.materia.ver_asignatura(self.nueva_materia)

            if datos_asignatura:
                with open(self.archivo, mode='r', encoding='utf-8') as alumnos, \
                        open('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt', mode='w',
                             encoding='utf-8') as temp:
                    for linea in alumnos:
                        activo, dni, nombre, apellidos, asignaturas, importe = linea.rstrip().split(',')
                        if dni == self.dni:
                            materias = [asignatura for asignatura in asignaturas.split(';')]
                            if asignaturas:
                                if self.nueva_materia in asignaturas:
                                    materias.remove(self.nueva_materia)
                                    asignaturas = ';'.join(materias)
                                    asignaturas = asignaturas[1:]

                                    coste = self.precio * datos_asignatura['horas']
                                    importe = float(importe) - coste

                            linea = ''.join(
                                activo + ',' + dni + ',' + nombre + ',' + apellidos + ',' + asignaturas + ',' + str(
                                    importe) + '\n')
                        temp.write(linea)
                os.remove('/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')
                os.rename('/home/jordi/PycharmProjects/uf2-exord/examenuf2/temp.txt',
                          '/home/jordi/PycharmProjects/uf2-exord/examenuf2/alumnos.txt')


