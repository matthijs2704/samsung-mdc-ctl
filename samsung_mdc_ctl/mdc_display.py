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

    def _check_response(self, response) -> None:
        if isinstance(response, AckResponse):
            pass
        elif isinstance(response, NakResponse):
            raise NakReceived(response.errCode)

    def getStatus(self) -> None:
        statusResponse = self.connection.send(Command.STATUS)
        self._check_response(statusResponse)

        if statusResponse.rCmd == Command.STATUS.value:
            return DisplayStatus(statusResponse.payload)
        raise UnhandledResponse()

    def getMute(self) -> bool:
        muteResponse = self.connection.send(Command.MUTE)
        self._check_response(muteResponse)

        if muteResponse.rCmd == Command.MUTE.value:
            return muteResponse.payload[0] == 1
        raise UnhandledResponse()

    def setMute(self, mute: bool) -> None:
        muteResponse = self.connection.send(Command.MUTE, [mute])
        self._check_response(muteResponse)

        if muteResponse.rCmd == Command.MUTE.value:
            return muteResponse.payload[0] == 1
        raise UnhandledResponse()
