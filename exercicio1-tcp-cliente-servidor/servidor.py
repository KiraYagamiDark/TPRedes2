# Exercicio 1 Erik Fernandes dos Santos
#!/usr/bin/env python3  

import socket  # Importa o modulo de sockets para comunicacao via rede

# Define o endereco e a porta onde o servidor vai escutar conexoes
HOST = 'localhost'  # Endereco local (127.0.0.1)
PORT = 50000        # Porta onde o servidor ira escutar

# Cria um socket TCP/IP (SOCK_STREAM indica TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereco e porta definidos
s.bind((HOST, PORT))

# Coloca o socket em modo de escuta, pronto para aceitar conexoes
s.listen()

print('Aguardando conexao')  # Mensagem indicando que o servidor esta esperando uma conexao

# Aceita uma conexao quando um cliente se conecta
conn, ender = s.accept()

print('Conectado em', ender)  # Exibe o endereco do cliente conectado

# Loop principal para comunicacao com o cliente
while True:
    data = conn.recv(1024)  # Recebe ate 1024 bytes de dados enviados pelo cliente
    if not data:
        # Se nao houver dados (cliente desconectou), fecha a conexao
        print('Fechando a conexao')
        conn.close()
        break
    conn.sendall(data)  # Envia de volta 
