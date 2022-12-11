import numpy as np

class Monkey:
    
    all_monkeys = []
    lcm = 0
    
    def __init__(self, idx:int, starting_items: list, operation, rvalue, divisor: int, true_monkey: int, false_monkey: int):
        self.idx = idx
        self.starting_items = starting_items
        self.operation = operation
        self.rvalue = rvalue
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected = 0
        
    def calc_operation(self, item):
        if self.operation == "*" and self.rvalue == "old":
            return (item ** 2) % Monkey.lcm
        elif self.operation == "*":
            return (item * int(self.rvalue)) % Monkey.lcm
        elif self.operation == "+":
            return (item + int(self.rvalue)) % Monkey.lcm

    def test(self, item) -> None:
        operated = self.calc_operation(item)
        #operated = operated // 3  # monkey bored

        divisible = operated % self.divisor == 0
        to_throw = self.true_monkey if divisible else self.false_monkey
        to_throw_monkey = self.all_monkeys[to_throw]
        to_throw_monkey.starting_items.append(operated)
        self.inspected += 1
        
    def test_all(self):
        while self.starting_items:
            item = self.starting_items.pop(0)
            self.test(item)
            
    def __repr__(self) -> str:
        return f"Monkey[{self.idx},{len(self.starting_items)},{self.inspected}]"
    
    def __str__(self) -> str:
        return self.__repr__()

def monkey_round():
    for monkey in Monkey.all_monkeys:
        monkey.test_all()

def main():
    with open("day11/day11.txt", "r") as f:
        all_monkey_data = f.read()

    for idx, monkey_data in enumerate(all_monkey_data.split("\n\n")):
        monkey_lines = monkey_data.split("\n")
        starting_items = [
            int(i)
            for i in monkey_lines[1].partition("  Starting items: ")[-1].split(", ")
        ]
        operation = monkey_lines[2].partition("  Operation: new = old ")[-1]
        operation, rvalue = operation.split()
        divisor = int(monkey_lines[3].partition("  Test: divisible by ")[-1])
        true_monkey = int(monkey_lines[4].partition("    If true: throw to monkey ")[-1])
        false_monkey = int(monkey_lines[5].partition("    If false: throw to monkey ")[-1])
        Monkey.all_monkeys.append(Monkey(idx, starting_items, operation, rvalue, divisor, true_monkey, false_monkey))
    
    Monkey.lcm = int(np.lcm.reduce([ m.divisor for m in Monkey.all_monkeys]))
    
    for i in range(10000):
        monkey_round()
        
    top_inspectors = sorted(monkey.inspected for monkey in Monkey.all_monkeys)[-2:]
    print(top_inspectors[0]*top_inspectors[1])
    
            
        
        


if __name__ == "__main__":
    main()
