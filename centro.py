#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# aud.py
#
# Centro multimedia, con servicio de streaming
#
# Autor: Torres López José Antonio
# License: MIT
#
# ## ###############################################

import pygame #Con esta clase controlamos la reproducción de archivos de audio
import threading #Con esta clase controlamos hilos
import vlc #Con esta clase controlamos el reproductor de archivos multimedia vlc
import os #Usaremos esta clase para poder listar la lista de archivos del sistema
from tkinter import* #Esta clase servirá para poder realizar una interfaz grafica
import webbrowser #Con esta clase mediante un navegador nos conectara a una paginá de internet
                  #para el servicio de streaming(Netflix y Spotify)
"""Con el método buscar, se revisará si el archivo fichero
termina con la extensión dada por una lista de archivos permitidos.
Se recorre la lista y si el archivo termina con alguna de las
extensiones permitidas regresa un valor de True, sino sigue recorriendo
la lista y si no encuentra un valor permitido regresa un False"""
def buscar(a,fichero):
    for i in range(len(a)):#Recorre la lista a
        if fichero.endswith(a[i]):#Revisa si el archivo termina con una extensión dada por la lista a
            return True#Regresa un valor de True si el archivo termina con una extensión de la lista a
    return False#Si el archivo no tiene una extensión valida regresa un false
"""Con el método encontrar se analiza el contenido
de la carpeta /media/pi/, donde se montará nuestra unidad USB.Se listan
las carpetas de /media/pi y si no contienen nada regresa una lista vacía,
sino revisa el contenido de la memoria y se analiza con una lista con las
extensiones validas, se revisa si el contenido es un archivo y con el
método buscar verifica si tiene una extensión valida, si se
cumplen ambas condiciones se agrega en una lista y al final se devuelve esa
lista
"""
def encontrar(entrada):
    contenido2=os.listdir('/media/pi/')#Se lista el contenido de la carpeta /media/pi
    '''Se lista el directorio para saber si está conectado alguna USB, si la lista esta
    vacía regresa una lista vacía'''
    if len(contenido2)==0:#Si la lista contenido 2 esta vacía
        return contenido2 #Regresa una lista vacía
    '''Si está conectada una memoria la variable contenido tiene la lista de los
    nombres de las carpetas de las USB. Se escoge la primera USB y
    se concatena con /media/pi/ para obtener el contenido de la USB'''
    contenido=os.listdir('/media/pi/'+contenido2[0])#Se obtiene el contenido de /media/pi+contenido2[0]
    arreglo=[]#Arreglo sera una lista vacía
    """Revisa todos los archivos de la memoria y verifica si
        es un archivo y si cumple con la extensión
        que está determinada por la lista entrada"""
    for fichero in contenido:# Se recorre la lista contenido
                            #con cada cadena fichero de la lista contenido
        if os.path.isfile(os.path.join('/media/pi/'+contenido2[0],fichero))and buscar(entrada,fichero): #Si la ruta de /media/Pi+contenido2[0] es un archivo
                                                                                                        #y el método buscar regresa un True
            arreglo.append(fichero)#La lista arreglo agrega el valor de fichero
    return arreglo#Regresa la lista arreglo
"""Creamos la clase ventana la cual creara una interfaz gráfica para
   la primera ventana de selección, con tres botones Netflix, Spotify
   o memoria USB"""
