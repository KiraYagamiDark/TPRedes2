# servidor_udp.py
# Participante: Thais Rosa

import socket

# Configurações do servidor
IP = "127.0.0.1"       # Endereço local (localhost)
PORTA = 6000           # Porta usada para comunicação
BUFFER = 65507         # Máximo de bytes permitido pelo UDP (64 KB - cabeçalhos)

# Criação do socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincula o socket à porta
servidor.bind((IP, PORTA))
print(f"[SERVIDOR] Escutando em {IP}:{PORTA}...")

while True:
    try:
        # Aguarda recebimento de dados
        dados, endereco = servidor.recvfrom(BUFFER)
        mensagem = dados.decode()

        # Mostra mensagem recebida
        print(f"[RECEBIDO de {endereco}] {mensagem}")

        # Envia a mesma mensagem de volta (eco)
        servidor.sendto(dados, endereco)

    except Exception as erro:
        print(f"[ERRO] Falha na comunicação: {erro}")

