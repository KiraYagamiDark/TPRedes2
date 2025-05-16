
# Exercicio 1 Erik Fernandes 
#!/usr/bin/env python3 

import socket  # Importa o modulo de sockets para comunicacao em rede

# Define o endereco IP e a porta do servidor ao qual o cliente vai se conectar
HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 50000        # Porta onde o servidor esta escutando

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor no endereço e porta especificados
s.connect((HOST, PORT))

# Envia a mensagem 'Bom dia' para o servidor
# str.encode() converte a string para bytes, que e o formato necessario para envio
s.sendall(str.encode('Bom dia'))

# Recebe ate 1024 bytes da resposta do servidor
data = s.recv(1024)

# Exibe a mensagem recebida (ecoada) decodificando de bytes para string
print('mensagem ecoada', data.decode())

