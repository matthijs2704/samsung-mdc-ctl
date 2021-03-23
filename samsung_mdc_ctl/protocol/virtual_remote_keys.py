from enum import Enum


class VirtualRemoteKey(Enum):
    """Keys to be used with the virtual remote"""

    KEY_SOURCE = 0x01
    KEY_POWER = 0x02
    KEY_1 = 0x04
    KEY_2 = 0x05
    KEY_3 = 0x06
    KEY_VOLUME_UP = 0x07
    KEY_4 = 0x08
    KEY_5 = 0x09
    KEY_6 = 0x0A
    KEY_VOLUME_DOWN = 0x0B
    KEY_7 = 0x0C
    KEY_8 = 0x0D
    KEY_9 = 0x0E
    KEY_MUTE = 0x0F
    KEY_CHANNEL_DOWN = 0x10
    KEY_0 = 0x11
    KEY_CHANNEL_UP = 0x12
    KEY_GREEN = 0x14
    KEY_YELLOW = 0x15
    KEY_CYAN = 0x16
    KEY_MENU = 0x1A
    KEY_DISPLAY = 0x1F
    KEY_INFO = 0x1F
    KEY_DIGIT = 0x23
    KEY_PIP_TV_VIDEO = 0x24
    KEY_BLANK = 0x24
    KEY_EXIT = 0x2D
    KEY_MAGICINFO = 0x30
    KEY_REW = 0x45
    KEY_STOP = 0x46
    KEY_PLAY = 0x47
    KEY_FF = 0x48
    KEY_PAUSE = 0x4A
    KEY_TOOLS = 0x4B
    KEY_RETURN = 0x58
    KEY_MAGICINFO_LITE = 0x5B
    KEY_CURSOR_UP = 0x60
    KEY_CURSOR_DOWN = 0x61
    KEY_CURSOR_RIGHT = 0x62
    KEY_CURSOR_LEFT = 0x65
    KEY_ENTER = 0x68
    KEY_RED = 0x6C
    KEY_LOCK = 0x77
    KEY_CONTENT = 0x79
    KEY_POWER_OFF = 0x98
    KEY_3D = 0x9F
