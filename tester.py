from py import prettyfsize
import random
import humanize

# Maximum value for which humanize.naturalsize(value, True) prints in TiB
MAXIMUM_HUMANIZE_VALUE = 2**50 - 4


def _main():

    cases = []

    case = list(range(0, 2**20))
    print(f"All numbers in range [{min(case)}, {max(case)}].")
    cases.append(case)

    exp = 49
    print(f"All powers of two from 0th to {exp}th (inclusive).")
    cases.append([2**x for x in range(exp + 1)])

    print(f"MAXIMUM_HUMANIZE_VALUE aka {MAXIMUM_HUMANIZE_VALUE}")
    cases.append([MAXIMUM_HUMANIZE_VALUE])

    print("All negative versions of these numbers.")
    totest = sum(cases, [])
    totest = totest + [-x for x in totest]

    # dedup and sort
    totest = sorted(set(totest))
    print(f"\nTotal test cases: {len(totest):,}\n")  # newlines for spacing

    okay = 0
    for fsize in totest:
        a = humanize.naturalsize(fsize, binary=True, format="%.3f")
        b = prettyfsize.prettyfsize(fsize)

        if a != b:
            print(fsize, a, b)
        else:
            okay += 1

    print(okay, "okay out of", len(totest))
    print(len(totest) - okay, "broken.")


if __name__ == "__main__":
    _main()
