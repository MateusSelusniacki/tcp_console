import socket
import datetime
import time
import threading

def infinityconn(server):
    #cria looping de conexão com o cliente
    try:
        connection, address = server.accept()
        print(f"Conexão aceita {datetime.datetime.now()}")
        while(1):
            #aceita conexão
            #recebe dados do cliente e transforma em string
            #sending = input()
            sending = "sending sending sending"
            connection.send( sending.encode() )
            content = connection.recv(8192).decode()

            #verifica se ainda há comunicação
            if not content:
                return
            else:
                print('Dado recebido: ' + content)
                with open('ProMarking_txt.txt', 'w') as arquivo:
                    arquivo.write(content)
            #envia dados
            
            
            #Cliente.enviaDadoTCPIP("dado","192.168.56.2",11000)
            print('\n')
    except Exception as E:
            print(f'Erro {E}')
            infinityconn(ip,port)

def thread_func():
    ip = "0.0.0.0"
    port = -1
    while port == -1:
        try:
            port = int(input('Porta: '))
        except:
            print('Porta precisa ser um numero')

    print(f'Esperando no ip: {ip}:{port}')
    #abrindo socket para comunicação TCP/IP
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    #fazendo bind do ip e porta
    server.bind ( (ip,port) )

    #listen
    print("Esperando cliente")
    server.listen(1)
    infinityconn(server)
    
            
threading.Thread(target = thread_func).start()
