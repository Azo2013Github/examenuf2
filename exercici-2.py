__author__ = 'jordi martínez'

#"ASIGNATURAS:
# Desarrollar una clase para gestionar asignaturas. Los datos que se requiere gestionar de cada asignatura son las
#siguientes:
#
# - Nombre.
# - Número de horas.
#
# La clase debe tener, al menos:
#
# - un método para añadir una asignatura.
# - un método para mostrar los datos de una asignatura.
# - un método para listar las asignaturas por orden alfabético.
#
#Los datos de las asignaturas se deben guardar en un único archivo de texto codificado mediante UTF-8.


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
        :param nombre:
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
