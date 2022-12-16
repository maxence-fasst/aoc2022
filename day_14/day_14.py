class AoC14:

    def __init__(self) -> None:
        self.area = {}
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                self._build_walls(*line.split(' -> '))
        self.max_y = max(y for x, y in self.area.keys())
        self.infinite_wall_y = self.max_y + 2
        self.initial_area = self.area.copy()
                
    def _build_walls(self, *coords):
        coords = list(coords)
        while len(coords) > 1:
            start, end = coords.pop(0), coords[0]
            x_start, y_start = [int(pos) for pos in start.split(',')]
            x_end, y_end = [int(pos) for pos in end.split(',')]
            if x_start == x_end:
                mov_x = 0
                mov_y = 1 if y_start < y_end else -1
            else:
                mov_y = 0
                mov_x = 1 if x_start < x_end else -1
            self.area[(x_start, y_start)] = '#'
            while (x_start, y_start) != (x_end, y_end):
                x_start += mov_x
                y_start += mov_y
                self.area[(x_start, y_start)] = '#'

    def _drop_sand(self, use_infinite_wall=False):
        x_start, y_start = 500, 0
        max_y_to_reach = self.infinite_wall_y if use_infinite_wall else self.max_y
        while y_start < max_y_to_reach:
            if use_infinite_wall and y_start == self.infinite_wall_y - 1:
                self.area[(x_start, y_start + 1)] = '#'
                self.area[(x_start - 1, y_start + 1)] = '#'
                self.area[(x_start + 1, y_start + 1)] = '#'
            if (x_start, y_start + 1) not in self.area:
                y_start += 1
            elif (x_start - 1, y_start + 1) not in self.area:
                x_start -= 1
                y_start += 1
            elif (x_start + 1, y_start + 1) not in self.area:
                x_start += 1
                y_start += 1
            else:
                if use_infinite_wall and (x_start, y_start) == (500, 0):
                    return False
                self.area[(x_start, y_start)] = 'o'
                return True
        return False
      
    def question1(self):
        result = 0
        while _ := self._drop_sand():
            result += 1
        return result

    def question2(self):
        self.area = self.initial_area.copy()
        result = 0
        while _ := self._drop_sand(use_infinite_wall=True):
            result += 1
        return result + 1 
                

aoc = AoC14()

print(aoc.question1())
print(aoc.question2())
