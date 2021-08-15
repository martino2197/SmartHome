# !/usr/bin/env python3
# Autor: Hernández Albino Edgar Alejandro

# Bibliotecas a utilizar
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import socket

# Crea divisiones para la ventana
def frame(parent, a=0, b=0):
    divisor = tk.Frame(parent)
    divisor.place(x=a, y=b, relwidth=0.3, relheight=0.9)
    divisor.config(bg="#282A36")
    return divisor

# Para agregar los servicios a cada sección
#def createLight(frame, canvas, x1, y1, x2, y2, **kwargs):


# Clase principal main
def main():

    #direccionServidor = "localhost"
    #puertoServidor = 5555
    #coneccion con los sockets
    #socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    #socketServidor.bind( (direccionServidor, puertoServidor) )
    #socketServidor.listen()
    #print("Servidor Iniciado") #mensaje que se inicio el servidor
    #socketConexion, addr = socketServidor.accept()
    #print("Conectado con cliente", addr) #Se muestra la coneccion con el cliente


    # Creando la ventana
    raiz = tk.Tk()
    raiz.title("Centro Multimedia")
    raiz.resizable(1,1)
    raiz.config(bg="#282A36")
    raiz.geometry("900x800")
    raiz.resizable(width=0, height=0)
    raiz.tk.call('wm', 'iconphoto', raiz._w, tk.PhotoImage(file='img/garaje.png'))  

    # Creación del frame principal
    mainFrame = tk.Frame(raiz)
    mainFrame.pack(fill="both", expand="True")

    # Fondo del frame 
    casa = tk.PhotoImage(file="img/casa.png") 
    c = Canvas(mainFrame, width=900, height=800)
    c.pack(fill="both", expand="True")
    c.create_image(0,0, image=casa, anchor="nw")

    # Para crear la iluminación de los focos
    i = tk.PhotoImage(file="img/circle.png")
    c.create_image(185,370, image=i)

    j = tk.PhotoImage(file="img/circle1.png")
    c.create_image(645, 210, image=i)

    c.create_image(435, 500, image=j)

    # Timbre
    #timbre = frame(mainFrame,450,400) 
    timbreImg = tk.PhotoImage(file="img/timbre.png")
    b1 = tk.Button(mainFrame, image=timbreImg, bg="#282A36", activebackground="#F325C1")
    b1.place(x=490, y=470)
    
    while True:
        #recibido = socketConexion.recv(1024)  #Esperamos la respuesta del Cliente
        #recibidoCadena = recibido.decode(encoding = "ascii", errors = "ignore") #pasamos la respuesta del cliente a cadena con decode
        #print("Se recibio la opcion: ",recibidoCadena)
        print("Se recibio la opcion")
        # Loop para manterner la ventana
        raiz.mainloop()

# Punto de anclaje de la función main
if __name__ == "__main__":
	main()

