import pytest
from samsung_mdc_ctl.utils import byte_compute_checksum, compute_checksum


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ([0x00], 0x00),
        ([0x01], 0x01),
        ([0x01, 0x01], 0x02),
        ([0x11, 0xFE, 0x01, 0x01], 0x11),
    ],
)
def test_checksum(input_data, expected):
    """Test checksum computation"""
    assert int(compute_checksum(input_data)) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ([0x00], b"00"),
        ([0x01], b"01"),
        ([0x01, 0x01], b"02"),
        ([0x11, 0xFE, 0x01, 0x01], b"11"),
    ],
)
def test_checksum_hex(input_data, expected):
    """Test checksum computation"""
    assert byte_compute_checksum(input_data) == expected