class Ventana:
    #Constructor de la ventana
    def __init__(self,maestro):
        self.maestro=maestro#El atributo maestro se inicializa con el
                            #valor mandado por el constructor, que es un
                            #objeto Tk, el cual permite crear ventanas con
                            #diferentes objetos dentro de ella
        self.omega=0#El atributo omega se inicializa en cero
        maestro.title("Interfaz Maestro")#Ponemos el título a la ventana
        self.boton=Button(maestro,text="Netflix",command=self.youtube)#Instanciamos un botón, con el texto
                                                                        #Netflix y el comando youtube
        self.boton.pack()#Coloca el botón
        self.boton1=Button(maestro,text="Spotify",command=self.spt)#Instanciamos un botón, con el texto
                                                                        #Spotify y el comando spt
        self.boton1.pack()#Coloca el botón
        self.boton2=Button(maestro,text="Memoria",command=self.memoria)#Instanciamos un botón, con el texto
                                                                        #Memoria y el comando memoria
        self.boton2.pack()#Coloca el botón
        self.boton3=Button(maestro,text="Salir",command=self.salir)#Instanciamos un botón, con el texto
                                                                        #Salir y el comando salir
        self.boton3.pack()#Coloca el botón
    """En estas sección se muestran los métodos que se activan al presionar los
    botones"""
    def youtube(self):
        self.omega=1#Se le asigna al atributo omega 1
        self.maestro.destroy()#Destruye la ventana
    def spt(self):
        self.omega=2#Se le asigna al atributo omega 2
        self.maestro.destroy()#Destruye la ventana
    def memoria(self):
        self.maestro.destroy()#Destruye la ventana
    def salir(self):
        self.omega=4#Se le asigna al atributo omega 4
        self.maestro.destroy()#Destruye la ventana
    """Método auxiliar para obtener el atributo omega"""
    def dev(self):
        return self.omega#Regresa el atributo omega
"""Segunda ventana para seleccionar los archivos multimedia de la
    memoria USB"""
class Ventana2:
    #Constructor de la segunda ventana
    def __init__(self,maestro,elec):
        self.maestro=maestro
        maestro.title("Interfaz Memoria")
        a=[".mp3"] #Lista que contiene las extensiones aceptadas para archivo de audio
        arr=encontrar(a)#Mediante el método encontrar obtenemos la lista con los nombres
                        #de los archivos de audio
        b=[".mp4"]#Lista que contiene las extensiones aceptadas para archivo de video
        arr2=encontrar(b)#Mediante el método encontrar obtenemos la lista con los nombres
                        #de los archivos de video
        c=[".jpg",".png",".jfif"]#Lista que contiene las extensiones aceptadas para archivo de imagenes
        arr3=encontrar(c)#Mediante el metodo encontrar obtenemos la lista con los nombres
                        #de los archivos de imágenes
        '''Si no hay nada en la memoria o no hay memoria entrara al siguiente
        if, en la ventana solo habrá una etiqueta y un botón para salir'''
        if(len(arr)==0 and len(arr2)==0 and len(arr3)==0):
            self.lab=Label(maestro,text="No hay contenido")#Pone una etiqueta con el texto "no hay contenido
            self.lab.pack()
            self.salir=Button(maestro,text="Salir",command=self.salir)#Instanciamos un botón, con el texto
                                                                        #Salir y el comando salir
            self.salir.pack()
        if(len(arr)!=0):
            self.boton=Button(maestro,text="Musica",command=self.youtube)#Instanciamos un botón, con el texto
                                                                        #Música y el comando youtube
            self.boton.pack()
        if(len(arr2)!=0):
            self.boton=Button(maestro,text="Imagenes",command=self.spt)#Instanciamos un botón, con el texto
                                                                        #Imágenes y el comando spt
            self.boton.pack()
        if(len(arr3)!=0):
            self.boton=Button(maestro,text="Video",command=self.memoria)#Instanciamos un botón, con el texto
                                                                        #Video y el comando memoria
            self.boton.pack()
    def youtube(self):
        self.elec=1#Se le asigna al atributo elec 1
        self.maestro.destroy()#Destruye la ventana
    def spt(self):
        self.elec=2#Se le asigna al atributo elec 2
        self.maestro.destroy()#Destruye la ventana
    def memoria(self):
        self.elec=3#Se le asigna al atributo elec 3
        self.maestro.destroy()#Destruye la ventana
    def regresa(self):
        return self.elec#Regresa el valor elec
    def salir(self):
        self.elec=5#Se le asigna al atributo elec 5
        self.maestro.destroy()#Destruye la ventana
