
# Exercicio 1 Erik Fernandes 
#!/usr/bin/env python3  # Indica que o script deve ser executado com o interpretador Python 3

import socket  # Importa o módulo de sockets para comunicação em rede

# Define o endereço IP e a porta do servidor ao qual o cliente vai se conectar
HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 50000        # Porta onde o servidor está escutando

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor no endereço e porta especificados
s.connect((HOST, PORT))

# Envia a mensagem 'Bom dia' para o servidor
# str.encode() converte a string para bytes, que é o formato necessário para envio
s.sendall(str.encode('Bom dia'))

# Recebe até 1024 bytes da resposta do servidor
data = s.recv(1024)

# Exibe a mensagem recebida (ecoada) decodificando de bytes para string
print('mensagem ecoada', data.decode())

