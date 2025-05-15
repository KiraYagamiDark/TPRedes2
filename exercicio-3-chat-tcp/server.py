import socket
import threading

clients = []

def handle_client(client, other_client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.lower() == "sair":
                client.send("Você saiu do chat.".encode())
                other_client.send("O outro usuário saiu do chat.".encode())
                client.close()
                other_client.close()
                break
            else:
                other_client.send(msg.encode())
        except:
            break

def main():
    host = '127.0.0.1'  # IP local, ideal no WSL
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)
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
