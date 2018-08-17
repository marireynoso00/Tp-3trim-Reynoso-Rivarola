from dos import DB
from claseCliente import Cliente
from claseMenu import Menu
from claseEmpleado import Empleado
from claseSucursal import Sucursal

dos=DB()
cliente=Cliente()
menu=Menu()
empleado=Empleado()
Sucursal=Sucursal()

class Menuu(object):
    opcion=None

    @staticmethod
    def MenuMenu():

        while True:

            print("OPCIONES DEL CLIENTE: ")
            print("1) Agregar un cliente")
            print("2) Borrar un clinte")
            print("3) Modificar un cliente")

            print("OPCIONES DEL MENU:")
            print("4)Agregar un menu")
            print("5)Borrar un menu")
            print("6)Modificar un menu")

            print("OPCIONES DEL EMPLEADO: ")
            print("7) Agregar un empleado")
            print("8) Borrar un empleado")
            print("9) Modificas un empleado")

            print("OPCIONES DE SUCURSAL: ")
            print("10) Agregar una sucursal")
            print("11) Borrar un menu")
            print("12) Modificar un menu")

            print("13) Salir del programa")


