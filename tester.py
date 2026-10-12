import subprocess
import shlex
import time

# Maximum value for which humanize.naturalsize(value, True) prints in TiB
MAXIMUM_HUMANIZE_VALUE = 2**50 - 4

BINARIES = (
    ("python3", "py/prettyfsize.py"),
    ("python3", "testprograms/usinghumanize.py"),
    ("testprograms/usingc.exe",),
    ("lua51.exe", "testprograms/usinglua.lua"),
    ("G:/mybin/luajitdir/luajit.exe", "testprograms/usinglua.lua"),
    ("lua52.exe", "testprograms/usinglua.lua"),
    ("lua53.exe", "testprograms/usinglua.lua"),
    ("lua54.exe", "testprograms/usinglua.lua"),
    ("lua55.exe", "testprograms/usinglua.lua"),
)


def run_all_binaries(args: list, benchmark=False) -> list:
    jobs = []
    ret = []
    for binary in BINARIES:
        fullargs = list(binary) + list(map(str, args))
        start_time = time.perf_counter()
        j = subprocess.Popen(fullargs, stdout=subprocess.PIPE, bufsize=1024 * 1024 * 32)
        if benchmark:
            ret.append(j.communicate()[0].replace(b"\r\n", b"\n"))
            print(f"{time.perf_counter() - start_time:.3f}", "--", shlex.join(fullargs))
        jobs.append(j)
    if not benchmark:
        for j in jobs:
            ret.append(j.communicate()[0].replace(b"\r\n", b"\n"))
    return ret


def test_surrounding(middle, exp):
    print(f"Checking 2^{exp} numbers in both directions around {middle}.")
    magnitude = 2**exp
    outs = run_all_binaries([middle - magnitude, "to", middle + magnitude])
    if len(set(outs)) == 1:
        print("Answer: yes.\n")
    else:
        print("Answer: NO!\n")
        # print the binaries used (last part is script name, exe name, etc.)
        print(tuple(bin[-1] for bin in BINARIES))
        # get some examples of failures of formatting, but not all (for performance reasons)
        lines = [out[:9123].split(b"\n")[:20] for out in outs]
        for group in zip(*lines):
            print(group)


def main():
    exp = 20
    midpoints = [0, 2**32, 2**16, MAXIMUM_HUMANIZE_VALUE - 2**exp]
    midpoints = midpoints + [-x for x in midpoints]
    midpoints = sorted(set(midpoints))
    for mid in midpoints:
        test_surrounding(mid, exp)


if __name__ == "__main__":
    main()
