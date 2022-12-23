from collections import deque

class AoC20:

    def __init__(self) -> None:
        with open('input.txt') as f:
            self.initial_list = [int(line.replace('\n', '')) for line in f.readlines()]
            self.initial_index_0 = self.initial_list.index(0)
            self.initial_list = [(i, item) for i, item in enumerate (self.initial_list)]

    def _mix(self, initial, nb_mixes=1):
        queue = deque(initial)
        for _ in range(nb_mixes):
            for index, item in initial:
                if item == 0:
                    continue
                queue_index = queue.index((index, item))
                queue.rotate(-queue_index)
                queue.popleft()
                queue.rotate(-item)
                queue.appendleft((index, item))
        return queue
            
    def question1(self):
        queue = self._mix(self.initial_list)
        result = 0
        index_0 = queue.index((self.initial_index_0, 0))
        for check in (1000, 2000, 3000, ):
            result += queue[(index_0 + check) % len(self.initial_list)][1]
        return result

    def question2(self):
        new_list = [(i, item * 811_589_153) for i, item in self.initial_list]
        queue = self._mix(new_list, nb_mixes=10)
        result = 0
        index_0 = queue.index((self.initial_index_0, 0))
        for check in (1000, 2000, 3000, ):
            result += queue[(index_0 + check) % len(self.initial_list)][1]
        return result

aoc = AoC20()

print(aoc.question1())
print(aoc.question2())
