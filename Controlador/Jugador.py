import tkinter
from tkinter import messagebox

from modelo.conexionDB import conexion

class Jugador():

    def __init__(self):
        self.contrasena=None
        self.nombre = None
        

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1]== nombreUsuario and usuario[2]== password):
                self.contrasena= usuario[2]
                self.nombre= usuario[1]
                messagebox.showinfo("Informacion","Acceso correcto")
                miConexion.cerrarConexion()
                return

        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseñ a no existen, verifique e intente nuevamente!")
    
    def crearUsuario(self,nombreUsuario,contrasenaUsuario):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuario(nombre,contrasena) VALUES(?,?)",(nombreUsuario,contrasenaUsuario))
        miConexion.cerrarConexion()



    