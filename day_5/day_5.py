import copy
import re
import string

class AoC5:

    def __init__(self) -> None:
        self.stacks = {}
        self.moves = []
        reading_stacks = True
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if not self.stacks:
                    # define number of stacks
                    self.stacks = dict.fromkeys(range(1, len(line) // 4 + 2))
                if not line:
                    reading_stacks = False
                    continue
                if reading_stacks:
                    if '[' not in line:  # last line of stacks with only stack number
                        continue
                    self._parse_stack_line(line)
                else:
                    re_match = re.match("move (\d+) from (\d+) to (\d+)", line)
                    self.moves.append([int(g) for g in re_match.groups()])
        self.initial_stacks = copy.deepcopy(self.stacks)

    def _reset(self):
        self.stacks = copy.deepcopy(self.initial_stacks)

    def _parse_stack_line(self, line):
        for i in range(1, len(line), 4):
            value = line[i]
            if value in string.ascii_uppercase:
                stack_number = i // 4 + 1
                stack = self.stacks.get(stack_number) or []
                self.stacks[stack_number] = [*[value], *stack]

    def _apply_move(self, nb_items, from_stack_nb, to_stack_nb, craft_mover_9001=False):
        from_stack = self.stacks.get(from_stack_nb)
        chunk = [from_stack.pop() for i in range(nb_items)]
        if craft_mover_9001:
            chunk = reversed(chunk)
        self.stacks[to_stack_nb] = [*(self.stacks[to_stack_nb] or []), *chunk]

    def _apply_all_moves(self, craft_mover_9001=False):
        for move in self.moves:
            self._apply_move(*move, craft_mover_9001=craft_mover_9001)

    def _get_result(self):
        values = []
        for stack in self.stacks.values():
            if stack:
                values.append(stack[len(stack) - 1])
        return ''.join(values)
                
    def question1(self):
        self._apply_all_moves()
        return self._get_result()

    def question2(self):
        self._apply_all_moves(craft_mover_9001=True)
        return self._get_result()

aoc = AoC5()
print(aoc.question1())
aoc._reset()
print(aoc.question2())
