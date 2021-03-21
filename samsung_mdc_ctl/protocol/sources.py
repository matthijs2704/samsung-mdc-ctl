from enum import Enum


class InputSource(Enum):
    """ Input Sources """

    INPUT_S_VIDEO = 0x04
    INPUT_COMPONENT = 0x08
    INPUT_AV = 0x0C
    INPUT_AV_2 = 0x0D
    INPUT_SCART = 0x0E
    INPUT_DVI = 0x18
    INPUT_PC = 0x14
    INPUT_BNC = 0x1E
    INPUT_DVI_VIDEO = 0x1F
    INPUT_MAGICINFO = 0x20
    INPUT_HDMI_1 = 0x21
    INPUT_HDMI_1_PC = 0x22  # get only!
    INPUT_HDMI_2 = 0x23
    INPUT_HDMI_2_PC = 0x24  # get only!
    INPUT_DP = 0x25
    INPUT_DP_2 = 0x26
    INPUT_DP_3 = 0x27
    INPUT_HDMI_3 = 0x31
    INPUT_HDMI_3_PC = 0x32  # get only!
    INPUT_HDMI_4 = 0x33
    INPUT_HDMI_4_PC = 0x34  # get only!
    INPUT_TV = 0x40
    INPUT_MODULE = 0x50
    INPUT_HDBT = 0x55
    INPUT_OCM = 0x56
    INPUT_MEDIA = 0x60
    INPUT_SCREEN_MIRRORING = 0x61
    INPUT_INTERNAL_USB = 0x62
    INPUT_URL_LAUNCHER = 0x63
    INPUT_IWB = 0x64
    INPUT_WEB_BROWSER = 0x65
    INPUT_REMOTE_WORKSPACE = 0x65

    ALL_SOURCES = [
        INPUT_S_VIDEO,
        INPUT_COMPONENT,
        INPUT_AV,
        INPUT_AV_2,
        INPUT_SCART,
        INPUT_DVI,
        INPUT_PC,
        INPUT_BNC,
        INPUT_DVI_VIDEO,
        INPUT_MAGICINFO,
        INPUT_HDMI_1,
        INPUT_HDMI_1_PC,
        INPUT_HDMI_2,
        INPUT_HDMI_2_PC,
        INPUT_DP,
        INPUT_DP_2,
        INPUT_DP_3,
        INPUT_HDMI_3,
        INPUT_HDMI_3_PC,
        INPUT_HDMI_4,
        INPUT_HDMI_4_PC,
        INPUT_TV,
        INPUT_MODULE,
        INPUT_HDBT,
        INPUT_OCM,
        INPUT_MEDIA,
        INPUT_SCREEN_MIRRORING,
        INPUT_INTERNAL_USB,
        INPUT_URL_LAUNCHER,
        INPUT_IWB,
        INPUT_WEB_BROWSER,
        INPUT_REMOTE_WORKSPACE,
    ]

    ALL_SOURCE_NAMES = {
        INPUT_S_VIDEO: "S-Video",
        INPUT_COMPONENT: "Component",
        INPUT_AV: "AV1 (AV)",
        INPUT_AV_2: "AV2",
        INPUT_SCART: "Ext. (SCART1)",
        INPUT_DVI: "DVI",
        INPUT_PC: "PC",
        INPUT_BNC: "BNC",
        INPUT_DVI_VIDEO: "DVI VIDEO",
        INPUT_MAGICINFO: "MagicInfo",
        INPUT_HDMI_1: "HDMI 1",
        INPUT_HDMI_1_PC: "HDMI 1 (PC)",
        INPUT_HDMI_2: "HDMI 2",
        INPUT_HDMI_2_PC: "HDMI 2 (PC)",
        INPUT_DP: "DisplayPort",
        INPUT_DP_2: "DisplayPort 2",
        INPUT_DP_3: "DisplayPort 3",
        INPUT_HDMI_3: "HDMI 3",
        INPUT_HDMI_3_PC: "HDMI 3 (PC)",
        INPUT_HDMI_4: "HDMI 4",
        INPUT_HDMI_4_PC: "HDMI 4 (PC)",
        INPUT_TV: "TV (DTV)",
        INPUT_MODULE: "Plug In Module",
        INPUT_HDBT: "HDBaseT",
        INPUT_OCM: "OCM",
        INPUT_MEDIA: "Meida/MagicInfo S",
        INPUT_SCREEN_MIRRORING: "WiDi/Screen Mirroring",
        INPUT_INTERNAL_USB: "Internal/USB",
        INPUT_URL_LAUNCHER: "URL launcher",
        INPUT_IWB: "IWB",
        INPUT_WEB_BROWSER: "Web Browser",
        INPUT_REMOTE_WORKSPACE: "Remote Workspace",
    }
