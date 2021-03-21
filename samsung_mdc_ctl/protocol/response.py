from samsung_mdc_ctl.protocol.commands import Command


class Response:
    def __init__(self, rCmd: Command):
        self.rCmd = rCmd


class AckResponse(Response):
    def __init__(self, rCmd: Command, payload: bytes):
        super().__init__(rCmd)
        self.payload = payload


class NakResponse(Response):
    def __init__(self, rCmd: Command, errCode: int):
        super().__init__(rCmd)
        self.errCode = errCode
