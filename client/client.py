import socket


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    while True:
        message = input("Enter a message: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(f"Server response: {response}")
    client.close()


if __name__ == "__main__":
    start_client()
