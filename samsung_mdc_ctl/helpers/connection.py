import logging
import socket
import time

from samsung_mdc_ctl import utils
from samsung_mdc_ctl.protocol.commands import Command

from . import exceptions
from .response import AckResponse, NakResponse


class MDCConnection:
    """Object for the connection to the screen"""

    def __init__(self, config) -> None:
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if config["timeout"]:
            self.connection.settimeout(config["timeout"])

        self.connection.connect((config["host"], 1515))
        self.deviceId = config["deviceId"] & 0xFF

        # self._read_response(True)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        """Close the connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
            logging.debug("Connection closed.")

    def send(self, cmd: Command, data=[]):
        """Send a control command."""
        if not self.connection:
            raise exceptions.ConnectionClosed()

        print(f"command: {cmd}")

        payload = bytearray()
        payload.append(cmd.value)
        payload.append(self.deviceId)
        payload += self._serialize_data(data)
        print(utils.byte_compute_checksum(payload))

        packet = bytearray([0xAA])
        packet += payload
        packet.append(utils.compute_checksum(payload))
        print(packet)

        logging.info("Sending control command: %s", cmd)
        self.connection.send(packet)
        return self._read_response()

    def _read_response(self, first_time=False):
        read_data = self.connection.recv(1024)

        if len(read_data) <= 2:
            raise exceptions.NotEnoughData()

        if (
            read_data[0] != 0xAA
            or Command(read_data[1]) is not Command.ACK_NACK
        ):
            raise exceptions.InvalidResponse()

        checksum = read_data[-1]
        computed_checksum = utils.compute_checksum(read_data[1:-2])
        if checksum != computed_checksum:
            raise exceptions.InvalidResponseChecksum()

        if read_data[2] != self.deviceId:
            print("Received an response not for my device")
            raise exceptions.InvalidResponseDeviceId()

        dataLength = read_data[3]
        payload = read_data[4:-1]
        if len(payload) != dataLength:
            raise exceptions.NotEnoughData()

        rCmd = payload[1]

        if payload[0] == ord("A"):
            return AckResponse(rCmd, payload[2:])
        elif payload[0] == ord("N"):
            return NakResponse(rCmd, payload[2])
        else:
            raise exceptions.UnhandledResponse()

    @staticmethod
    def _serialize_data(data):
        serialized_data = bytearray()
        serialized_data.append(len(data))
        serialized_data += bytearray(data)
        return serialized_data
