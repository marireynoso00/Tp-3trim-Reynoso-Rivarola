from conexion import DB

class Sucursal(object):
    idSucursal= None
    NombreSucursal= None
    DireccionSucursal= None


    def AgregarSucursal(self,nombre,direccion):
        self.NombreSucursal=nombre
        self.DireccionSucursal= direccion

        DB().run(" INSERT INTO Sucursal VALUES (NULL, '"+self.NombreSucursal+"','"+self.DireccionSucursal+"');")

    def BorrarSucursal(self,idSucursal):

        DB().run("DELETE FROM Sucursal WHERE idSucursal = "+idSucursal+";")

    def UpdateSucursal(self,nombre,direccion,idS):

        DB().run("UPDATE Sucursal SET NombreSucursal = '"+nombre+"',DireccionSucursal='"+direccion+"' WHERE idSucursal= '"+idS+"';")

    def DeserializarSucursal(self, DiccionarioSucursal ):
        self.idSucursal= DiccionarioSucursal["idSucursal"]
        self.NombreSucursal= DiccionarioSucursal["NombreSucursal"]
        self.DireccionSucursal= DiccionarioSucursal["DireccionSucursal"]