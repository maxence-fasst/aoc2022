class AoC10:

    def __init__(self) -> None:
        self.operations = []
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if line == 'noop':
                    self.operations.append(0)
                else:
                    self.operations.extend([0, int(line.split(' ').pop())])

    def _get_cycle_result(self, cycle):
        result = sum(x for x in self.operations[:cycle - 1]) + 1
        return result * cycle
     
    def question1(self):
        cycles = [20, 60, 100, 140, 180, 220]
        return sum(self._get_cycle_result(cycle) for cycle in cycles)

    def question2(self):
        result = []
        x = 1
        for cycle in range(240):
            modulo = cycle % 40
            if modulo - 1 <= x <= modulo + 1:
                result.append('#')
            else:
                result.append(' ')
            x += self.operations[cycle]
            if len(result) == 40:
                print(''.join(result))
                result = []
                

aoc = AoC10()
print(aoc.question1())
aoc.question2()
