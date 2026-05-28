# -*- coding: utf-8 -*-
"""FSize is a class to represent file and other computer-based sizes.

This module provides a class to represent file sizes in bytes, with
conversion capabilities to other units (KiB, MiB, GiB, TiB, PiB, EiB or
KB, MB, GB, TB, PB, EB). The class is a subclass of float and can be
used in mathematical operations. It also provides a way to format the
size in a human-readable way, with options for grouping and alignment.

Format
------

The FSize class can be formatted using most of the same options as the
built-in float type.  However, FSize is always positive, and the format
can contain the SI (International System of Units) prefixes for binary
prefixes (KiB, MiB, GiB, TiB, PiB, EiB) or decimal prefixes (KB, MB,
GB, TB, PB, EB) to convert the number to those units.

Examples
--------

1. Set the file size of two files, and compare them:
    >>> from fsize import FSize
    >>> file1 = FSize(1024, "KiB")
    >>> file2 = FSize(1, "MiB")
    >>> file1 == file2
    True
2. Format the file size in MB:
    >>> file1 = FSize(1.2e6, "B")
    >>> print(f"{file1:2M} MB")
    1.1 MB
3. Convert a number from GiB to KiB:
    >>> value = FSize(1, "GiB")
    >>> value.to_k()
    1048576.0
"""

import math
import re
from typing import Any, Self

__all__ = ["FSize"]

__version__ = "0.3.0"

_UNIT_POWERS: dict[str, int] = {
    "K": 1,
    "M": 2,
    "G": 3,
    "T": 4,
    "P": 5,
    "E": 6,
}

_RE_STR_PARSE = re.compile(
    r"(\d*\.?\d+)\s*(?:([KkMmGgTtPpEe]i?[Bb])|[Bb])?\s*$"
)
_RE_UNITS = re.compile(r"([KkMmGgTtPpEe])?(i)?[Bb]$")
_RE_FORMAT_SPEC = re.compile(
    r"^(?:(?P<fill>.)??(?P<align>[<>^])?)"
    r"(?P<width>\d+)?(?P<grouping>[_,])?(?P<unit>[KkMmGgTtPpEe])?i?[Bb]?$"
)


