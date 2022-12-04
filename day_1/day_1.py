class AoC1:

    def __init__(self) -> None:
        elves = []
        actual = []
        with open('input.txt') as f:
            for line in f.readlines():
                value  = line.replace('\n', '')
                if value:
                    actual.append(int(value))
                else:
                    elves.append(actual);
                    actual = []
        self.snacks = [sum(e) for e in elves]

    def question1(self):
        return max(self.snaks)

    def question2(self):
        return sum(sorted(self.snaks, reverse=True)[:3])


aoc = AoC1()
print(aoc.question1())
print(aoc.question2())
