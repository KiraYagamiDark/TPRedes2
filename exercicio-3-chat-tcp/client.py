# Nome: Mateus Alves Silva
# Trabalho 2 - Redes de Computadores 2
# Exercício 3: Cliente do chat em tempo real(TCP e threads)

import socket
import threading

# Função para receber mensagens do servidor em uma thread separada
def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print("\n[Recebido]:", msg)
            if "saiu do chat" in msg.lower():
                break
        except:
            break

# Função para enviar mensagens para o servidor
def send_messages(sock):
    while True:
        msg = input()
        sock.send(msg.encode())
        if msg.lower() == "sair":
            break

def main():
    host = '127.0.0.1'  # IP do servidor
    port = 5000

    # Cria o socket e conecta ao servidor
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Conectado ao servidor. Digite mensagens. Escreva 'sair' para sair.")

    # Inicia a thread para receber mensagens
    threading.Thread(target=receive_messages, args=(client,)).start()

    # Envia mensagens (loop principal)
    send_messages(client)

    # Fecha a conexão
    client.close()

if __name__ == "__main__":
    main()
