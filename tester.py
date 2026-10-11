import subprocess

# Maximum value for which humanize.naturalsize(value, True) prints in TiB
MAXIMUM_HUMANIZE_VALUE = 2**50 - 4

BINARIES = (
    ("python3", "py/prettyfsize.py"),
    ("python3", "testprograms/usinghumanize.py"),
    ("testprograms/usingc.exe",),
)


def run_all_binaries(args: list) -> list:
    jobs = []
    for binary in BINARIES:
        fullargs = list(binary) + list(map(str, args))
        j = subprocess.Popen(fullargs, stdout=subprocess.PIPE, bufsize=1024 * 1024)
        jobs.append(j)
    ret = []
    for j in jobs:
        ret.append(j.communicate()[0])
    return ret


def test_surrounding(middle, exp):
    print(f"Checking 2^{exp} numbers in both directions around {middle}.")
    magnitude = 2**exp
    outs = run_all_binaries([middle - magnitude, "to", middle + magnitude])
    if len(set(outs)) == 1:
        print("Answer: yes.\n")
    else:
        print("Answer: NO!\n")


def main():
    exp = 20
    midpoints = [0, 2**32, 2**16, MAXIMUM_HUMANIZE_VALUE - 2**exp]
    midpoints = midpoints + [-x for x in midpoints]
    midpoints = sorted(set(midpoints))
    for mid in midpoints:
        test_surrounding(mid, exp)


if __name__ == "__main__":
    main()
