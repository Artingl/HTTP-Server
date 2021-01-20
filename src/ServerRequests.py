from src.ServerInfo import ServerInfo


class ServerRequests:
    def __init__(self, httpClass):
        self.http = httpClass
        self.requests = {}

    def add(self, req, callback):
        """Will add new listener witch will listen to the new request"""
        self.requests[req] = callback
