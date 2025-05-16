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