'''Crea la ventana para el control del contenido de contenido de audio
de la memoria'''
class Ventana3:
    def __init__(self,maestro,n):
        self.maestro=maestro
        self.i=0
        self.aux=True
        self.ban=True
        self.n=n
        maestro.title("Reproductor de audio")
        pygame.mixer.music.load(self.n[self.i])#Carga el archivo de audio
        pygame.mixer.music.play()#Se reproduce el archivo cargado
        self.boton=Button(maestro,text="Pausa",command=self.youtube)#Instanciamos un botón, con el texto
                                                                        #Pausa y el comando youtube
        self.boton.pack()
        self.boton1=Button(maestro,text="Adelantar",command=self.spt)#Instanciamos un botón, con el texto
                                                                        #Adelantar y el comando spt
        self.boton1.pack()
        self.boton2=Button(maestro,text="Atrasar",command=self.retro)#Instanciamos un botón, con el texto
                                                                        #Atrasar y el comando retro
        self.boton2.pack()
        self.boton3=Button(maestro,text="Salir",command=self.memoria)#Instanciamos un botón, con el texto
                                                                        #Salir y el comando memoria
        self.boton3.pack()
    '''Si se presiona el botón de pausa se pausa o reanuda la música dependiendo
        del atributo ban'''
    def youtube(self):
        '''Si ban es True la música esta reproduciendoce y se quiere pausar'''
        if(self.ban==True):
            pygame.mixer.music.pause()#Pausa el audio
            self.ban=False#Pone al atributo ban en False
            '''Si ban es False la música esta en pausa y se quiere reproducir'''
        else:
            pygame.mixer.music.unpause()#Reanuda el audio
            self.ban=True#Pone al atributo ban en True
    '''El método spt sirve para que, al presionar adelantar, la música cargue
    el siguiente audio de la memoria y lo reproduzca, si la lista está en el
    ultimo audio de la lista se regresa al primer valor de la lista'''
    def spt(self):
        self.i=self.i+1 #Incrementa el valor del atributo i en 1
                        #este es el índice de la lista de archivos de
                        #de audio
        '''Si el valor i es menor al tamaño de la lista se debe
        de detener y pasar al siguiente valor de la lista y reproducirlo'''
        if(self.i<len(self.n)):
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
            '''En caso contrario, significa que se llegó al límite de la lista
            y se debe de reiniciar desde cero'''
        else:
            self.i=0#Se reinicia el índice de la lista
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
    '''El método reto sirve para que al presionar atrasa, el reproductor cargue
    el siguiente video de la memoria y lo reproduzca, si la lista está en el
    primer video de la lista se va al último valor de la lista'''
    def retro(self):
        self.i=self.i-1#Incrementa el valor del atributo i en 1
                        #este es el índice de la lista de archivos de
                        #de audio
        '''Si el valor i es mayor o igual a 0 se debe
        de detener y pasar al anterior valor de la lista y reproducirlo'''
        if(self.i>=0):
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
            '''En caso contrario, significa que i vale 0 y por ende al disminuirlo en 1
            se obtiene un índice negativo generando un error por ende, se debe de reiniciar desde el ultimo
            valor de la lista'''
        else:
            self.i=len(self.n)-1#Al índice se le asigna el tamaño de la lista menos 1
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
    """Sale del menú de audio"""
    def memoria(self):
        self.maestro.destroy()#Destruye la ventana
        self.aux=False#El atributo aux se pone en falso, este
                        #se utilizará en otro método, para terminar
                        #la secuencia de un hilo
        pygame.mixer.music.stop()#Se detiene la pista
    def devolver(self):
        return self.aux#Este método regresa aux, que servirá para terminar un
                        #hilo en otro método
    '''El método devolveri y poneri servirá para que otro método que funciona con
un hilo pueda cambiar el valor de i para que cuando termine una pieza de la lista
se reproduzca la siguiente pista'''
    def devolveri(self):
        return self.i#Regresa i
    def poneri(self,a):
        self.i=a#Pone i
'''Con el método concatena se recorre la lista
de entrada n, que tendrá la lista de los nombres
de los archivos multimedia y a cada valor de esa
lista se le concatenara la ruta completa donde
se encuentra ese archivo en la USB y regresara la
lista'''
def concatena(n):
    for i in range(len(n)):
        contenido=os.listdir('/media/pi/')#Se obtiene el contenido
                                            #de la carpeta /media/pi
                                            #para obtener el nombre de la memoria USB
        n[i]="/media/pi/"+contenido[0]+"/"+n[i]#Se concatena el nombre del archivo
                                                #con la ruta completa de los archivos de la memoria USB
    return n #Regresa la nueva lista
