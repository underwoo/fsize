FSize: File size converter and formatter
========================================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

FSize is a class to simplify the use and conversion of numbers related to the
computer sizes (e.g., file, disk, memory, etc).  FSize also has its own format
specifier that will convert the numerical value to the chosen SI (International
System of Units) prefixes for binary prefixes.

FSize Format Specifier
----------------------

The format specifier is based on the [float format specifier
mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language),
but only accepts the width, and accepts these SI (International System of Units)
prefixes for binary prefixes (KiB, MiB, GiB, TiB, PiB, EiB) and decimal prefixes
(KB, MB, GB, TB, PB, EB).  However, how the number is initialized will determine
if the value will be in converted as binary or decimal, not with the inclusion
or absence of the "i".

Since the FSize value must be positive, the "+", "-", and " " float specifier
sign specifiers.

An example would be `f"{size:4MiB}"` to display `size` with at least a width of
4, but if the number is larger than 4 wide, e.g., `123345`, size will expand to
ensure the number is not displayed using scientific notation.

Install
-------

FSize can be installed using pip:

```
pip install fsize
```

However, this doesn't work yet, as FSize does not have a package uploaded
anywhere.

Examples
--------

1. Set the file size of two files, and compare them:
```python
>>> from fsize import FSize
>>> file1 = FSize(1024, "KiB")
>>> file2 = FSize(1, "MiB")
>>> file1 == file2
True
```
2. Format the file size in MB:
```
>>> file1 = FSize(1.2e6, "B")
>>> print(f"{file1:2M} MB")
1.1 MB
```
3. Convert a number from GiB to KiB:
```
>>> value = FSize(1, "GiB")
>>> value.to_k()
1048576.0
```
