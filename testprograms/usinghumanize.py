import humanize

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) == 3 and args[1] == "to":
        for x in range(int(args[0]), int(args[2]) + 1):
            print(humanize.naturalsize(x, binary=True, format="%.3f"))
    else:
        for x in map(int, args):
            print(humanize.naturalsize(x, binary=True, format="%.3f"))
