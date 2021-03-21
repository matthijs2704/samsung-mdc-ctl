from samsung_mdc_ctl.helpers.connection import MDCConnection
from samsung_mdc_ctl.helpers.display_status import DisplayStatus
from samsung_mdc_ctl.helpers.exceptions import NakReceived, UnhandledResponse
from samsung_mdc_ctl.helpers.model import DisplayModel
from samsung_mdc_ctl.helpers.status import Status
from samsung_mdc_ctl.power import DisplayPower
from samsung_mdc_ctl.protocol.commands import Command
from samsung_mdc_ctl.protocol.response import AckResponse, NakResponse, Response
from samsung_mdc_ctl.protocol.sources import InputSource


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
            return Status(statusResponse.payload)
        raise UnhandledResponse()

    def getSerialNumber(self) -> str:
        response = self.connection.send(Command.GET_SERIAL)
        serialResponse = self._check_response(response)

        if serialResponse.rCmd == Command.GET_SERIAL:
            return str(serialResponse.payload.decode("utf-8"))
        raise UnhandledResponse()

    def getDisplayStatusControl(self) -> DisplayStatus:
        response = self.connection.send(Command.GET_DISPLAY_STATUS)
        dispStatusResponse = self._check_response(response)

        if dispStatusResponse.rCmd == Command.GET_DISPLAY_STATUS:
            return DisplayStatus(dispStatusResponse.payload)
        raise UnhandledResponse()

    def getSWVersion(self) -> str:
        response = self.connection.send(Command.GET_SW_VER)
        swVerResponse = self._check_response(response)

        if swVerResponse.rCmd == Command.GET_SW_VER:
            return str(swVerResponse.payload.decode("utf-8"))
        raise UnhandledResponse()

    def getModelNumber(self) -> DisplayModel:
        response = self.connection.send(Command.GET_MODEL)
        modelResponse = self._check_response(response)

        if modelResponse.rCmd == Command.GET_MODEL:
            return DisplayModel(modelResponse.payload)
        raise UnhandledResponse()

    ############## 2.1.11 Power Control ##############

    def getPower(self) -> DisplayPower:
        response = self.connection.send(Command.POWER)
        pwrResponse = self._check_response(response)

        if pwrResponse.rCmd == Command.POWER:
            return DisplayPower(pwrResponse.payload[0])
        raise UnhandledResponse()

    # todo: on power on, wait 10 sec, then reconnect
    def setPower(self, power: DisplayPower) -> None:
        pwrResponse = self.connection.send(Command.POWER, [power.value])
        self._check_response(pwrResponse)

    ############## 2.1.12 Volume Control ##############

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

    ############## 2.1.13 Mute Control ##############

    def getMute(self) -> bool:
        response = self.connection.send(Command.MUTE)
        muteResponse = self._check_response(response)

        if muteResponse.rCmd == Command.MUTE:
            return bool(muteResponse.payload[0] == 1)
        raise UnhandledResponse()

    def setMute(self, mute: bool) -> None:
        muteResponse = self.connection.send(Command.MUTE, [mute])
        self._check_response(muteResponse)

    ############## 2.1.14 Input Source Control ##############

    def getInputSource(self) -> InputSource:
        response = self.connection.send(Command.INPUT_SOURCE)
        inputSourceResponse = self._check_response(response)

        if inputSourceResponse.rCmd == Command.INPUT_SOURCE:
            return InputSource(inputSourceResponse.payload[0])
        raise UnhandledResponse()

    def setInputSource(self, src: InputSource) -> None:
        changeInputSourceResponse = self.connection.send(
            Command.INPUT_SOURCE, [src.value]
        )
        self._check_response(changeInputSourceResponse)
