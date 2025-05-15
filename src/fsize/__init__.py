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

__version__ = "0.1.0"

class FSize(float):
    """Represents a file size in bytes.

    A class to represent file sizes in bytes, with conversion capabilities to
    other units (KiB, MiB, GiB, TiB, PiB, EiB or KB, MB, GB, TB, PB, EB).
    """
    __convert__: float

    def __new__(cls, value: Any, units: str="B") -> Self:
        """Create a new FSize instance.

        Create a new FSize instance, which is a subclass of float. The value is
        converted to bytes based on the units given. The default is Bytes
        (Kibibytes).

        Args:
            value (Any): The size of a file or file system.
            units (str): The units of the value. Can be "KiB", "MiB", "GiB",
                "TiB", "PiB", "EiB" or "KB", "MB", "GB", "TB", "PB", "EB".  The
                default is "KiB".
        """
        # Check if the value can be cast to a float
        try:
            value = float(value)
        except ValueError as exc:
            raise ValueError(f"could not convert value to "
                             f"{cls.__name__}: '{value}'") from exc
        # The value must be a positive number
        if value < 0:
            raise ValueError(f"{cls.__name__} cannot be negative: "
                             f"{value}")
        # Perform the conversion to Bytes based on the units given:
        re_units = re.compile(r"([KkMmGgTtPpEe])?(i)?[Bb]")
        in_units = re_units.match(units)
        if in_units is None:
            raise ValueError(f"Unknown units: {units}")
        if in_units[2] or in_units[1] is None:
            # The string contains the "i", or the units are "B" (no
            # size prefix)
            convert = 1024
        else:
            convert = 1000
        if in_units[1] is None:
            pass
        elif in_units[1].upper() == "K":
            value *= convert
        elif in_units[1].upper() == "M":
            value *= (
                convert *
                convert
            )
        elif in_units[1].upper() == "G":
            value *= (
                convert *
                convert *
                convert
            )
        elif in_units[1].upper() == "T":
            value *= (
                convert *
                convert *
                convert *
                convert
            )
        elif in_units[1].upper() == "P":
            value *= (
                convert *
                convert *
                convert *
                convert *
                convert
            )
        elif in_units[1].upper() == "E":
            value *= (
                convert *
                convert *
                convert *
                convert *
                convert *
                convert
            )
        else:
            raise ValueError(f"Unknown units: {units}")
        instance = super().__new__(cls, value)
        instance.__convert__ = convert
        return instance

    def __str__(self) -> str:
        """Return the string representation of the FSize value.

        Returns:
            str: The string representation of the FSize value.
        """
        return f"{self.real}"

    def __repr__(self) -> str:
        """Return the string representation of the FSize value.

        Returns:
            str: The string representation of the FSize value.
        """
        return self.__str__()

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
        print(f"format_spec: {format_spec}")
        re_spec_fill = r"(?P<fill>.)??"
        re_spec_align = r"(?P<align>[<>^])?"
        re_spec_options = rf"(?:{re_spec_fill}{re_spec_align})"

        re_spec_width = r"(?P<width>\d+)?"
        re_spec_grouping = r"(?P<grouping>[_,])?"
        re_spec_unit = r"(?P<unit>[KkMmGgTtPpEe])?"
        re_spec_format = (rf"{re_spec_width}"
                          rf"{re_spec_grouping}"
                          rf"{re_spec_unit}")

        re_format_spec = re.compile(
            r"^" +
            rf"{re_spec_options}" +
            rf"{re_spec_format}" +
            r"i?[Bb]?$"
        )

        # Default values for format specifiers
        fill= ""
        align = ""
        width = 0
        grouping = ""
        unit = "K"

        match = re_format_spec.match(format_spec)
        if match:
            fill = match.group("fill") \
                if match.group("fill") else fill
            align = match.group("align") \
                if match.group("align") else align
            width = int(match.group("width"))\
                if match.group("width") else width
            grouping = match.group("grouping") \
                if match.group("grouping") else grouping
            unit = match.group("unit").upper() \
                if match.group("unit") else unit
        else:
            raise ValueError(
                f"Unknown format code '{format_spec}'",
                f"for object of type '{self.__class__.__name__}'"
            )

        # Convert the number to the appropriate unit
        n = self.real
        if unit == "K":
            n = self.to_k()
        elif unit == "M":
            n =  self.to_m()
        elif unit == "G":
            n = self.to_g()
        elif unit == "T":
            n = self.to_t()
        elif unit == "P":
            n = self.to_p()
        elif unit == "E":
            n = self.to_e()

        out_format_spec = (
            f"{fill}{align}{width}{grouping}" +
            "." +
            f"{max(0, width, math.ceil(math.log10(n)))}g"
        )
        try:
            return f"{n:{out_format_spec}}"
        except Exception as exc:
            raise ValueError(
                f"Unknown format code '{format_spec}'",
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
        return self.real / self.__convert__

    def to_m(self) -> float:
        """Return the value in MB or MiB.

        Returns:
            float: The value in MB or MiB.
        """
        return self.real / (self.__convert__ *
                            self.__convert__)

    def to_g(self) -> float:
        """Return the value in GB or GiB.

        Returns:
            float: The value in GB or GiB.
        """
        return self.real / (self.__convert__ *
                            self.__convert__ *
                            self.__convert__)

    def to_t(self) -> float:
        """Return the value in TB or TiB.

        Returns:
            float: The value in TB or TiB.
        """
        return self.real / (self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__)

    def to_p(self) -> float:
        """Return the value in PB or PiB.

        Returns:
            float: The value in PB or PiB.
        """
        return self.real / (self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__)

    def to_e(self) -> float:
        """Return the value in EB or EiB.

        Returns:
            float: The value in EB or EiB.
        """
        return self.real / (self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__ *
                            self.__convert__)
