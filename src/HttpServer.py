from src.ServerRequests import ServerRequests
from src.Socket import Socket


class HttpServer:
    def __init__(self, ip, port, folder=''):
        self.indexFile = 'index.html'

        self.ip = ip
        self.port = port
        self.folder = folder

        self.socket = Socket()
        self.requests = ServerRequests()

    def runServer(self):
        pass
