import functools
import json

class AoC13:
    
    def __init__(self) -> None:
        self.pairs = []
        actual = []
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if not line:
                    self.pairs.append(actual)
                    actual = []
                    continue
                actual.append(json.loads(line))
            self.pairs.append(actual)      

    def _is_in_right_order(self, left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                # If left equals right, continue checking
                return None
            return left < right
        elif isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]
        if not left or not right:
            len_left, len_right = len(left), len(right)
            if len_left == len_right:
                # If left equals right, continue checking
                return None
            return len_left < len_right
        left_element, *next_left = left
        right_element, *next_right = right
        result = self._is_in_right_order(left_element, right_element)
        if result is not None:
            return result
        return self._is_in_right_order(next_left, next_right)


    def question1(self):
        return sum(index for index, pair in enumerate(self.pairs, start=1) if self._is_in_right_order(*pair))

    def question2(self):
        first_elem = [[2]]
        second_elem = [[6]]
        all_packets = [first_elem, second_elem]
        for pair in self.pairs:
            all_packets.extend(pair)
        all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: -self._is_in_right_order(a, b)))
        return (all_packets.index(first_elem) + 1) * (all_packets.index(second_elem) + 1)
           

aoc = AoC13()

print(aoc.question1())
print(aoc.question2())
