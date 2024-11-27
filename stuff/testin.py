#!/usr/bin/env python
import re
import time
b = '+9+88+90'

def stack(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

print(list(stack(b, "+")))

