import socket
import time
import random


SERVERADDRESS = ("192.168.10.2", 9000)


def main():

    s = socket.socket()
    print("connect to server: ", SERVERADDRESS)

    s.connect(SERVERADDRESS)

    rand = random.randrange(5, 15)

    message = b"Hello from the other side!"

    while True:
        time.sleep(1)

        s.sendall(message)
        print("message sent!")

        echo = s.recv(1024)
        print(echo)

        rand -= 1
        if rand == 0:
            message = b'terminate'

        if echo == b'terminate':
            s.close()
            break


if __name__ == "__main__":
    main()

