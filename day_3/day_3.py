import string

class AoC3:

    PRIORITIES = { letter: i for i, letter in enumerate([*string.ascii_lowercase, *string.ascii_uppercase], start=1) }

    def __init__(self) -> None:
        self.full_rucksacks = []
        self.split_rucksacks = []
        with open('input.txt') as f:
            for line in f.readlines():
                value  = line.replace('\n', '')
                self.full_rucksacks.append(value)
                half = len(value) // 2
                self.split_rucksacks.append((value[:half], value[half:]))
                
    def _get_priority_value(self, chuncks):
        common = None
        for chunck in chuncks:
            if common:
                common &= set(chunck)
            else:
                common = set(chunck)
        return AoC3.PRIORITIES.get(common.pop())

    def question1(self):
        return sum(self._get_priority_value(split_rucksack) for split_rucksack in self.split_rucksacks)

    def question2(self):
        groups = [self.full_rucksacks[i:i + 3] for i in range(0, len(self.full_rucksacks), 3)]
        return sum(self._get_priority_value(group) for group in groups)     


aoc = AoC3()
print(aoc.question1())
print(aoc.question2())
