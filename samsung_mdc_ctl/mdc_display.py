from samsung_mdc_ctl.helpers.connection import MDCConnection
from samsung_mdc_ctl.helpers.exceptions import NakReceived, UnhandledResponse
from samsung_mdc_ctl.helpers.status import DisplayStatus
from samsung_mdc_ctl.protocol.commands import Command
from samsung_mdc_ctl.protocol.response import AckResponse, NakResponse, Response


class MDCDisplay:
    """Object representing the MDC controlled display"""

    def __init__(self, host: str, deviceId: int) -> None:
        self._host = host
        self._deviceId = deviceId
        self.connection = MDCConnection(host=host, deviceId=deviceId)

    def _check_response(self, response: Response) -> AckResponse:
        if isinstance(response, AckResponse):
            return response
        elif isinstance(response, NakResponse):
            raise NakReceived(response.errCode)

    def getStatus(self) -> DisplayStatus:
        response = self.connection.send(Command.STATUS)
        statusResponse = self._check_response(response)

        if statusResponse.rCmd == Command.STATUS:
            return DisplayStatus(statusResponse.payload)
        raise UnhandledResponse()

    def getPower(self) -> bool:
        response = self.connection.send(Command.POWER)
        pwrResponse = self._check_response(response)

        if pwrResponse.rCmd == Command.POWER:
            if pwrResponse.payload[0] == 1:
                return True
            return False
        raise UnhandledResponse()

    def setPower(self, power: bool) -> None:
        pwrResponse = self.connection.send(Command.POWER, [power])
        self._check_response(pwrResponse)

    def getMute(self) -> bool:
        response = self.connection.send(Command.MUTE)
        muteResponse = self._check_response(response)

        if muteResponse.rCmd == Command.MUTE:
            return bool(muteResponse.payload[0] == 1)
        raise UnhandledResponse()

    def setMute(self, mute: bool) -> None:
        muteResponse = self.connection.send(Command.MUTE, [mute])
        self._check_response(muteResponse)

    def getVolume(self) -> int:
        response = self.connection.send(Command.VOLUME)
        volResponse = self._check_response(response)

        if volResponse.rCmd == Command.VOLUME:
            return int(volResponse.payload[0])
        raise UnhandledResponse()

    def setVolume(self, volume: int) -> None:
        volume = max(0, min(volume, 100))
        volResponse = self.connection.send(Command.VOLUME, [volume])
        self._check_response(volResponse)

    def getSWVersion(self) -> str:
        response = self.connection.send(Command.GET_SW_VER)
        swVerResponse = self._check_response(response)

        if swVerResponse.rCmd == Command.GET_SW_VER:
            return str(swVerResponse.payload.decode("utf-8"))
        raise UnhandledResponse()
