# Erik Fernandes dos Santos
# Importa o módulo de sockets para comunicação em rede
import socket

# Define o endereço IP e a porta do servidor ao qual o cliente vai se conectar
HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 50000        # Porta onde o servidor está escutando

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor no endereço e porta especificados
s.connect((HOST, PORT))

# Solicita ao usuário que digite uma mensagem
mensagem = input("Digite a mensagem: ").strip()

# Verifica se a mensagem não está vazia
if mensagem:
    # Envia a mensagem codificada para bytes
    s.sendall(mensagem.encode())

    # Recebe até 1024 bytes da resposta do servidor
    resposta = s.recv(1024)

    # Exibe a resposta do servidor decodificando de bytes para string
    print(f"Resposta do servidor: {resposta.decode()}")
else:
    # Informa que a mensagem está vazia e não será enviada
    print("Mensagem vazia não enviada.")

# Fecha o socket para encerrar a conexão
s.close()
