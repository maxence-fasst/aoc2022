class AoC21:

    def __init__(self) -> None:
        self.ops = { '+': lambda a, b: a + b, '*': lambda a, b: a * b, '-': lambda a, b: a - b, '/': lambda a, b: a / b }
        self.left_ops = { '+': lambda r, m: r - m, '*': lambda r, m: r / m, '-': lambda r, m: m - r, '/': lambda r, m: m / r}   
        self.right_ops = {'+': lambda r, m: r - m, '*': lambda r, m: r / m, '-': lambda r, m: r + m, '/': lambda r, m: r * m }
        self.monkeys = {}
        with open('input.txt') as f:
            for line in f.readlines():
                monkey, value = line.replace('\n', '').split(': ')
                if value.isdigit():
                    value = int(value)
                self.monkeys[monkey] = value

    def _get_monkey_value(self, monkey):
        value = self.monkeys.get(monkey)
        if isinstance(value, int):
            return value
        sub_monkey_1, operator, sub_monkey_2 = value.split(' ')
        return int(self.ops.get(operator)(self._get_monkey_value(sub_monkey_1), self._get_monkey_value(sub_monkey_2)))

    def _get_humn_value(self, root='root', value_to_reach=None):
        value = self.monkeys.get(root)
        sub_monkey_1, operator, sub_monkey_2 = value.split(' ')
        try:
            monkey_value = self._get_monkey_value(sub_monkey_1)
            ops = self.left_ops
            next_monkey = sub_monkey_2
        except:
            monkey_value = self._get_monkey_value(sub_monkey_2)
            ops = self.right_ops
            next_monkey = sub_monkey_1
        if value_to_reach is None:
            new_value = monkey_value
        else:
            new_value = ops.get(operator)(value_to_reach, monkey_value)
        if 'humn' in [sub_monkey_1, sub_monkey_2]:
            return new_value   
        return self._get_humn_value(next_monkey, value_to_reach=new_value)      
      
    def question1(self):
        return self._get_monkey_value('root')

    def question2(self):
        self.monkeys['humn'] = '?'
        return int(self._get_humn_value())

aoc = AoC21()

print(aoc.question1())
print(aoc.question2())
