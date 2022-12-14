import copy
import math
import re

class AoC11:

    def __init__(self) -> None:
        ops = {'+': lambda a, b: a + b, '*': lambda a, b: a * b, '-': lambda a, b: a - b, '/': lambda a, b: a / b}
        self.initial_monkeys = []
        actual_monkey = None
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.strip().replace('\n', '')
                if not line:
                    self.initial_monkeys.append(actual_monkey)
                    continue
                if line.startswith('Monkey'):
                    actual_monkey = { 'items': [], 'checks': 0 }
                elif line.startswith('Starting'):
                    items = line.split(': ')[-1].split(', ')
                    actual_monkey['items'] = [int(item) for item in items]
                elif line.startswith('Operation'):
                    *_, operator, value = line.split(' ')
                    actual_monkey['operation'] = lambda operator=operator, value=value: lambda old: ops[operator](old, old if value == 'old' else int(value)) 
                elif line.startswith('Test'):
                    actual_monkey['divide_by'] = int(re.match('Test: divisible by (\d+)', line).groups()[0])
                elif line.startswith('If true'):
                    actual_monkey['monkey_if_true'] = int(re.match('If true: throw to monkey (\d+)', line).groups()[0])
                elif line.startswith('If false'):
                    actual_monkey['monkey_if_false'] = int(re.match('If false: throw to monkey (\d+)', line).groups()[0])
            self.initial_monkeys.append(actual_monkey)
        self.monkeys = copy.deepcopy(self.initial_monkeys)
        self.ppcm = math.lcm(*[monkey.get('divide_by') for monkey in self.monkeys])

    def _reset(self):
        self.monkeys = copy.deepcopy(self.initial_monkeys)

    def _run_monkey_turn(self, monkey, divide_by_three):
        items = monkey.get('items')
        while items:
            item = items.pop(0)
            monkey['checks'] = monkey.get('checks') + 1
            new = monkey.get('operation')()(item)
            if divide_by_three:
                new //= 3
            new = new % self.ppcm
            if new % monkey.get('divide_by') == 0:
                next_monkey = monkey.get('monkey_if_true')
            else:
                next_monkey = monkey.get('monkey_if_false')
            next_monkey = self.monkeys[next_monkey]
            next_monkey.get('items').append(new)

    def _run_turn(self, divide_by_three=True):
        for monkey in self.monkeys:
            self._run_monkey_turn(monkey, divide_by_three=divide_by_three)
     
    def question1(self):
        for _ in range(20):
            self._run_turn(divide_by_three=True)
        return math.prod(sorted([monkey.get('checks') for monkey in self.monkeys], reverse=True)[:2])

    def question2(self):
        self._reset()
        for _ in range(10000):
            self._run_turn(divide_by_three=False)
        return math.prod(sorted([monkey.get('checks') for monkey in self.monkeys], reverse=True)[:2])
                

aoc = AoC11()

print(aoc.question1())
print(aoc.question2())
