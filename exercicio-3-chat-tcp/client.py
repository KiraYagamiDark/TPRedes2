import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print("\n[Recebido]:", msg)
            if "saiu do chat" in msg.lower():
                break
        except:
            break

def send_messages(sock):
    while True:
        msg = input()
        sock.send(msg.encode())
        if msg.lower() == "sair":
            break

def main():
    host = '127.0.0.1'  # IP do servidor (no mesmo WSL)
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Conectado ao servidor. Digite mensagens. Escreva 'sair' para sair.")

    threading.Thread(target=receive_messages, args=(client,)).start()
    send_messages(client)

    client.close()

if __name__ == "__main__":
    main()
