# Autor: Erik Fernandes dos Santos

# Importa o módulo de sockets para comunicação em rede
import socket

# Define o endereço IP e a porta onde o servidor vai escutar
HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 50000        # Porta onde o servidor vai escutar

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Coloca o socket em modo de escuta, pronto para aceitar conexões
s.listen()

print(f"Servidor ouvindo em {HOST}:{PORT}")

# Loop principal para aceitar e processar conexões de clientes
while True:
    # Aceita uma nova conexão
    conn, addr = s.accept()
    print(f"Conectado por {addr}")

    # Recebe até 1024 bytes de dados do cliente
    data = conn.recv(1024)

    # Verifica se algum dado foi recebido
    if data:
        # Decodifica os dados recebidos de bytes para string e remove espaços em branco
        mensagem = data.decode().strip()
        print(f"Mensagem recebida: {mensagem}")

        # Envia uma confirmação de recebimento para o cliente
        conn.sendall(b"Mensagem recebida")

    # Fecha a conexão com o cliente
    conn.close()

