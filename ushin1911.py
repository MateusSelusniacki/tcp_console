import socket
import time
import datetime

def enviaDadoTCPIP(data, host, port):
    #abrindo socket para comunicação TCP/IP
    cliente = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    #conecta no servidor
    try:
        cliente.connect( ( host, port ) )
        print('conectado')
        while(1):
            print('\n')  
            #envia requisições para o servidor
            data_get = cliente.recv(8192).decode()
            print(f"Dado recebido: {data_get} - {datetime.datetime.now()}")
            with open('p.txt', 'w') as arquivo:
                arquivo.write(data_get)
            with open('Log.txt', 'a') as arquivo:
                arquivo.write(data_get + " - " +  str(datetime.datetime.now()) + "\n")

            cliente.send( "recebido".encode() )

    except Exception as E:
        print(f'Conexão com servidor falhou {E}')
        #ip = '192.168.10.100'
        ip = '127.0.0.1'
        porta = 4000
        time.sleep(0.5)
        enviaDadoTCPIP("TCP:Give me string",ip,porta)

ip = '127.0.0.1'
#ip = '192.168.10.100'
porta = 4000
enviaDadoTCPIP("ReqCode",ip,porta)