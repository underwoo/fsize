#!/usr/bin/env python3

import re
import math
import src.fsize.fsize as fsize


numbers = [
    1,
    1024,
    12345,
    123455,
    1234567,
    12345678,
    123456789,
    1234567890,
]

for number in numbers:
    n = fsize.FSize(number, "MiB")
    print(f"number: {n:b}")
    print(f"{n:M} MiB")
    print("")
