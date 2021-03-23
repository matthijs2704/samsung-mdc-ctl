from samsung_mdc_ctl.protocol.power import DisplayPower
from samsung_mdc_ctl.protocol.sources import InputSource


class Status:
    """ Representation of the status message """

    def __init__(self, payload: bytes) -> None:
        self.power = DisplayPower(payload[0])
        self.volume = payload[1]
        self.mute = payload[2] == 1
        self.input = InputSource(payload[3])
        self.aspect = payload[4]
        pass
