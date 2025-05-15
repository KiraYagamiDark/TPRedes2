# Nome: Mateus Alves Silva
# Trabalho 2 - Redes de Computadores 2
# Exercício 4: Cliente do serviço de requisição de hora

import socket

def main():
    host = '127.0.0.1'  # IP do servidor
    port = 7000		#Porta usada pelo servidor

    # Criação do socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta ao servidor
    cliente.connect((host, port))

    # Envia uma solicitação de hora
    cliente.send("hora".encode())
    # Recebe a resposta com a hora atual
    hora = cliente.recv(1024).decode()
    print(f"Hora recebida do servidor: {hora}")

    # Encerra a conexão
    cliente.close()

if __name__ == "__main__":
    main()
