import socket
import struct
import threading
from src.ResponseCodes import ResponseCodes, getNameByCode
from src.ServerInfo import ServerInfo
from src.ServerRequests import ServerRequests


class HttpServer:
    def __init__(self, ip, port, folder=''):
        self.indexFile = 'index.html'

        self.maxConnectionsInOneTime = 10
        self.ip = ip
        self.port = port
        self.folder = folder
        self.serverIsRunning = False
        self.serverName = "Python server 1.0.20.21"

        self.connectionsThread = threading.Thread(target=self.listenForConnections)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.requests = ServerRequests(self)

    def genResponse(self, usr, req, text, type):
        result = f"{req['httpVersion']} {type} {getNameByCode(type)}\n" \
                 f"Date: Mon, 27 Jul 2009 12:28:53 GMT\n" \
                 f"Server: {self.serverName}\n" \
                 f"Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\n" \
                 f"Content length: {(len(text))}\n" \
                 f"Connection: Closed\n" \
                 f"Content-Type: text/html;\n\n" \
                 f"{text}\n"
        usr.sendall(bytes(result, encoding="UTF-8"))

    def executeRequest(self, req, usr):
        req = self.decodeHttpRequest(req)
        obj = ServerInfo(self)
        obj.request = req["info"]

        if self.folder:
            pass
        else:
            if req["filePath"] in self.requests.requests:
                self.genResponse(usr, req, self.requests.requests[req['filePath']](obj), ResponseCodes.SUCCESS)
            else:
                self.genResponse(usr, req, f"{req['filePath']} not found!", ResponseCodes.NOT_FOUND)  # 404

    def runServer(self):
        """Will run the server"""
        self.socket.bind((self.ip, self.port))
        self.socket.listen(self.maxConnectionsInOneTime)

        self.serverIsRunning = True
        self.connectionsThread.start()

    def listenForConnections(self):
        while self.serverIsRunning:
            try:
                usr, address = self.socket.accept()
                msg = ''

                while True:
                    data = usr.recv(1024)
                    data = ''.join([chr(i) for i in bytes(data)])

                    msg += data
                    if data.endswith("\r\n\r\n"):
                        break

                self.executeRequest(msg, usr)

            except Exception as e:
                print(f"Unexpected error with one connection ({e})")

    def decodeHttpRequest(self, req):
        res = {}

        for i in req.split("\n"):
            if i.startswith("GET"):
                res["httpVersion"] = "HTTP" + i.split("HTTP")[1].strip()
                res["filePath"] = i.split("HTTP")[0].split("GET")[1].strip()
            else:
                if "info" not in res:
                    res["info"] = {}
                if i.strip():
                    res["info"][i.split(":")[0].strip().lower()] = i.split(":")[1].strip()

        return res
