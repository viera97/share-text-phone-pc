import socket
from argparse import ArgumentParser
import threading
import sys

class Client():

    def __init__(self):
        self.parse = ArgumentParser(description=' Share text.')
        self.parse.add_argument('-i',
                                '--ip',
                                type=str,
                                default="127.0.0.1",
                                help='Specify Ip server')
        self.parse.add_argument('-p',
                                '--port',
                                type=int,
                                default=12313,
                                help='Specify Port server')
        self.option, self.content = self.parse.parse_known_args()

    def start_client(self):
        global s
        s = socket.socket()
        s.connect((self.option.ip, self.option.port))
        s.send(''.encode());

    def listen_for_incoming_messages_in_a_thread(self):
            thread = threading.Thread(target=self.listen)
            try:
                thread.start()
            except KeyboardInterrupt:
                sys.exit()

    def sendData(self):
        while True:
            try:
                str = input()
            except KeyboardInterrupt:
                break
            s.send(str.encode());
            if str.lower() == 'quit' or str.lower() == 'q':
                break
        s.close()
        sys.exit()

    def listen(self):
        while True:
            try:
                recved = s.recv(1024).decode()
                if not len(recved):
                    print('Connection from server closed')
                    sys.exit()
                    break
            except KeyboardInterrupt:
                break
            except:
                break
            print(recved)
        s.close()
        sys.exit()

if __name__ == "__main__":
    client = Client()
    client.start_client()
    client.listen_for_incoming_messages_in_a_thread()
    try:
        client.sendData()
    except:
        pass
