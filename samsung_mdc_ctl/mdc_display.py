from samsung_mdc_ctl.helpers.connection import MDCConnection
from samsung_mdc_ctl.helpers.exceptions import NakReceived, UnhandledResponse
from samsung_mdc_ctl.helpers.status import DisplayStatus
from samsung_mdc_ctl.protocol.commands import Command
from samsung_mdc_ctl.protocol.response import AckResponse, NakResponse


class MDCDisplay:
    """Object representing the MDC controlled display"""

    def __init__(self, host: str, deviceId: int) -> None:
        self._host = host
        self._deviceId = deviceId
        self.connection = MDCConnection(host=host, deviceId=deviceId)

    def getStatus(self) -> None:
        statusResponse = self.connection.send(Command.STATUS)
        if isinstance(statusResponse, AckResponse):
            if statusResponse.rCmd == Command.STATUS.value:
                status = DisplayStatus(statusResponse.payload)
                return status
            raise UnhandledResponse()
        elif isinstance(statusResponse, NakResponse):
            raise NakReceived(statusResponse.errCode)

    def getMute(self) -> bool:
        muteResponse = self.connection.send(Command.MUTE)
        if isinstance(muteResponse, AckResponse):
            if muteResponse.rCmd == Command.MUTE.value:
                return muteResponse.payload[0] == 1
            raise UnhandledResponse()
        elif isinstance(muteResponse, NakResponse):
            raise NakReceived(muteResponse.errCode)

    def setMute(self, mute: bool) -> None:
        muteResponse = self.connection.send(Command.MUTE, [mute])
        if isinstance(muteResponse, AckResponse):
            if muteResponse.rCmd == Command.MUTE.value:
                return muteResponse.payload[0] == 1
            raise UnhandledResponse()
        elif isinstance(muteResponse, NakResponse):
            raise NakReceived(muteResponse.errCode)
