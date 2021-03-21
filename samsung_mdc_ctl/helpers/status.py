from samsung_mdc_ctl.protocol.sources import InputSource


class DisplayStatus:
    """ Representation of the display status message """

    def __init__(self, payload: bytes) -> None:
        self.power = payload[0] == 1
        self.volume = payload[1]
        self.mute = payload[2] == 1
        self.input = InputSource(payload[3])
        self.aspect = payload[4]
        pass
