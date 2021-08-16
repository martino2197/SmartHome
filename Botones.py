from tkinter import *
from PIL import ImageTk, Image
ventana = Tk()
ventana.title('Botones')
ventana.iconbitmap(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\icon.png')
ventana.iconbitmap(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\netflix.png')
ventana.iconbitmap(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\Spotify.png')
ventana.iconbitmap(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\Amazon.png')
ventana.iconbitmap(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\HBO.png')

imagen= ImageTk.PhotoImage(Image.open(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\icon.png').resize((100, 100)))
imagen2= ImageTk.PhotoImage(Image.open(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\netflix.png').resize((80, 80)))
imagen3= ImageTk.PhotoImage(Image.open(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\Spotify.png').resize((80, 80)))
imagen4= ImageTk.PhotoImage(Image.open(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\Amazon.png').resize((100, 100)))
imagen5= ImageTk.PhotoImage(Image.open(r'D:\Facultad\SistemasEmbebidos\SmartHome\Botones\HBO.png').resize((80, 80)))
boton1 = Button(image = imagen, width= 80, height=80,relief="flat").place(x=0,y=10)
boton2 = Button(image = imagen2,width= 80, height=80,relief="flat" ).place(x=0,y=150)
boton3 = Button(image = imagen3,width= 80, height=85,relief="flat" ).place(x=0,y=310)
boton4 = Button(image = imagen4,width= 80, height=80,relief="flat" ).place(x=150,y=10)
boton4 = Button(image = imagen5,width= 75, height=75,relief="flat" ).place(x=150,y=145)


ventana.mainloop()