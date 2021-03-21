from samsung_mdc_ctl.helpers.panel_type import PanelType


class DisplayModel:
    def __init__(self, payload: bytes) -> None:

        self.panelType = PanelType(payload[0])
        self.model = payload[1]
        self.support_tv = bool(payload[2] == 0)