class Ventana4:
    #Constructor de Ventana para el control de imágenes
    def __init__(self,maestro,n):
        self.maestro=maestro
        self.i=0
        self.n=n
        maestro.title("Reproductor de Imagenes")
        self.media=vlc.MediaPlayer(self.n[self.i])#Se crea el objeto media, con el
                                                #el archivo de la lista n en su posición i
        self.media.play()#Se manda a reproducir el archivo
        self.boton1=Button(maestro,text="Adelantar",command=self.spt)#Instanciamos un botón, con el texto
                                                                        #Adelantar y el comando spt
        self.boton1.pack()
        self.boton2=Button(maestro,text="Atrasar",command=self.retro)#Instanciamos un botón, con el texto
                                                                        #Atrasar y el comando retro
        self.boton2.pack()
        self.boton3=Button(maestro,text="Salir",command=self.memoria)#Instanciamos un boton, con el texto
                                                                        #Salir y el comando memoria
        self.boton3.pack()
    '''Adelanta a la siguiente imagen de la lista, si i llega al valor de tamaño de la
    lista+1 el indice de la lista se reinicia(i=0)'''
    def spt(self):
        self.media.stop()#Detiene el contenido multimedia
        self.i=self.i+1#Incrementa el valor del índice en 1
        '''Si el valor es menor al tamaño de la lista solo
        carga el siguiente valor de la lista y la reproduce'''
        if(self.i<len(self.n)):
            self.media=vlc.MediaPlayer(self.n[self.i])#Carga el valor de n[i] para poder
                                                    #utilizarlo en el reproductor multimedia
            self.media.play()#Reproduce el archivo
            '''Sino se reinicia el valor de i en 0 se carga el valor
            de la lista y la reproduce'''
        else:
            self.i=0#Reinicia indice
            self.media=vlc.MediaPlayer(self.n[self.i])#Carga el valor de n[i] para poder
                                                    #utilizarlo en el reproductor multimedia
            self.media.play()#Reproduce el archivo
    '''Retrocede a la anterior imagen de la lista, si i es menor a cero
    el valor de i toma el valor del tamaño de la lista-1, para reproducir la última imagen de la lista'''
    def retro(self):
        self.i=self.i-1#Se decrementa i en uno
        self.media.stop()#Se detiene el contenido multimedia
        if(self.i>=0):
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo multimedia
                                                        #para reproducirlo
            self.media.play()#Se reproduce el archivo
        else:
            self.i=len(self.n)-1#El valor de i toma el valor de tamaño de la lista-1
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo multimedia
                                                        #para reproducirlo
            self.media.play()#Se reproduce el archivo
    '''Sale del reproductor de imágenes'''
    def memoria(self):
        self.maestro.destroy()#Destruye la ventana
        self.media.stop()#Detiene el contenido multimedia
