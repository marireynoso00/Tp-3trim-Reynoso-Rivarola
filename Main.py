from conexion import DB
from claseSucursal import Sucursal
from Menu import Menuu
DB().SetConection('127.0.0.1', 'root', 'alumno', 'mydb')

Sucursall=Sucursal()
Sucursall.idSucursal=2
Menu=Menuu()

Menu.MenuMenu()