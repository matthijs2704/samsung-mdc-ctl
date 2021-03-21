from enum import Enum


class InputSource(Enum):
    """ Input Sources """

    S_VIDEO = 0x04
    COMPONENT = 0x08
    AV = 0x0C
    AV_2 = 0x0D
    SCART = 0x0E
    DVI = 0x18
    PC = 0x14
    BNC = 0x1E
    DVI_VIDEO = 0x1F
    MAGICINFO = 0x20
    HDMI_1 = 0x21
    HDMI_1_PC = 0x22  # get only!
    HDMI_2 = 0x23
    HDMI_2_PC = 0x24  # get only!
    DP = 0x25
    DP_2 = 0x26
    DP_3 = 0x27
    HDMI_3 = 0x31
    HDMI_3_PC = 0x32  # get only!
    HDMI_4 = 0x33
    HDMI_4_PC = 0x34  # get only!
    TV = 0x40
    MODULE = 0x50
    HDBT = 0x55
    OCM = 0x56
    MEDIA = 0x60
    SCREEN_MIRRORING = 0x61
    INTERNAL_USB = 0x62
    URL_LAUNCHER = 0x63
    IWB = 0x64
    WEB_BROWSER = 0x65
    REMOTE_WORKSPACE = 0x65

    ALL_SOURCES = [
        S_VIDEO,
        COMPONENT,
        AV,
        AV_2,
        SCART,
        DVI,
        PC,
        BNC,
        DVI_VIDEO,
        MAGICINFO,
        HDMI_1,
        HDMI_1_PC,
        HDMI_2,
        HDMI_2_PC,
        DP,
        DP_2,
        DP_3,
        HDMI_3,
        HDMI_3_PC,
        HDMI_4,
        HDMI_4_PC,
        TV,
        MODULE,
        HDBT,
        OCM,
        MEDIA,
        SCREEN_MIRRORING,
        INTERNAL_USB,
        URL_LAUNCHER,
        IWB,
        WEB_BROWSER,
        REMOTE_WORKSPACE,
    ]

    ALL_SOURCE_NAMES = {
        S_VIDEO: "S-Video",
        COMPONENT: "Component",
        AV: "AV1 (AV)",
        AV_2: "AV2",
        SCART: "Ext. (SCART1)",
        DVI: "DVI",
        PC: "PC",
        BNC: "BNC",
        DVI_VIDEO: "DVI VIDEO",
        MAGICINFO: "MagicInfo",
        HDMI_1: "HDMI 1",
        HDMI_1_PC: "HDMI 1 (PC)",
        HDMI_2: "HDMI 2",
        HDMI_2_PC: "HDMI 2 (PC)",
        DP: "DisplayPort",
        DP_2: "DisplayPort 2",
        DP_3: "DisplayPort 3",
        HDMI_3: "HDMI 3",
        HDMI_3_PC: "HDMI 3 (PC)",
        HDMI_4: "HDMI 4",
        HDMI_4_PC: "HDMI 4 (PC)",
        TV: "TV (DTV)",
        MODULE: "Plug In Module",
        HDBT: "HDBaseT",
        OCM: "OCM",
        MEDIA: "Meida/MagicInfo S",
        SCREEN_MIRRORING: "WiDi/Screen Mirroring",
        INTERNAL_USB: "Internal/USB",
        URL_LAUNCHER: "URL launcher",
        IWB: "IWB",
        WEB_BROWSER: "Web Browser",
        REMOTE_WORKSPACE: "Remote Workspace",
    }
