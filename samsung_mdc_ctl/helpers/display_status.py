from enum import Enum


class LampError(Enum):
    NORMAL = 0x00
    ERROR = 0x01


class TemperatureError(Enum):
    NORMAL = 0x00
    ERROR = 0x01


class BrightSensorError(Enum):
    NONE = 0x00
    ERROR = 0x01
    NORMAL = 0x02


class NoSyncError(Enum):
    NORMAL = 0x00
    NO_SYNC = 0x01
    INVALID = 0x02


class FanError(Enum):
    NORMAL = 0x00
    ERROR = 0x01
    NOT_SUPPORTED = 0x02


class DisplayStatus:
    """Display status response object"""

    def __init__(self, payload: bytes) -> None:
        self.lampError = LampError(payload[0])
        self.tempError = TemperatureError(payload[1])
        self.brightSensorError = BrightSensorError(payload[2])
        self.noSyncError = NoSyncError(payload[3])
        self.temperature = int(payload[4])
        self.fanError = FanError(payload[5])
        pass
