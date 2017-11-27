import socket,sys

class Transmissor:
    def __init__(self):
        self.port = 4321
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.sock.connect(('localhost',self.port))
        print('[Transmissor] Connecting transmissor')

    def send(self,text):
        package = str(text)
        self.sock.send(package)
        print('[Transmissor] Text sent: ', package)