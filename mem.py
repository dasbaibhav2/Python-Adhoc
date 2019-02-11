#!/usr/bin/python3

import ctypes
a=10
b=id(a)
print(ctypes.cast(b, ctypes.py_object).value)
