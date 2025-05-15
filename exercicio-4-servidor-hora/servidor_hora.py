import socket
import threading
import datetime

# Função que trata cada cliente conectado
def atender_cliente(conexao, endereco):
    try:
        print(f"[LOG] Conexão recebida de {endereco}")
        while True:
            # Recebe a requisição do cliente
            requisicao = conexao.recv(1024).decode()
            if not requisicao:
                break

            # Obtém a hora atual no formato HH:MM:SS
            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
            # Envia a hora de volta ao cliente
            conexao.send(hora_atual.encode())

            # Registra a solicitação no log
            print(f"[LOG] Hora enviada para {endereco}: {hora_atual}")
    except Exception as e:
        print(f"[ERRO] Problema com cliente {endereco}: {e}")
    finally:
        # Fecha a conexão com o cliente
        conexao.close()
        print(f"[LOG] Conexão encerrada com {endereco}")

def main():
    host = '0.0.0.0'  	# Aceita de qualquer endereço
    port = 7000		# Porta do Servidor

    # Criação do socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)

    print(f"[INÍCIO] Servidor de hora ouvindo na porta {port}")

    # Loop principal do servidor
    while True:
        try:
            # Aceita novas conexões
            conexao, endereco = servidor.accept()

            # Cria uma thread para atender o novo cliente
            thread = threading.Thread(target=atender_cliente, args=(conexao, endereco))
            thread.start()
        except KeyboardInterrupt:
            print("\n[ENCERRADO] Servidor encerrado manualmente.")
            break

if __name__ == "__main__":
    main()
