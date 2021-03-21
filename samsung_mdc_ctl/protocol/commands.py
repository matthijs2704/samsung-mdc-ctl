from enum import Enum


class Command(Enum):
    STATUS = 0x00
    GET_SERIAL = 0x0B
    GET_FW_VER = 0x0E
    GET_MODEL = 0x10
    POWER = 0x11
    VOLUME = 0x12
    MUTE = 0x13
    INPUT_SOURCE = 0x14
    CHANNEL_CONTROL = 0x17

    ACK_NACK = 0xFF
