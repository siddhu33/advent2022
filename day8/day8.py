def main():
    lines = (l.rstrip("\n") for l in open("day8/day8.txt", "r").readlines())
    grid = [[int(i) for i in l] for l in lines]
    part1(grid)
    part2(grid)


def part1(grid):
    visible = 0
    max_viewing_score = 0
    for row in range(1, len(grid) - 1):
        val = grid[row]
        for col in range(1, len(val) - 1):
            num = grid[row][col]
            prev_rows = [r[col] for r in grid[:row]]
            after_rows = [r[col] for r in grid[row + 1 :]]
            prev_cols = grid[row][:col]
            after_cols = grid[row][col + 1 :]
            max_viewing_score = max(
                max_viewing_score,
                calc_viewing_score(
                    num, [prev_rows[::-1], after_rows, prev_cols[::-1], after_cols]
                ),
            )
            neighbours = [prev_rows, after_rows, prev_cols, after_cols]
            if any(all(num > i for i in n) for n in neighbours):
                visible += 1
    visible += (len(grid) * 2) + (len(grid[0]) - 2) * 2

    print(visible, max_viewing_score)


def calc_viewing_score(num, neighbours):
    viewing = [0, 0, 0, 0]
    for idx, nlist in enumerate(neighbours):
        for val in nlist:
            viewing[idx] += 1
            if num > val:
                continue
            else:
                break

    return viewing[0] * viewing[1] * viewing[2] * viewing[3]


def viewing_scores(grid, row, val, col, num):
    viewing = [0, 0, 0, 0]
    update_row_scores(grid, row, col, viewing, num)
    update_column_scores(grid, row, val, col, viewing, num)
    return viewing


def part2(grid):
    max_viewing = 0
    for row in range(len(grid)):
        val = grid[row]
        for col in range(len(val)):
            num = grid[row][col]
            viewing = viewing_scores(grid, row, val, col, num)

            viewing_score = viewing[0] * viewing[1] * viewing[2] * viewing[3]
            max_viewing = max(max_viewing, viewing_score)

    print(max_viewing)


def update_row_scores(grid, row, col, viewing, num):
    for i in range(row - 1, -1, -1):
        if num > grid[i][col]:
            viewing[0] += 1
        else:
            viewing[0] += 1
            break

    for i in range(row + 1, len(grid)):
        if num > grid[i][col]:
            viewing[1] += 1
        else:
            viewing[1] += 1
            break


def update_column_scores(grid, row, val, col, viewing, num):
    for j in range(col - 1, -1, -1):
        if num > grid[row][j]:
            viewing[2] += 1
        else:
            viewing[2] += 1
            break

    for j in range(col + 1, len(val)):
        if num > grid[row][j]:
            viewing[3] += 1
        else:
            viewing[3] += 1
            break


if __name__ == "__main__":
    main()