class FSize(float):
    """Represents a file size in bytes.

    A class to represent file sizes in bytes, with conversion capabilities to
    other units (KiB, MiB, GiB, TiB, PiB, EiB or KB, MB, GB, TB, PB, EB).
    """

    _convert: float

    def __new__(cls, value: Any, units: str = "B") -> Self:
        """Create a new FSize instance.

        Create a new FSize instance, which is a subclass of float. The value is
        converted to bytes based on the units given. The default unit is
        Bytes ("B").

        Args:
            value (Any): The size of a file or file system.
            units (str): The units of the value. Can be "KiB", "MiB", "GiB",
                "TiB", "PiB", "EiB" or "KB", "MB", "GB", "TB", "PB", "EB".
                The default is "B" (Bytes).
        """
        try:
            if isinstance(value, str):
                m = _RE_STR_PARSE.match(value)
                if m is None:
                    raise ValueError
                value = m.group(1)
                if m.group(2) is not None:
                    units = m.group(2)
            # Check if the value can be cast to a float
            value = float(value)
        except ValueError as exc:
            raise ValueError(
                f"could not convert value to {cls.__name__}: '{value}'"
            ) from exc
        # The value must be a positive number
        if value < 0:
            raise ValueError(f"{cls.__name__} cannot be negative: {value}")
        # Perform the conversion to Bytes based on the units given:
        in_units = _RE_UNITS.match(units)
        if in_units is None:
            raise ValueError(f"Unknown units: {units}")
        has_i = in_units[2] is not None
        no_prefix = in_units[1] is None
        convert = 1024 if (has_i or no_prefix) else 1000
        if in_units[1] is not None:
            prefix = in_units[1].upper()
            value *= convert ** _UNIT_POWERS[prefix]
        instance = super().__new__(cls, value)
        instance._convert = convert
        return instance

    def __str__(self) -> str:
        """Return the string representation of the FSize value.

        Returns:
            str: The string representation of the FSize value.
        """
        return f"{self.real}"

    def __repr__(self) -> str:
        """Return an unambiguous representation of the FSize value.

        Returns:
            str: A representation that identifies the type and value.
        """
        return f"FSize({self.real})"

    def __format__(self, format_spec: str) -> str:
        """Format the FSize value.

        Format the FSize value according to the given format specifier. The
        format specifier can include most of the same options as the built-in
        float type, but with the following differences:

        - FSize uses the SI (International System of Units) prefixes for binary
          prefixes (KiB, MiB, GiB, TiB, PiB, EiB) or decimal prefixes (KB, MB,
          GB, TB, PB, EB).  You cannot use the float format specifiers for
          binary prefixes (e.g. "f", "g", or "n").  The size will be converted
          to the chosen units.
        - FSize only accepts the width specifier.  The precision specifier is
          chosen from the output value and the width specified.
        - FSize does not support the "+" or "-" sign specifiers.
        - FSize will attempt to not display the number in scientific notation.
          The exception to this is for very small numbers with a negative
          exponent.

        Arguments:
            format_spec (str): The format specifier.  The default is "K", which
                corresponds to the float format specifier ".4g".

        Returns:
            str: The formatted string.

        Raises:
            ValueError: If the format specifier is invalid.

        .. seealso::

            - `Python Format Specification Mini-Language`_

        .. _Python Format Specification Mini-Language:
           https://docs.python.org/3/library/string.html#format-specification-mini-language
        """
        # Default values for format specifiers
        fill = ""
        align = ""
        width = 0
        grouping = ""
        unit = "K"

        match = _RE_FORMAT_SPEC.match(format_spec)
        if match:
            fill = match.group("fill") if match.group("fill") else fill
            align = match.group("align") if match.group("align") else align
            width = int(match.group("width")) if match.group("width") else width
            grouping = (
                match.group("grouping") if match.group("grouping") else grouping
            )
            unit = match.group("unit").upper() if match.group("unit") else unit
        else:
            raise ValueError(
                f"Unknown format code '{format_spec}' "
                f"for object of type '{self.__class__.__name__}'"
            )

        # Convert the number to the appropriate unit
        n = self.real
        if unit == "K":
            n = self.to_k()
        elif unit == "M":
            n = self.to_m()
        elif unit == "G":
            n = self.to_g()
        elif unit == "T":
            n = self.to_t()
        elif unit == "P":
            n = self.to_p()
        elif unit == "E":
            n = self.to_e()

        log_digits = math.ceil(math.log10(n)) if n > 0 else 0
        out_format_spec = (
            f"{fill}{align}{width}{grouping}"
            + "."
            + str(max(0, width, log_digits))
            + "g"
        )
        try:
            return f"{n:{out_format_spec}}"
        except Exception as exc:
            raise ValueError(
                f"Unknown format code '{format_spec}' "
                f"for object of type '{self.__class__.__name__}'"
            ) from exc

    def to_bytes(self) -> float:
        """Return the value in bytes.

        Returns:
            float: The value in bytes.
        """
        return self.real

    def to_k(self) -> float:
        """Return the value in KB or KiB.

        Returns:
            float: The value in KB or KiB.
        """
        return self.real / self._convert

    def to_m(self) -> float:
        """Return the value in MB or MiB.

        Returns:
            float: The value in MB or MiB.
        """
        return self.real / self._convert**2

    def to_g(self) -> float:
        """Return the value in GB or GiB.

        Returns:
            float: The value in GB or GiB.
        """
        return self.real / self._convert**3

    def to_t(self) -> float:
        """Return the value in TB or TiB.

        Returns:
            float: The value in TB or TiB.
        """
        return self.real / self._convert**4

    def to_p(self) -> float:
        """Return the value in PB or PiB.

        Returns:
            float: The value in PB or PiB.
        """
        return self.real / self._convert**5

    def to_e(self) -> float:
        """Return the value in EB or EiB.

        Returns:
            float: The value in EB or EiB.
        """
        return self.real / self._convert**6
