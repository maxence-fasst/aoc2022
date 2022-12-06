class AoC6:

    def __init__(self) -> None:
        with open('input.txt') as f:
            self.input = f.read().replace('\n', '')

    def _get_packet_position(self, packet_length):
        for i in range(len(self.input) - packet_length + 1):
            values = set(self.input[i: i + packet_length])
            if len(values) == packet_length:
                return i + packet_length
            
    def question1(self):
        return self._get_packet_position(packet_length=4)

    def question2(self):
        return self._get_packet_position(packet_length=14)

aoc = AoC6()
print(aoc.question1())
print(aoc.question2())
