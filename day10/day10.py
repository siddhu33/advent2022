def main():
    lines = [
        l.rstrip("\n").split(" ", 1) for l in open("day10/day10.txt", "r").readlines()
    ]

    num_instructions = len(lines)
    max_cycles = 240
    cycles = 0
    program_counter = 0
    queue = []
    register = 1
    samples = [19, 59, 99, 139, 179, 219]
    signals = []
    crt = []

    while cycles < max_cycles:
        if queue and queue[0][0] == cycles:
            register += queue.pop(0)[1]

        if cycles % 40 in (register - 1, register, register + 1):
            crt.append("#")
        else:
            crt.append(".")

        next = lines[program_counter % num_instructions]
        if next[0] != "noop" and not queue:
            queue.append((cycles + 2, int(next[1])))
            program_counter += 1
        elif next[0] == "noop" and not queue:
            queue.append((cycles + 1, 0))
            program_counter += 1

        if cycles in samples:
            signals.append(register * (cycles + 1))

        cycles += 1

    print(sum(signals))
    for i in range(6):
        print("".join(crt[i * 40 : (i * 40) + 40]))


if __name__ == "__main__":
    main()
