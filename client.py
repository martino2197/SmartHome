import socket


IPServidor ="localhost"
puertoServidor = 5555

socketCliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

print("Cliente iniciado")


while True:
    recibido = socketCliente.recv(1024)
    print("Recibido del Servidor",recibido.decode(encoding = "ascii",errors = "ignore"))
    enviar = input("Escriba la opcion: ")
    #if  enviar == "CONSULTA" or enviar == "consulta":
    socketCliente.send(enviar.encode(encoding = "ascii",errors = "ignore"))


socketCliente.close()
