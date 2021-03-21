class Response:
    def __init__(self, rCmd):
        self.rCmd = rCmd


class AckResponse(Response):
    def __init__(self, rCmd, payload):
        super().__init__(rCmd)
        self.payload = payload


class NakResponse(Response):
    def __init__(self, rCmd, errCode):
        super().__init__(rCmd)
        self.errCode = errCode
