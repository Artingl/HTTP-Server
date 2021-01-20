class ServerInfo:
    def __init__(self, httpClass):
        self.http = httpClass
        self.request = {}

    def getServerIp(self):
        """Will return the ip to witch the socket is bound"""
        return self.http.ip

    def getServerPort(self):
        """Will return the port to witch the socket is bound"""
        return self.http.port

    def getSiteDir(self):
        """Will return the current site folder"""
        return self.http.folder
