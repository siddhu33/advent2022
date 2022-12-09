def main():
    lines = (
        l.rstrip("\n").split(" ", 1) for l in open("day9/day9.txt", "r").readlines()
    )
    instructions = [(direction, int(value)) for direction, value in lines]
    process(instructions, 2)
    process(instructions, 10)


def process(instructions, length):
    knots = [(0, 0) for i in range(length)]
    coordinates = [set() for i in range(length)]
    for direction, steps in instructions:
        for _step in range(steps):
            new_head = step_head(direction, knots[0])
            coordinates[0].add(new_head)
            knots[0] = new_head
            for idx in range(1, length):
                new_tail = step_tail(knots[idx - 1], knots[idx])
                coordinates[idx].add(new_tail)
                knots[idx] = new_tail

    print(len(coordinates[-1]))


def step_head(direction, head):
    match direction:
        case "U":
            return (head[0], head[1] + 1)
        case "D":
            return (head[0], head[1] - 1)
        case "R":
            return (head[0] + 1, head[1])
        case "L":
            return (head[0] - 1, head[1])


def step_tail(new_head, tail):
    x_diff = new_head[0] - tail[0]
    y_diff = new_head[1] - tail[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:  # move tail
        if not x_diff:
            return (tail[0], tail[1] + y_diff // 2)
        elif not y_diff:
            return (tail[0] + x_diff // 2, tail[1])
        else:
            if abs(x_diff) > 1 and abs(y_diff) == 1:
                diff = (x_diff // 2, y_diff)
            elif abs(y_diff) > 1 and abs(x_diff) == 1:
                diff = (x_diff, y_diff // 2)
            elif abs(x_diff) > 1 and abs(y_diff) > 1:
                diff = (x_diff // 2, y_diff // 2)

            return (tail[0] + diff[0], tail[1] + diff[1])

    else:
        return tail


if __name__ == "__main__":
    main()
