import humanize

if __name__ == "__main__":
    import sys

    def f(x):
        return humanize.naturalsize(x, binary=True, format="%.3f")

    # NOTE: using sys.stdout.buffer.write to avoid windows \r\n newlines
    args = sys.argv[1:]
    if len(args) == 3 and args[1] == "to":
        for x in range(int(args[0]), int(args[2]) + 1):
            sys.stdout.buffer.write(f(x).encode("ASCII") + b"\n")
    else:
        for x in map(int, args):
            sys.stdout.buffer.write(f(x).encode("ASCII") + b"\n")
