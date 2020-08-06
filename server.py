#!/home/viera/anaconda3/bin/python3.7
import socket
from argparse import ArgumentParser
import os
import threading
import sys

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class Server():

    def __init__(self):
        self.parse = ArgumentParser(description=' Share text.')
        self.parse.add_argument('-p',
                                '--port',
                                type=int,
                                default=12313,
                                help='Specify port')
        self.option, self.content = self.parse.parse_known_args()

    def start_server(self):
        global s, c, addr
        s = socket.socket()
        port = self.option.port
        s.bind(('', port))
        s.listen(5)
        print('Waiting for connection:\n')
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            print('')
            exit()
            return
        os.system('clear')
        print('Connection from:', addr)

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.listen)
        try:
            thread.start()
        except KeyboardInterrupt:
            sys.exit()

    def listen(self):
        while True:
            try:
                rcvdData = c.recv(1024).decode()
                if not len(rcvdData):
                    print('Closed connection from cell')
                    sys.exit()
                    break
            except KeyboardInterrupt:
                print('')
                break
            except:
                break
            print(rcvdData)
        c.close()
        s.close()
        sys.exit()

    def sendData(self):
        while True:
            try:
                sendData = input()
                if sendData.lower() == 'q' or sendData.lower() == 'quit':
                    os._exit(0)
                    break
            except KeyboardInterrupt:
                print('')
                break
            c.send(sendData.encode())
        c.close()
        s.close()
        sys.exit()

if __name__ == "__main__":
    os.system('clear')
    server = Server()
    server.start_server()
    try:
        server.listen_for_incoming_messages_in_a_thread()
    except KeyboardInterrupt:
        sys.exit()
    try:
        server.sendData()
    except:
        pass
