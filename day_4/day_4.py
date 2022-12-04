class AoC4:

    def __init__(self) -> None:
        self.elves = []
        with open('input.txt') as f:
            for line in f.readlines():
                self.elves.append([self._get_range(elf) for elf in line.replace('\n', '').split(',')])
                
    def _get_range(self, elf):
        start, end = [int(r) for r in elf.split('-')]
        return set(range(start, end + 1)) 

    def _full_overlap(self, elf1, elf2):
        return not (elf1 - elf2) or not (elf2 - elf1)

    def _simple_overlap(self, elf1, elf2):
        return len(elf1 - elf2) != len(elf1) or len(elf2 - elf1) != len(elf2)
    
    def question1(self):
        return len([team for team in self.elves if self._full_overlap(*team)])

    def question2(self):
        return len([team for team in self.elves if self._simple_overlap(*team)])

aoc = AoC4()
print(aoc.question1())
print(aoc.question2())
