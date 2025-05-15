# Nome: Mateus Alves Silva
# Trabalho 2 - Redes de Computadores 2
# Exercício 3: Servidor do chat em tempo real(TCP e threads)

import socket
import threading

clients = []  # Lista para armazenar os dois clientes conectados

# Função que trata um cliente e repassa mensagens ao outro
def handle_client(client, other_client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.lower() == "sair":
                # Envia mensagens de saída para ambos os clientes
                client.send("Você saiu do chat.".encode())
                other_client.send("O outro usuário saiu do chat.".encode())
                client.close()
                other_client.close()
                break
            else:
                # Repassa a mensagem ao outro cliente
                other_client.send(msg.encode())
        except:
            break

def main():
    host = '127.0.0.1'  # IP definido
    port = 5000  # Porta do chat

    # Criação do socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)

    # Espera até que dois clientes se conectem
    print("Servidor ouvindo na porta", port)

    while len(clients) < 2:
        client_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")
        clients.append(client_socket)

    # Criar threads para repassar mensagens entre os dois clientes
    t1 = threading.Thread(target=handle_client, args=(clients[0], clients[1]))
    t2 = threading.Thread(target=handle_client, args=(clients[1], clients[0]))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
