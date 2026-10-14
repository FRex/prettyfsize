def prettyfsize(fsize: int) -> str:
    if fsize < 0:
        return "-" + prettyfsize(-fsize)
    if fsize == 1:
        return "1 Byte"
    if fsize < 1024:
        return f"{fsize} Bytes"
    if fsize < 1024**2:
        return f"{fsize / 1024:.3f} KiB"
    if fsize < 1024**3:
        return f"{fsize / (1024 **2):.3f} MiB"
    if fsize < 1024**4:
        return f"{fsize / (1024 ** 3):.3f} GiB"
    return f"{fsize / (1024 ** 4):.3f} TiB"


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) == 3 and args[1] == "to":
        for x in range(int(args[0]), int(args[2]) + 1):
            print(prettyfsize(x))
    else:
        for x in map(int, args):
            print(prettyfsize(x))
