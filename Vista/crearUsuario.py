import tkinter as tk
from tkinter import *
from tkinter import messagebox

class CrearUsuario():

    def guardarUsuario(self, event):
        self.jugador.crearUsuario(self.txtNombre.get(), self.txtContrasena.get())
        messagebox.showinfo("Confirmación", "¡Nuevo usuario registrado con éxito!")

    def limpiarCampos(self):
        self.txtNombre.delete(0, END)
        self.txtContrasena.delete(0, END)

    def __init__(self, menu, jugador):
        self.ventana = tk.Toplevel(menu)
        self.ventana.resizable(0, 0)
        self.ventana.title("Crear Nuevo Usuario")
        self.ventana.config(width=360, height=385)
        self.jugador = jugador

        # Título
        self.lbltitulo = tk.Label(self.ventana, text="Crear Usuario", font=("Arial", 14, "bold"))
        self.lbltitulo.place(relx=0.5, y=40, anchor="center")

        # Campos de entrada
        self.lblNombre = tk.Label(self.ventana, text="Nombre*:", anchor="w")
        self.lblNombre.place(x=50, y=100, width=80, height=25)

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(x=150, y=100, width=160, height=25)

        self.lblContrasena = tk.Label(self.ventana, text="Contraseña*:", anchor="w")
        self.lblContrasena.place(x=50, y=150, width=80, height=25)

        self.txtContrasena = tk.Entry(self.ventana)
        self.txtContrasena.place(x=150, y=150, width=160, height=25)

        # Botones
        self.btnGuardar = tk.Button(self.ventana, text="Guardar")
        self.btnGuardar.place(x=85, y=260, width=80, height=30)
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiarCampos)
        self.btnLimpiar.place(x=195, y=260, width=80, height=30)

        self.ventana.mainloop()
