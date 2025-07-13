import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  # Szerver IP és port
    server_socket.listen(1)
    print("A szerver fut...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Kapcsolódott: {addr}")

        while True:
            data = conn.recv(1024)  # Üzenet fogadása
            if not data:
                break  # Kapcsolat bezárása, ha nem érkezik több adat
            recieved = data.decode()
            print(f"Kapott üzenet: {recieved}")  # Üzenet kiírása
            response = "-".join(l for l in recieved)   # Válasz
            print(f"Válasz: {response}")
            conn.sendall(response.encode())  # Válasz küldése
        conn.close()

if __name__ == '__main__':
    run_server()

