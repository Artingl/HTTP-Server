from src.HttpServer import HttpServer


def testRequest(info):
    return f"Browser user agent is {info.request['user-agent']}"


server = HttpServer("0.0.0.0", 8364)
server.runServer()

server.folder = 'site'
server.requests.add("/test", testRequest)
