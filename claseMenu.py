from conexion import DB
from claseSucursal import Sucursal
class MenuComida(object):
    idMenues= None
    NombreMenu= None
    PrecioMenu= None
    TipoMenu= None
    Sucursal=None

    def AgregarMenu (self,Nombre,precio,tipo,sucursal):
        self.NombreMenu=Nombre
        self.PrecioMenu=precio
        self.TipoMenu=tipo
        self.Sucursal=sucursal

        DB().run("INSERT INTO Menues VALUES (NULL, '"+self.NombreMenu+"','"+self.PrecioMenu+"','"+self.TipoMenu+"','"+str(self.Sucursal.idSucursal)+"');")

    def BorrarMenu(self, id):
        DB().run("DELETE FROM Menues WHERE idMenues = '"+id+"';")

    def UpdateMenu(self,nombre,precio,tipo,aidi):
        DB().run("UPDATE Menues SET NombreMenu= '"+nombre+"', PrecioMenu= '"+precio+"', TipoMenu= '"+tipo+"' WHERE idMenues='"+aidi+"';")

    #deserializar