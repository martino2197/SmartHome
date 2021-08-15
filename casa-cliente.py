# !/usr/bin/env python3
# Autor: Hernández Albino Edgar Alejandro

# Bibliotecas a utilizar
import tkinter as tk
import socket

# Para añadir los encabezados a cada sección
def title(frame, message):
    label = tk.Label(frame, text=message, fg="#E5E8E8", bg="#282A36",  font=("Bebas Kai", 15))
    label.pack()

# Para agregar los servicios a cada sección
def image(frame, img):
    service = tk.Label(frame, image=img)
    service.pack(pady=10, padx=10)
    service.config(bg="#282A36")
    

def button(frame, img):
    press = tk.Button(frame, image=img, bg="#282A36", activebackground="#F325C1")
    press.pack(padx=10, pady=10)
    return press

# Crea divisiones para la ventana
def frame(parent, relX=0, relY=0):
    divisor = tk.Frame(parent)
    divisor.place(relx=relX, rely=relY, relwidth=0.5)
    divisor.config(bg="#282A36", pady=5, padx=5)
    return divisor

IPServidor ="localhost"
puertoServidor = 5555
socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

def enviar():
    msg = "f1"
    socketCliente.send(msg.encode(encoding = "ascii",errors = "ignore"))

# Clase principal main
def main():

    

    # Creando la ventana
    raiz = tk.Tk()
    raiz.title("Centro Multimedia")
    raiz.resizable(1,1)
    raiz.config(bg="#282A36")
    raiz.geometry("400x950")
    raiz.resizable(width=0, height=0)
    raiz.tk.call('wm', 'iconphoto', raiz._w, tk.PhotoImage(file='img/garaje.png'))  

    # Creación del frame principal
    mainFrame = tk.Frame(raiz)
    mainFrame.pack(fill="both", expand="True")
    mainFrame.config(bg="#282A36")

    # Control del Foco1
    foco1 = frame(mainFrame)
    focoImg = tk.PhotoImage(file="img/foco.png")
    f1 = button(foco1, focoImg)
    title(foco1, "CONTROL DEL FOCO 1")

    # Control del Foco2
    foco2 = frame(mainFrame, 0.5)
    button(foco2, focoImg)
    title(foco2, "CONTROL DEL FOCO 2")
   
    # Control del foco3
    foco3 = frame(mainFrame, 0, 0.2)
    upImg = tk.PhotoImage(file="img/flecha-arriba.png")
    downImg = tk.PhotoImage(file="img/flecha-abajo.png")
    
    b1 = tk.Button(foco3, image=upImg, bg="#282A36", activebackground="#F325C1")
    b1.grid(row=0, column=0)
    b1.config(width=70)

    b2 = tk.Button(foco3, image=downImg, bg="#282A36", activebackground="#F325C1")
    b2.grid(row=0, column=1)
    b2.config(width=70)

    labelF3 = frame(mainFrame, 0.5, 0.25)
    title(labelF3, "CONTROL FOCO 3\n ATENUAR") 

    # Alarma del timbre (recepción desde el servidor)
    timbre = frame(mainFrame, 0, 0.35)
    alarmaImg = tk.PhotoImage(file="img/alarma.png")
    image(timbre, alarmaImg)
    title(timbre, "TIMBRE SONANDO")

    # Control de la cochera
    cochera = frame(mainFrame, 0.5, 0.35)
    cocheraImg = tk.PhotoImage(file="img/garaje.png")
    button(cochera, cocheraImg)
    title(cochera, "CONTROL COCHERA")

    # Alarma del timbre (recepción desde el servidor)
    cam1 = frame(mainFrame, 0, 0.55)
    camImg = tk.PhotoImage(file="img/camara.png")
    button(cam1, camImg)
    title(cam1, "CÁMARA 1")

    # Alarma del timbre (recepción desde el servidor)
    cam2 = frame(mainFrame, 0.5, 0.55)
    button(cam2, camImg)
    title(cam2, "CÁMARA 2")

    # Programado de luces 
    programador = frame(mainFrame, 0, 0.75)
    proImg = tk.PhotoImage(file="img/timer.png")
    button(programador, proImg)
    title(programador, "PROGRAMADO DE LUZ")

    #f1.config(command=enviar())

    # Loop para manterner la ventana
    raiz.mainloop()

# Punto de anclaje de la función main
if __name__ == "__main__":
	main()
