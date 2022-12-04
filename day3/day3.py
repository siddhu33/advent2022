import sys


def main():
    lines = [line.rstrip("\n") for line in open("day3.txt", "r").readlines()]
    part1(lines)
    part2(lines)

 
def part1(lines):
    priority = 0
    for line in lines:
        comp_length = len(line) // 2
        c1 = line[:comp_length]
        c2 = line[comp_length:]
        s1 = {c for c in c1}
        s2 = {c for c in c2}
        for common in s1.intersection(s2):
            if common.lower() == common:
                priority += ord(common) - ord("a") + 1
            else:
                priority += 26 + ord(common) - ord("A") + 1

    print(priority)


def part2(lines):
    priority = 0
    for idx in range(0, len(lines), 3):
        group = lines[idx : idx + 3]
        overall = None
        for line in group:
            sl = {c for c in line}
            if overall is None:
                overall = sl
            else:
                overall = overall.intersection(sl)

        for common in overall:
            if common.lower() == common:
                priority += ord(common) - ord("a") + 1
            else:
                priority += 26 + ord(common) - ord("A") + 1

    print(priority)


if __name__ == "__main__":
    main()
