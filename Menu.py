from conexion import DB
from claseCliente import Cliente
from claseMenu import MenuComida
from claseEmpleado import Empleado
from claseSucursal import Sucursal
DB().SetConection('127.0.0.1', 'root', 'alumno', 'mydb')

conexion=DB()
menu=MenuComida()
unEmpleado=Empleado()
UnitaSucursal=Sucursal()

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
            print("11) Borrar una sucursal")
            print("12) Modificar una sucursal")

            print("13) Salir del programa")


            opcion=input("ingrese una opcion: ")

            if opcion == '1':
                queja=input("Digame su queja: ")
                pedido=input("Ustedes pidio: ")
                sucursal=int(input("Usted fue a la sucursal: "))
                unCliente=Cliente()
                unitaSucursal=Sucursal()
                unitaSucursal.getSucursal(sucursal)
                unCliente.AgregarCliente(queja,pedido,sucursal)

            if opcion == '2':
                id=input("ingrese ID a borrar: ")
                unCliente=Cliente()
                unCliente.BorrarCliente(id)

            if opcion == '3':
                id=int(input("id a cambiar: "))
                queja=input("Queja nueva: ")
                pedido=input("menu nuevo: ")
                unCliente=Cliente()
                unitaSucursal=Sucursal()
                unitaSucursal.getSucursal()
                unCliente.UpdateCliente(queja,pedido,id)



            if opcion == '4':
                nombre=input("Nombre del menu: ")
                precio=input("Precio del menu: ")
                tipo=input("Tipo del Menu: ")
                sucursal = int(input("Ingrese la sucursal: "))
                unMenu=MenuComida()
                unitaSucursal=Sucursal()
                unitaSucursal.getSucursal(sucursal)
                unMenu.AgregarMenu(nombre,precio,tipo,sucursal)

            if opcion == '5':
                id=input("Ingrese id del menu a borrar: ")
                unMenu=MenuComida()
                unMenu.BorrarMenu(id)

            if opcion == '6':
                Nombre=input("Ingrese Nombre del nuevo menu: ")
                Precio=input("Ingrese el nuevo precio: ")
                Tipo=input("Ingrese el nuevo tipo: ")
                id=int(input("ID del menu que desea cambiar: "))
                unMenu=MenuComida()
                unMenu.UpdateMenu(Nombre,Precio,Tipo,id)


            if opcion == '7':
                Nombre=input("Ingrese el Nombre: ")
                Apellido=input("Ingrese el Apellido: ")
                DNI=input("Ingrese el DNI: ")
                sucursal=int(input("Ingrese la Sucursal: "))
                unEmpleado=Empleado()
                unitaSucursal=Sucursal()
                unitaSucursal.getSucursal(sucursal)
                unEmpleado.AgregarEmpleado(Nombre,Apellido,DNI,sucursal)


            if opcion == '8':
                id=input("Ingrese el id del empleado a borrar: ")
                unEmpleado=Empleado()
                unEmpleado.BorrarEmpleado(id)

            if opcion == '9':
                Nombre=input("Ingrese el nombre del nuevo empleado: ")
                Apellido=input("Ingrese el apellido del nuevo empleado: ")
                DNI=input("Ingrese el dni del nuevo empleado: ")
                id=int(input("Ingrese el id del empleado que desea modificar: "))
                unEmpleado=Empleado()
                unEmpleado.UpdateEmpleado(Nombre,Apellido,DNI,id)



            if opcion == '10':
                nombre=input("Nombre de la nueva sucursal: ")
                direccion=input("Cual es la direccion?: ")
                unitaSucursal=Sucursal()
                unitaSucursal.AgregarSucursal(nombre,direccion)

            if opcion == '11':
                id=input("Ingrese id de la Sucursal a borrar: ")
                UnitaSucursal=Sucursal()
                UnitaSucursal.BorrarSucursal(id)


            if opcion == '12':
                Nombre=input("Ingrese el nombre de la nueva Sucursal: ")
                Direccion=input("Ingrese la direccion de la nueva Sucursal")
                idS=int(input("Ingrese el id de la sucursal que desea modificar: "))
                unitaSucursal=Sucursal()
                unitaSucursal.UpdateSucursal(Nombre,Direccion,idS)







            if opcion == '13':
                break

