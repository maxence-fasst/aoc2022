class AoC10:

    def __init__(self) -> None:
        operations = []
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if line == 'noop':
                    operations.append(0)
                else:
                    operations.extend([0, int(line.split(' ').pop())])
        x = 1
        self.results = []
        for operation in operations:
            self.results.append(x)
            x += operation

    def question1(self):
        cycles = [20, 60, 100, 140, 180, 220]
        return sum(self.results[cycle - 1] * cycle for cycle in cycles)

    def question2(self):
        result = []
        for cycle in range(240):
            modulo = cycle % 40
            if modulo - 1 <= self.results[cycle] <= modulo + 1:
                result.append('#')
            else:
                result.append(' ')
            if len(result) == 40:
                print(''.join(result))
                result = []
                

aoc = AoC10()
print(aoc.question1())
aoc.question2()
