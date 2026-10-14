# prettyfsize

This repository contains implementation of a function that takes in a number
and returns a string representing it as a file size, e.g. 100 becomes
"100 bytes", 123456 becomes "120.562 KiB", 1234567890 becomes "1.150 GiB", etc.

Inspired by `naturalsize` from [humanize](https://pypi.org/project/humanize/),
but implemented differently, more limited (only binary sizes, with 3 digits
after decimal point), and in several languages, in a ready to copy paste form.

Negative numbers **are** supported.

Implementation is in `py/`, `lua/` and `c/` dirs.

Dir `testprograms/` contains test programs for Lua, C and Python using
[humanize](https://pypi.org/project/humanize/), the `py/prettyfsize.py` file
on its own servers as the test program for Python.

The `tester.py` script runs the test programs to ensure they all the
implementations give the same string for the same numbers and `build.sh` builds
the C program (Lua and Python don't require building).
