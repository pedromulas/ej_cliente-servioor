import socket
ip = '127.0.0.1'
puerto = 8081
respuestas = 2

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind((ip, puerto))
    servidor.listen(respuestas)
    while True:
        print('Esperando conexion en {ip},{puerto}'.format(ip = ip, puerto = puerto))
        (cliente, direccion) = servidor.accept()
        print('Se ha conectado alguien')
        c_abierta = True
        while c_abierta:
            resp = cliente.recv(1000).decode('utf-8')
            if resp == 'cierra':
                break
                cliente.close()
            print(resp)
            msg = input('>>')
            msg = str.encode(msg)
            cliente.send(msg)




except KeyboardInterrupt:
    cliente.close()
    print('Cerrando el chat...')
