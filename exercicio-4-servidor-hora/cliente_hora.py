import socket

def main():
    host = '127.0.0.1'  # ou IP do servidor
    port = 7000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    cliente.send("hora".encode())
    hora = cliente.recv(1024).decode()
    print(f"Hora recebida do servidor: {hora}")

    cliente.close()

if __name__ == "__main__":
    main()
