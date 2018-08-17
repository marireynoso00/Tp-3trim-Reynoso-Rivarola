from conexion import DB
from claseSucursal import Sucursal
from claseCliente import  Cliente
from claseMenu import MenuComida
DB().SetConection('127.0.0.1', 'root', 'alumno', 'mydb')

Sucursal=Sucursal()
Sucursal.idSucursal=2

Cliente=Cliente()
Menuc=MenuComida()

