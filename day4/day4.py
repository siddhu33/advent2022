def overlap_set(a0, a1):
    s0 = set(range(a0[0], a0[1] + 1, 1))
    s1 = set(range(a1[0], a1[1] + 1, 1))
    return s0.issubset(s1) or s0.issuperset(s1)


def intersection(a0, a1):
    return a0[0] <= a1[1] and a1[0] <= a0[1]


def part1(pairs):
    total = sum(1 for a0, a1 in pairs if overlap_set(a0, a1))
    print(total)


def part2(pairs):
    total = sum(1 for a0, a1 in pairs if intersection(a0, a1))
    print(total)


def main():
    lines = (line.rstrip("\n") for line in open("day4.txt", "r").readlines())
    pairs = [
        [tuple(int(a) for a in tok.split("-", 1)) for tok in line.split(",", 1)]
        for line in lines
    ]
    part1(pairs)
    part2(pairs)


if __name__ == "__main__":
    main()
