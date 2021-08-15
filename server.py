#Librerias que utilizaremos
import socket
import sys
from io import open

direccionServidor = "localhost"
puertoServidor = 5555
#coneccion con los sockets
socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
socketServidor.bind( (direccionServidor, puertoServidor) )
socketServidor.listen()
print("Servidor Iniciado") #mensaje que se inicio el servidor
socketConexion, addr = socketServidor.accept()
print("Conectado con cliente", addr) #Se muestra la coneccion con el cliente

#Bucle infinito
while True:
    #mostramos el menu disponible
    menu = """
    Menu
    1- CONSULTA
    2- DEPOSITO + CANTIDAD
    3- Retirar
    """
    socketConexion.send(menu.encode(encoding = "ascii", errors = "ignore")) #enviamos el menu al cliente de forma encode
    recibido = socketConexion.recv(1024)  #Esperamos la respuesta del Cliente
    recibidoCadena = recibido.decode(encoding = "ascii", errors = "ignore") #pasamos la respuesta del cliente a cadena con decode
    print("Se recibio la opcion: ",recibidoCadena) # mostramos que opcion escogio el cliente
    opcion = recibidoCadena.upper()  #Pasamos toda la palabra a mayusculas
    print(recibidoCadena.count(" "))  #Vemos si hay espacios en la cadena
    if recibidoCadena.count(" ") < 1:  #si no hay espacios entra al if
        if  opcion == "CONSULTA" : #si la opcion que mando el cliente es CONSULTA entra en el if
            archivo = open("cuenta.txt", "r") #abrimos el archivo como lectura (read)
            consulta = archivo.read() #guardamos el archivo en la variable consulta
            print(consulta)  #mostramos lo que tiene el archivo
            consultaCadena = "".join(consulta) #pasamos a cadena lo leido del archivo
            socketConexion.send(consultaCadena.encode(encoding = "ascii", errors = "ignore"))  #Enviamos la cadena al cliente
            archivo.close() #Cerramos el archivo
    if recibidoCadena.count(" ") >= 1: # Si tiene 1 o mas espacios entra al if
        recibidoLista = recibidoCadena.split() #Divido la cadena en los espacios que tiene
        opcion = recibidoLista[0] #Guarda la priemra palabra en la variable opcion
        print(recibidoLista) #Muestro que si sea la palabra
        cantidad = int(recibidoLista[1]) #Guardo la cantidad que ingreso el usuario
        print(cantidad) #Muestro la cantidad para ver cual es
        opcionMayusculas = opcion.upper() # Paso la palabra a mayusculas
        if  opcionMayusculas  == "DEPOSITO" : # Si la opcion que llego es deposito entra al if
            archivo = open("cuenta.txt", 'r+' ) # Abro el archivo como lectura y escritura
            deposito = archivo.readlines() # Lee todas las lineas y las guarda como lista en deposito
            print(deposito)
            dinero = deposito[2] #Guardo la cantidad que tiene el archivo
            print(dinero)
            dineroFloat = float(dinero) # Paso la cantidad a flotante y la guardo en su variable
            print (dineroFloat)
            dineroFloat = dineroFloat + cantidad #Realizo la suma  correspondiente al deposito
            print(dineroFloat)
            dineroStr = str(dineroFloat) #Paso el monto final a string para poder escribir en el archivo
            deposito[2] = dineroStr # Escribo en la lista que remplazara al antiguo saldo
            print(deposito[2])
            archivo.seek(0) #Se posiciona al principio de la linea
            archivo.writelines(deposito) #Escribe todo el texto de nuevo ya con las modificaciones
            archivo.close() #Cierra el archivo

socketConexion.close()
