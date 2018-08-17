from conexion import DB
from claseSucursal import Sucursal

class Cliente(object):
    idCliente=None
    QuejasCliente= None
    MenuPedido= None
    Sucursal =None


    def AgregarCliente(self,queja,pedido,sucursal):
        self.QuejasCliente=queja
        self.MenuPedido=pedido
        self.Sucursal=sucursal

        DB().run("INSERT INTO Clientes VALUES (NULL,'"+self.QuejasCliente+"','"+self.MenuPedido+"','"+str(self.Sucursal.idSucursal)+"');")

    def BorrarCliente(self,id):

        DB().run ("DELETE FROM Clientes WHERE idCliente= '"+id+"';")

    def UpdateCliente(self,queja,pedido):
        DB().run("UPDATE Clientes SET QuejasCliente= '"+queja+"',Menupedido= '"+pedido+"';")

    def DeserializarCliente(self, DiccionarioCliente):
        self.idCliente= DiccionarioCliente["idCliente"]
        self.QuejasCliente= DiccionarioCliente["QuejasCliente"]
        self.MenuPedido= DiccionarioCliente["MenuPedido"]
        self.Sucursal=DiccionarioCliente["Sucursal"]


