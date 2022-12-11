DOWN = 'D'
UP = 'U'
LEFT = 'L'
RIGHT = 'R'

class AoC9:

    def __init__(self) -> None:
        self.head = (0, 0)
        for i in range(1, 10, 1):
            setattr(self, f'tail_{i}', (0, 0))
            setattr(self, f'positions_passed_tail_{i}', ['0;0'])
        with open('input.txt') as f:
            for line in f.readlines():
                direction, nb_moves = line.replace('\n', '').split(' ')
                nb_moves = int(nb_moves)
                for _ in range(nb_moves):
                    self._move('head', direction)
                    self._move_tails()

    def _move(self, element_to_move, directions):
        x, y = getattr(self, element_to_move)
        if RIGHT in directions:
            x += 1
        if LEFT in directions:
            x -= 1
        if UP in directions:
            y += 1
        if DOWN in directions:
            y -= 1
        setattr(self, element_to_move, (x, y))

    def _move_tails(self):
        chain = ['head', *[f'tail_{i}' for i in range(1, 10, 1)]]
        groups = [chain[i:i + 2] for i in range(0, len(chain), 1)][:-1]
        for group in groups:
            self._move_tail(*group)
    
    def _move_tail(self, head, tail):
        x_head, y_head = getattr(self, head)
        x_tail, y_tail = getattr(self, tail)
        directions = ''
        # Same X
        if x_tail == x_head:
            if abs(y_head - y_tail) > 1:
                if y_head > y_tail:
                    directions = UP
                else:
                    directions = DOWN
        # Same Y
        elif y_tail == y_head:
            if abs(x_head - x_tail) > 1:
                if x_head > x_tail:
                    directions = RIGHT
                else:
                    directions = LEFT
        # Diagonal move
        elif abs(x_head - x_tail) > 1 or abs(y_head - y_tail) > 1:
            if x_head > x_tail:
                directions = RIGHT
            else:
                directions = LEFT
            if y_head > y_tail:
                directions += UP
            else:
                directions += DOWN
        if directions:
            self._move(tail, directions=directions)
            positions_attr = f'positions_passed_{ tail }'
            positions = getattr(self, positions_attr)
            positions.append(';'.join(str(value) for value in getattr(self, tail)))
            setattr(self, positions_attr, positions)

     
    def question1(self):
        return len(set(getattr(self, 'positions_passed_tail_1')))

    def question2(self):
        return len(set(getattr(self, 'positions_passed_tail_9')))
                

aoc = AoC9()
print(aoc.question1())
print(aoc.question2())
