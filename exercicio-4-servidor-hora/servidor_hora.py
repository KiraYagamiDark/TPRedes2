import socket
import threading
import datetime

def atender_cliente(conexao, endereco):
    try:
        print(f"[LOG] Conexão recebida de {endereco}")
        while True:
            requisicao = conexao.recv(1024).decode()
            if not requisicao:
                break

            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
            conexao.send(hora_atual.encode())

            print(f"[LOG] Hora enviada para {endereco}: {hora_atual}")
    except Exception as e:
        print(f"[ERRO] Problema com cliente {endereco}: {e}")
    finally:
        conexao.close()
        print(f"[LOG] Conexão encerrada com {endereco}")

def main():
    host = '0.0.0.0'
    port = 7000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)

    print(f"[INÍCIO] Servidor de hora ouvindo na porta {port}")

    while True:
        try:
            conexao, endereco = servidor.accept()
            thread = threading.Thread(target=atender_cliente, args=(conexao, endereco))
            thread.start()
        except KeyboardInterrupt:
            print("\n[ENCERRADO] Servidor encerrado manualmente.")
            break

if __name__ == "__main__":
    main()
