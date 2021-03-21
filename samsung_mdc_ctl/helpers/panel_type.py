from enum import Enum


class PanelType(Enum):
    PDP = 0x01
    LCD = 0x02
    DLP = 0x03
    LED = 0x04
    CRT = 0x05
    OLED = 0x06
