# type: ignore[attr-defined]

from typing import Optional

import logging
import random
import time
from enum import Enum

import typer
from rich.console import Console
from samsung_mdc_ctl import __version__
from samsung_mdc_ctl.example import hello
from samsung_mdc_ctl.helpers.connection import MDCConnection
from samsung_mdc_ctl.helpers.exceptions import NakReceived
from samsung_mdc_ctl.mdc_display import MDCDisplay
from samsung_mdc_ctl.protocol.commands import Command
from samsung_mdc_ctl.protocol.power import DisplayPower
from samsung_mdc_ctl.protocol.sources import InputSource


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="samsung-mdc-ctl",
    help="Awesome `samsung-mdc-ctl` is a Python cli/package created with https://github.com/TezRomacH/python-package-template",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]samsung-mdc-ctl[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for name. If not specified then choice will be random.",
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the samsung-mdc-ctl package.",
    ),
):
    """Prints a greeting for a giving name."""
    # logger.setLevel()
    greeting: str = hello(name)

    logging.basicConfig(encoding="utf-8", level=logging.DEBUG)

    display = MDCDisplay(host="192.168.3.153", deviceId=1)
    # print(display.getModelNumber().__dict__)
    # print(display.getSWVersion())
    print(display.getStatus().__dict__)
    # print(display.getPower())
    # print(display.getMute())
    # print(display.getVolume())
    # display.setMute(False)
    # display.setPower(DisplayPower.POWER_ON)
    # display.setVolume(10)
    try:
        print(display.getPower())
        print(display.setPower(DisplayPower.POWER_OFF))
        time.sleep(2)
        print(display.getPower())
        # time.sleep(10)
        print(display.setPower(DisplayPower.POWER_ON))
        print(display.getPower())
        # resp = display.connection.send(cmd=Command.PIP_STATUS, data=[])
        # print(f"Resp: %s" % resp)
        # print(f"Resp Data: %s" % resp.__dict__)
    except NakReceived as e:
        print(f"NAK: %s" % e.args)

    # try:
    #     print(display.getInputSource())
    #     print(display.setInputSource(InputSource.HDMI_1))
    # except NakReceived as e:
    #     print(e.args)

    # print(display.connection.send(Command.OUTDOOR_MODE, [0x81]).__dict__)
    # console.print(f"[bold magenta]Got connection to the Samsung display![/]")
    # print(connection.send(Command.STATUS))
    # print(connection.send(Command.MUTE, [0x0]))
    # connection.close()
