from os import close
import socket
import threading


SERVERADDRESS = ("0.0.0.0", 9000)


def receive_message(connection, client_address):
    while True:
        message = connection.recv(1024)
        print("from: ", client_address, "message: ", message)
        connection.send(message)
        
        if message == b'terminate':
            connection.close()
            break


def main():

    s = socket.socket()

    s.bind(SERVERADDRESS)

    s.listen(5)

    while True:
        print("Waiting for a connection ...")

        connection, client_addr = s.accept()

        print("connection received from: ", client_addr)

        th = thread = threading.Thread(target=receive_message, args=[connection, client_addr])
        th.start()


if __name__ == "__main__":
    main()

