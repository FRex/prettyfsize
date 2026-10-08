def prettyfsize(fsize: int) -> str:
    if fsize < 0:
        return "-" + prettyfsize(-fsize)
    if fsize == 1:
        return "1 Byte"
    if fsize < 1024:
        return f"{fsize} Bytes"
    if fsize < 1024 * 1024:
        return f"{fsize / 1024:.3f} KiB"
    if fsize < 1024 * 1024 * 1024:
        return f"{fsize / (1024 * 1024):.3f} MiB"
    if fsize < 1024 * 1024 * 1024 * 1024:
        return f"{fsize / (1024 * 1024 * 1024):.3f} GiB"
    return f"{fsize / (1024 * 1024 * 1024 * 1024):.3f} TiB"


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) == 3 and args[1] == "to":
        for x in range(int(args[0]), int(args[2]) + 1):
            print(prettyfsize(x))
    else:
        for arg in args:
            print(prettyfsize(int(arg)))
