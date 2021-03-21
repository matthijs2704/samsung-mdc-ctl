class AccessDenied(Exception):
    """Connection was denied."""

    pass


class ConnectionClosed(Exception):
    """Connection was closed."""

    pass


class UnhandledResponse(Exception):
    """Received unknown response."""

    pass


class InvalidResponse(Exception):
    """Received an invalid response (not an ack/nack)."""

    pass


class InvalidResponseDeviceId(Exception):
    """Received a response for some other device id."""

    pass


class NotEnoughData(Exception):
    """Received not enough data."""

    pass


class InvalidResponseChecksum(Exception):
    """Response checksum does not match payload."""

    pass


class NakReceived(Exception):
    """Nak received from the display"""

    pass


class UnknownMethod(Exception):
    """Unknown method."""

    pass
