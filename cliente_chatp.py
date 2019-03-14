import socket
ip = '127.0.0.1'
puerto = 8081

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((ip, puerto))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Bienvenido al chat!')
    c_abierta = True
    while c_abierta:
        msg = input('>>')
        msg = str.encode(msg)
        cliente.send(msg)
        print(cliente.recv(1000).decode('utf-8'))


except KeyboardInterrupt:
    print('Cerrando el chat...')
    msg = 'cierra'
    msg = str.encode(msg)
    cliente.send(msg)
    cliente.close()

except OSError:
    print("Socket already used")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
