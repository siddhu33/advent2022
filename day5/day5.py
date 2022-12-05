import re
import copy


def top_crates(crates, crate_idx):
    return next(
        (idx for idx, val in enumerate(crates[crate_idx]) if val == " "),
        len(crates[crate_idx]),
    )


def move_crates(crates, top_idx, to_move, start, end, part1=True):
    crates_to_move = crates[start][top_idx[start] - to_move : top_idx[start]]
    crates_to_move = crates_to_move[::-1] if part1 else crates_to_move
    crates[end] = [i for i in crates[end] + crates_to_move if i != " "]
    for idx in range(top_idx[start] - to_move, top_idx[start]):
        crates[start][idx] = " "

    top_idx[start] = top_crates(crates, start)
    top_idx[end] = top_crates(crates, end)


def print_stack(part1):
    out = ""
    for stack in part1:
        out += [i for i in stack if i != " "][-1]

    print(out)


def part1_move(instructions, part1, top_idx):
    for to_move, start, end in instructions:
        move_crates(part1, top_idx, to_move, start - 1, end - 1)


def part2_move(instructions, part1, top_idx):
    for to_move, start, end in instructions:
        move_crates(part1, top_idx, to_move, start - 1, end - 1, part1=False)


def main():
    lines = (line.rstrip("\n") for line in open("day5/day5.txt", "r").readlines())
    crates = []
    instructions = []
    crate = True
    instr_ptn = re.compile("move (.*) from (.*) to (.*)")
    for line in lines:
        if line == "":
            crate = False
            continue
        if crate:
            crates.append([line[i] for i in range(1, len(line), 4)])
        else:
            instructions.append(tuple(int(i) for i in instr_ptn.match(line).groups()))

    size = int(crates[-1][-1])
    part1 = [[] for i in range(size)]
    crates = crates[:-1]
    for row in crates:
        for idx in range(size):
            part1[idx].insert(0, row[idx])

    part2 = copy.deepcopy(part1)

    top_idx = {idx: top_crates(part1, idx) for idx in range(size)}
    top_idx2 = copy.deepcopy(top_idx)

    part1_move(instructions, part1, top_idx)
    print_stack(part1)

    part2_move(instructions, part2, top_idx2)
    print_stack(part2)


if __name__ == "__main__":
    main()
