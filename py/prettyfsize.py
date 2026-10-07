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