class Ventana5:
    def __init__(self,maestro,n):
        self.maestro=maestro
        self.i=0
        self.aux=True
        self.ban=True
        self.n=n
        maestro.title("Reproductor de video")
        self.media=vlc.MediaPlayer(self.n[self.i])#Se crea el objeto media, con el
                                                #el archivo de la lista n en su posición i
        self.media.play()#Se manda a reproducir el archivo
        self.boton1=Button(maestro,text="Adelantar",command=self.spt)#Instanciamos un botón, con el texto
                                                                        #Adelantar y el comando spt
        self.boton1.pack()
        self.boton2=Button(maestro,text="Atrasar",command=self.retro)#Instanciamos un botón, con el texto
                                                                        #Atrasar y el comando retro

        self.boton2.pack()
        self.boton4=Button(maestro,text="Pausar",command=self.pausa)#Instanciamos un botón, con el texto
                                                                        #Pausar y el comando pausa
        self.boton4.pack()
        self.boton3=Button(maestro,text="Salir",command=self.memoria)#Instanciamos un botón, con el texto
                                                                        #Salir y el comando memoria
        self.boton3.pack()
    '''Si se presiona el botón de pausa se pausa o reanuda el video dependiendo
        del atributo ban'''
    def pausa(self):
        '''Si ban es True el video esta reproduciéndose y se quiere pausar'''
        if(self.ban==True):
            self.media.set_pause(1)#Se pausa el video
            self.ban=False#La bandera se pone en False para que cuando se
                            #oprima el botón ahora reanude el video
        else:
            self.media.play()#Se reanuda el video
            self.ban=True#La bandera se pone en True para que cuando se
                            #oprima el botón ahora pause el video
    '''El método spt sirve para qué al presionar adelantar, el reproductor cargue
    el siguiente video de la memoria y lo reproduzca, si la lista está en el
    ultimo audio de la lista se regresa al primer valor de la lista'''
    def spt(self):
        self.media.stop()#Detiene el contenido
        self.i=self.i+1#Incrementa en uno el índice
        '''Si el valor i es menor al tamaño de la lista se debe
        de detener y pasar al siguiente valor de la lista y reproducirlo'''
        if(self.i<len(self.n)):
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo de video en un
                                                    #nuevo objeto MediaPlayer
            self.media.play()#Reproduce el archivo multimedia
            '''En caso contrario, significa que se llegó al límite de la lista
            y se debe de reiniciar desde cero'''
        else:
            self.i=0#Reinicia el valor de i en cero
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo de video en un
                                                    #nuevo objeto MediaPlayer
            self.media.play()#Reproduce el archivo multimedia
    '''El método reto sirve para que al presionar atrasa, el reproductor cargue
    el siguiente video de la memoria y lo reproduzca, si la lista está en el
    primer video de la lista se va al último valor de la lista'''
    def retro(self):
        self.i=self.i-1
        self.media.stop()
        '''Si el valor i es mayor o igual a 0 se debe
        de detener y pasar al anterior valor de la lista y reproducirlo'''
        if(self.i>=0):
            self.media=vlc.MediaPlayer(self.n[self.i])
            self.media.play()
            '''En caso contrario, significa que i vale 0 y por ende al disminuirlo en 1
            se obtiene un índice negativo generando un error, por ende, se debe de reiniciar desde el ultimo
            valor de la lista'''
        else:
            self.i=len(self.n)-1
            self.media=vlc.MediaPlayer(self.n[self.i])
            self.media.play()
    def memoria(self):
        self.maestro.destroy()#Destruye la ventana
        self.media.stop()#Detiene el video
'''El siguiente método se ocupará en un hilo. Para
que mientras la ventana este en su mainloop, este método
se encargue de cambiar el audio cuando termine de reproducirse
el audio anterior.
Para ello eran necesarios los métodos poneri obteneri y devolver, para saber que índice se está utilizando y ponerlo
en el atributo i de la clase ventana, para cuando los botones lo
requieran'''
def incrementar(num,**datos):
    while (datos['inicio'].devolver()):#Cuando se oprima el botón salir
                                        #devolver regresara un falso, mientras
                                        #se realizará este ciclo
        #print(pygame.mixer.music.get_busy())
        if(pygame.mixer.music.get_busy()==0):#Pregunta si no se esta reproduciendo algo
            a=datos['inicio'].devolveri()#Se obtiene del objeto de la clase ventana i y se guarda en a
            '''Se analiza si el valor de i llego al tamaño del arreglo menos 1'''
            if(a==len(datos['arreglo'])-1):
                a=-1#Se le asigna -1 a "a"
            a=a+1#Se incrementa el índice para obtener el siguiente audio
            datos['inicio'].poneri(a)#Se poner el valor de i en el objeto de la clase ventana
                                    #para que pueda ser usado por los métodos de los botones
            pygame.mixer.music.load(datos['arreglo'][a])#Carga el nuevo archivo de audio
            pygame.mixer.music.play()#Reproduce el audio
            '''Así cuando termina de reproducirse un audio comienza el otro'''
    '''Cuando se sale de la ventana se debe detener el audio'''
    pygame.mixer.music.stop()#Detiene el audio
    pygame.mixer.quit()#Elimina el objeto que permitía reproducir música
                        #para poder recuperar el audio que este acaparaba
