def getNameByCode(code):
    if code == 200:
        return "OK"
    if code == 404:
        return "Not found"


class ResponseCodes:
    SUCCESS = 200
    NOT_FOUND = 404
