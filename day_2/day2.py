class AoC2:

    LOOSE = 0
    DRAW = 3
    WIN = 6
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    PLAYS_RULE_1 = {
        'X': {
            'score': ROCK,
            'against': {
                'A': DRAW,
                'B': LOOSE,
                'C': WIN
            }
        },
        'Y': {
            'score': PAPER,
            'against': {
                'A': WIN,
                'B': DRAW,
                'C': LOOSE
            }
        },
        'Z': {
            'score': SCISSOR,
            'against': {
                'A': LOOSE,
                'B': WIN,
                'C': DRAW
            }
        }
    }

    PLAYS_RULE_2 = {
        'X': {
            'score': LOOSE,
            'against': {
                'A': SCISSOR,
                'B': ROCK,
                'C': PAPER
            }
        },
        'Y': {
            'score': DRAW,
            'against': {
                'A': ROCK,
                'B': PAPER,
                'C': SCISSOR
            }
        },
        'Z': {
            'score': WIN,
            'against': {
                'A': PAPER,
                'B': SCISSOR,
                'C': ROCK
            }
        }
    }

    def __init__(self) -> None:
        with open('input.txt') as f:
            self.rounds = [line.replace('\n', '') for line in f.readlines()]
            
    def _compute_round(self, play_round, rules):
        elf_value, my_value = play_round.split(' ')
        play_result = rules.get(my_value)
        return play_result.get('score') + play_result.get('against').get(elf_value)

    def question1(self):
        return sum([self._compute_round(round, AoC2.PLAYS_RULE_1) for round in self.rounds])

    def question2(self):
        return sum([self._compute_round(round, AoC2.PLAYS_RULE_2) for round in self.rounds])


aoc = AoC2()
print(aoc.question1())
print(aoc.question2())
