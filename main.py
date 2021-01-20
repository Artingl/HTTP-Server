from src.HttpServer import HttpServer


def getRequest(info):
    return f"Hello, World! ({info.getServerIp()}:{info.getServerPort()})"


server = HttpServer("0.0.0.0", 8364)  # Binding server on 0.0.0.0:8364
server.runServer()  # Run the server

server.requests.add("/test", getRequest)  # When we get request /test the function getRequest will be called
