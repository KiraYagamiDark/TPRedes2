# cliente_udp.py
# Participante: Thais Rosa

import socket

# Configurações do cliente
IP_SERVIDOR = "127.0.0.1"
PORTA_SERVIDOR = 6000
BUFFER = 65507

# Criação do socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define tempo limite de espera por resposta
cliente.settimeout(3)

print("[CLIENTE] Digite mensagens para enviar ao servidor.")
print("Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("> ")

    if mensagem.lower() == "sair":
        print("[CLIENTE] Encerrando conexão...")
        break

    if len(mensagem.encode()) > BUFFER:
        print("[AVISO] Mensagem excede o limite de 64KB. Reduza o texto.")
        continue

    try:
        # Envia mensagem ao servidor
        cliente.sendto(mensagem.encode(), (IP_SERVIDOR, PORTA_SERVIDOR))

        # Aguarda resposta do servidor (eco)
        resposta, _ = cliente.recvfrom(BUFFER)
        print(f"[ECO] {resposta.decode()}")

    except socket.timeout:
        print("[ERRO] Tempo limite excedido. O servidor não respondeu.")
    except Exception as erro:
        print(f"[ERRO] Falha na comunicação: {erro}")

# Fecha o socket
cliente.close()
