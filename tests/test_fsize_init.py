#!/usr/bin/env python3
"""Test initialization of FSize class with different units.

Tests the initialization of the FSize class with various units
and checks if the conversion to bytes is done correctly.

The tests cover the following units:
- Bytes
- Kilobytes
- Megabytes
- Gigabytes
- Terabytes
- Petabytes
- Exabytes
- Kibibytes
- Mebibytes
- Gibibytes
- Tebibytes
- Pebibytes
- Exbibytes

The tests also check for invalid units and ensure that the
FSize class raises the appropriate exceptions.
"""

import pytest

from fsize import FSize


def test_byte():
    """Test initialization of FSize with a number in bytes"""
    var1 = FSize(1024)
    assert isinstance(var1, FSize)
    assert var1 == 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0)
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0
    assert var2.__convert__ == 1024


def test_kilobyte():
    """Test initialization of FSize with a number in kilobytes"""
    var1 = FSize(1024, "kb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "KB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000
    assert var2.__convert__ == 1000


def test_megabyte():
    """Test initialization of FSize with a number in megabytes"""
    var1 = FSize(1024, "mb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "MB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000 * 1000
    assert var2.__convert__ == 1000


def test_gigabyte():
    """Test initialization of FSize with a number in gigabytes"""
    var1 = FSize(1024, "gb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000 * 1000 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "GB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000 * 1000 * 1000
    assert var2.__convert__ == 1000


def test_terabyte():
    """Test initialization of FSize with a number in terabytes"""
    var1 = FSize(1024, "tb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000 * 1000 * 1000 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "TB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000 * 1000 * 1000 * 1000
    assert var2.__convert__ == 1000


def test_petabyte():
    """Test initialization of FSize with a number in petabytes"""
    var1 = FSize(1024, "pb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000 * 1000 * 1000 * 1000 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "PB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000 * 1000 * 1000 * 1000 * 1000
    assert var2.__convert__ == 1000


def test_exabyte():
    """Test initialization of FSize with a number in exabytes"""
    var1 = FSize(1024, "eb")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    assert var1.__convert__ == 1000
    var2 = FSize(123456789.0, "EB")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    assert var2.__convert__ == 1000


def test_kibibyte():
    """Test initialization of FSize with a number in kibibytes"""
    var1 = FSize(1024, "KiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Kib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024
    assert var2.__convert__ == 1024


def test_mebibyte():
    """Test initialization of FSize with a number in mebibytes"""
    var1 = FSize(1024, "MiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Mib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024 * 1024
    assert var2.__convert__ == 1024


def test_gibibyte():
    """Test initialization of FSize with a number in gibibytes"""
    var1 = FSize(1024, "GiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024 * 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Gib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024 * 1024 * 1024
    assert var2.__convert__ == 1024


def test_tebibyte():
    """Test initialization of FSize with a number in tebibytes"""
    var1 = FSize(1024, "TiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024 * 1024 * 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Tib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024 * 1024 * 1024 * 1024
    assert var2.__convert__ == 1024


def test_pebibyte():
    """Test initialization of FSize with a number in pebibytes"""
    var1 = FSize(1024, "PiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Pib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024 * 1024 * 1024 * 1024 * 1024
    assert var2.__convert__ == 1024


def test_exbibyte():
    """Test initialization of FSize with a number in exbibytes"""
    var1 = FSize(1024, "EiB")
    assert isinstance(var1, FSize)
    assert var1 == 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert var1.__convert__ == 1024
    var2 = FSize(123456789.0, "Eib")
    assert isinstance(var2, FSize)
    assert var2 == 123456789.0 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    assert var2.__convert__ == 1024


def test_invalid_unit():
    """Test initialization of FSize with an invalid unit"""
    with pytest.raises(ValueError) as exc:
        FSize(1024, "invalid")
    assert "Unknown units: invalid" in str(exc.value)


def test_invalid_unit_k():
    """Test initialization of FSize with an invalid unit (k)"""
    with pytest.raises(ValueError) as exc:
        FSize(1024, "k")
    assert "Unknown units: k" in str(exc.value)


def test_invalid_string():
    """Test initialization of FSize with a string that does not
    convert to a valid size with units"""
    with pytest.raises(ValueError) as exc:
        FSize("MiB")
    assert "could not convert value to FSize: 'MiB'" in str(exc.value)


def test_invalid_string_two_dots():
    """Test initialization of FSize with a string that does not
    convert to a valid size, string has two dots"""
    with pytest.raises(ValueError) as exc:
        FSize(".2.34")
    assert "could not convert value to FSize: '.2.34'" in str(exc.value)


def test_string_with_binary_units():
    """Test initialization of FSize with a string containing binary units"""
    var = FSize("1.5 GiB")
    assert var == FSize(1.5, "GiB")
    assert var.__convert__ == 1024


def test_string_with_decimal_units():
    """Test initialization of FSize with a string containing decimal units"""
    var = FSize("1024 KB")
    assert var == FSize(1024, "KB")
    assert var.__convert__ == 1000


def test_string_no_units():
    """Test initialization of FSize with a numeric string and no units"""
    var = FSize("1024")
    assert var == FSize(1024)
    assert var.__convert__ == 1024


def test_string_leading_whitespace():
    """Test that a string with leading whitespace raises ValueError"""
    with pytest.raises(ValueError):
        FSize("  1.5 MiB")


def test_string_empty():
    """Test that an empty string raises ValueError"""
    with pytest.raises(ValueError):
        FSize("")


def test_zero():
    """Test that zero is a valid size"""
    var = FSize(0)
    assert isinstance(var, FSize)
    assert var == 0
    assert var.__convert__ == 1024
    assert var.to_bytes() == 0.0
    assert var.to_k() == 0.0
    assert var.to_m() == 0.0
    assert str(var) == "0.0"
    assert FSize("0") == FSize(0)
    assert FSize(0, "KB") == 0
    assert format(FSize(0), "K") == "0"
    assert format(FSize(0), "M") == "0"
    assert FSize(0, "GiB") == 0
    assert format(FSize(0), "K") == "0"


def test_negative_value():
    """Test that a negative value raises ValueError"""
    with pytest.raises(ValueError) as exc:
        FSize(-1)
    assert "cannot be negative" in str(exc.value)


def test_to_bytes():
    """Test conversion to bytes"""
    assert FSize(1024).to_bytes() == 1024.0
    assert FSize(1, "KiB").to_bytes() == 1024.0
    assert FSize(1, "KB").to_bytes() == 1000.0


def test_to_k():
    """Test conversion to kibibytes and kilobytes"""
    assert FSize(1, "KiB").to_k() == 1.0
    assert FSize(1, "MiB").to_k() == 1024.0
    assert FSize(1, "KB").to_k() == 1.0
    assert FSize(1, "MB").to_k() == 1000.0


def test_to_m():
    """Test conversion to mebibytes and megabytes"""
    assert FSize(1, "MiB").to_m() == 1.0
    assert FSize(1, "GiB").to_m() == 1024.0
    assert FSize(1, "MB").to_m() == 1.0
    assert FSize(1, "GB").to_m() == 1000.0


def test_to_g():
    """Test conversion to gibibytes and gigabytes"""
    assert FSize(1, "GiB").to_g() == 1.0
    assert FSize(1, "TiB").to_g() == 1024.0
    assert FSize(1, "GB").to_g() == 1.0
    assert FSize(1, "TB").to_g() == 1000.0


def test_to_t():
    """Test conversion to tebibytes and terabytes"""
    assert FSize(1, "TiB").to_t() == 1.0
    assert FSize(1, "PiB").to_t() == 1024.0
    assert FSize(1, "TB").to_t() == 1.0
    assert FSize(1, "PB").to_t() == 1000.0


def test_to_p():
    """Test conversion to pebibytes and petabytes"""
    assert FSize(1, "PiB").to_p() == 1.0
    assert FSize(1, "EiB").to_p() == 1024.0
    assert FSize(1, "PB").to_p() == 1.0
    assert FSize(1, "EB").to_p() == 1000.0


def test_to_e():
    """Test conversion to exbibytes and exabytes"""
    assert FSize(1, "EiB").to_e() == 1.0
    assert FSize(1, "EB").to_e() == 1.0


def test_binary_decimal_differ():
    """Test that binary and decimal conversions produce different byte counts"""
    assert FSize(1, "KiB").to_bytes() == 1024.0
    assert FSize(1, "KB").to_bytes() == 1000.0
    assert FSize(1, "KiB").to_bytes() != FSize(1, "KB").to_bytes()


def test_str():
    """Test string representation of FSize"""
    assert str(FSize(1024)) == "1024.0"
    assert str(FSize(1.5)) == "1.5"


def test_repr():
    """Test repr of FSize matches str"""
    assert repr(FSize(1024)) == "1024.0"
    assert repr(FSize(1024)) == str(FSize(1024))


def test_arithmetic_returns_float():
    """Test that arithmetic on FSize returns plain float, not FSize"""
    result = FSize(1024) + FSize(1024)
    assert result == 2048.0
    assert isinstance(result, float)
    assert not isinstance(result, FSize)


def test_format_unit():
    """Test basic unit conversion in format spec"""
    assert f"{FSize(1024 * 1024):K}" == "1024"
    assert f"{FSize(1024 * 1024):M}" == "1"


def test_format_ib_suffix_accepted():
    """Test that iB suffix in format spec is accepted and ignored"""
    assert f"{FSize(1024 * 1024):MiB}" == f"{FSize(1024 * 1024):M}"
    assert f"{FSize(1024 * 1024):MB}" == f"{FSize(1024 * 1024):M}"


def test_format_width():
    """Test width specifier in format spec"""
    assert f"{FSize(1024):8K}" == "       1"


def test_format_align():
    """Test alignment specifier in format spec"""
    assert f"{FSize(1024):<8K}" == "1       "
    assert f"{FSize(1024):>8K}" == "       1"


def test_format_fill_and_align():
    """Test fill character with alignment in format spec"""
    assert f"{FSize(1024):*>8K}" == "*******1"
    assert f"{FSize(1024):0<8K}" == "10000000"


def test_format_grouping():
    """Test grouping separator in format spec"""
    assert f"{FSize(1024 * 1024 * 1024):,K}" == "1,048,576"


def test_format_decimal():
    """Test format with a decimal-mode FSize"""
    assert format(FSize(1, "MB"), "M") == "1"
    assert format(FSize(1, "KB"), "K") == "1"


def test_format_invalid():
    """Test that an invalid format spec raises ValueError"""
    with pytest.raises(ValueError):
        format(FSize(1024), "5.2f")
    with pytest.raises(ValueError):
        format(FSize(1024), "f")
