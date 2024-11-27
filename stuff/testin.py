#!/usr/bin/env python
import re
b = 'This is a'
print(b.index('is'))

def stack(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield
print(f"list(stack(b, "is"))")