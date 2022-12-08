class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = {}

    @property
    def size(self):
        return sum(size for size, _name in self.files) + sum(
            v.size for v in self.directories.values()
        )

    def __str__(self) -> str:
        return f"Node[{self.name}, {self.parent}, {self.size}]"

    def __repr__(self) -> str:
        return self.__str__()


def main():
    lines = [l.rstrip("\n") for l in open("day7/day7.txt", "r").readlines()]
    node = Node("/", None)
    root = node
    directories = []
    for line in lines[1:]:
        if line.startswith("$"):
            lsplit = line.split(" ")
            command = lsplit[1]
            if command == "cd":
                arg = lsplit[2]
                if arg == "..":
                    node = node.parent
                else:
                    node = node.directories[arg]
            elif command == "ls":
                continue
        else:
            lvalue, _, rvalue = line.partition(" ")
            if lvalue == "dir":
                if rvalue not in node.directories:
                    new_node = Node(rvalue, node)
                    node.directories[rvalue] = new_node
                    directories.append(new_node)
            else:
                node.files.append((int(lvalue), rvalue))

    part1(directories)
    part2(root, directories)


def part1(directories):
    elig_nodes = [n for n in directories if n.size <= 100000]
    print(sum(n.size for n in elig_nodes))


def part2(root, directories):
    unused = 70000000 - root.size
    required = 30000000 - unused
    print(min(n.size for n in directories if n.size >= required))


if __name__ == "__main__":
    main()
