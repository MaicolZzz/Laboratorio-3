import mariadb as sql


class conexion():
    def __init__(self):
        self.__host ="localhost"
        self.__user="root"
        self.__password =""
        self.__port = 3307
        self.__database="juego"
        self.__conection = None

    def crearConexion(self):
        self.__conection= sql.connect(
            host= self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database=self.__database
        )
   
    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection= None
    
    #poner aqui los getters y settes
    def getConection(self):
        return self.__conection