import socket
import threading

def handle_client(conn, addr):
    print(f"Kapcsolódott: {addr}")
    try:
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                recieved = data.decode()
                print(f"Kapott üzenet: {recieved}")
                response = "-".join(l for l in recieved)
                print(f"Válasz: {response}")
                conn.sendall(response.encode())
    except Exception as e:
        print(f"Hiba a klienssel ({addr}): {e}")
    finally:
        print(f"Kapcsolat lezárva: {addr}")

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    print("A szerver fut a 65432-es porton...")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\nA szerver leállt kézi megszakítás miatt.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_server()
