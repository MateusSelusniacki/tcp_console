import socket
import time

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
            cliente.send( input().encode() )
            print('dado enviado')

            #envia requisições para o servidor
            data_get = cliente.recv(8192).decode()
            print(f"Dado recebido: {data_get}")
            with open('ProMarking.txt', 'w') as arquivo:
                arquivo.write(data_get)

    except Exception as E:
        print(f'Conexão com servidor falhou {E}')
        print('insira novamente ip e porta')
        ip = input()
        porta = int(input())
        enviaDadoTCPIP("TCP:Give me string",ip,porta)

ip = input()
porta = int(input())
enviaDadoTCPIP("TCP:Give me string",ip,porta)