'''Se inicializa una bandera en True para tener un ciclo, que empiece con la
primera ventana y pase a las siguientes ventanas y repita el proceso
hasta que se salga con el botón salir de la primera ventana'''
bandera=True
while(bandera):
    '''Creamos una ventana'''
    root=Tk()
    a=0
    root.attributes("-zoomed",True)#Con esta instruccion ocupamos la pantalla completa, para
                                    #la ventana
    vent=Ventana(root)#Se crea el objeto vent de la clase ventana con el argumento root
    '''Esto para agregarle las funcionalidades a la ventana'''
    root.mainloop()#Ponemos en un ciclo a la ventana, para que se rompa cuando se destruye
                    #la ventana
    valor=vent.dev()#Obtenemos con el método dev un entero
    '''Que se ocupara para seleccionar hacia donde debe ir el programa si a Netflix Spotify o al
    contenido de la memoria'''
    '''Valor 0 memoria'''
    if valor==0:
        r=[".mp3"]
        arr=encontrar(r)
        b=[".mp4"]
        arr2=encontrar(b)
        c=[".jpg",".png",".jfif"]
        arr3=encontrar(c)
        '''Se analiza si solo se contiene un solo tipo de
        archivos, entiendase archivos como video, musica o imagenes.Para
        pasar directamente a reproducir ese tipo de archivos'''
        if len(arr)!=0 and len(arr2)==0 and len(arr3)==0:
            a=1
        elif len(arr)==0 and len(arr2)!=0 and len(arr3)==0:
            a=3
        elif len(arr)==0 and len(arr2)==0 and len(arr3)!=0:
            a=2
            '''En dado que no sea el caso, se debe de lanzar la segunda
            ventana para elegir que archivo reproducirá'''
        else:
            root=Tk()
            a=0
            root.attributes("-zoomed",True)
            vent=Ventana2(root,a)

            root.mainloop()
            a=vent.regresa()#Este valor determina que archivo se
                            #reproducirá
        '''a==1 es audio'''
        if a==1:
            ent=pygame.mixer.init()#Instancia el reproductor de música
            a=[".mp3"]#Lista con la extensión de los archivos permitidos para audio
            arr=encontrar(a)
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de los audios
            vent=Ventana3(root,arr)
            '''Se instancia un hilo, para poder ejecutar el método para reproducir cuando
            se acabe un audio el siguiente audio'''
            inicia=threading.Thread(target=incrementar,args=(2,),kwargs={'inicio':vent,'arreglo':arr})
            inicia.start()#Inicia hilo
            root.mainloop()#Loop de la ventana hasta que se elimine
            '''a==2 imágenes'''
        elif a==2:
            a=['.jpg','.png','.jfif']#Lista con la extensión de los archivos permitidos para imágenes
            arr=encontrar(a)#Se encuentra la lista de los nombres de los archivos validos
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de las imágenes
            vent=Ventana4(root,arr)
            root.mainloop()
            '''a==3 video'''
        elif a==3:
            a=['.mp4']#Lista con la extensión de los archivos permitidos para videos
            arr=encontrar(a)#Se encuentra la lista de los nombres de los archivos validos
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de los videos
            vent=Ventana5(root,arr)
            root.mainloop()
        '''Se eligio Netflix'''
    elif(valor==1):
        '''Como el navegador chrome no se encuentra registrado, se
        deben ejecutar las siguientes tres líneas para poder usarlo'''
        comando="/usr/bin/chromium-browser %s"#Se guarda la ubicación del navegador
                                            #Chrome
        nav=webbrowser.get(comando)#Se utiliza el método get para obtener el navegador
        webbrowser.register("chrome",None,nav)#Con este método se registra el navegador Chrome
                                                #con el nombre de chrome
        nav=webbrowser.get("chrome")#Se obtiene el navegador para utilizarlo
        nav.open("https://www.netflix.com/mx/login")#Con esta instrucción se abre la pagina
                                                       #de Netflix con Chrome
        '''Se eligio Spotify'''
    elif(valor==2):
        '''Como el navegador chrome no se encuentra registrado, se
        deben ejecutar las siguientes tres líneas para poder usarlo'''
        comando="/usr/bin/chromium-browser %s"#Se guarda la ubicación del navegador
                                            #Chrome
        nav=webbrowser.get(comando)#Se utiliza el método get para obtener el navegador
        webbrowser.register("chrome",None,nav)#Con este método se registra el navegador Chrome
                                                #con el nombre de chrome
        nav=webbrowser.get("chrome")#Se obtiene el navegador para utilizarlo
        nav.open("https://accounts.spotify.com/es/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=es-MX")#Con esta instrucción se abre la pagina
                                                       #de Spotify con Chrome
        '''Se quiere salir'''
    else:
        bandera=False#Para terminar con el ciclo while