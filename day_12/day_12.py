import networkx
import string

class AoC12:
    START, END = 'S', 'E'
    HEIGHTS = {
        START: 0,
        **{letter: index for index, letter in enumerate(string.ascii_lowercase)},
        END: 25
    }

    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.graph = networkx.DiGraph()
        with open('input.txt') as f:
            for y, line in enumerate(f.readlines()):
                line = line.replace('\n', '')
                for x, value in enumerate(line):
                    self.graph.add_node((x, y), height=AoC12.HEIGHTS.get(value), start=value == AoC12.START, end=value == AoC12.END)
        for node, node_data in self.graph.nodes(data=True):
            if node_data.get('end', False):
                self.end = node
                continue      
            if not self.start and node_data.get('start', False):
                self.start = node
            x, y = node
            self._add_edge(node, node_data, (x + 1, y))
            self._add_edge(node, node_data, (x - 1, y))
            self._add_edge(node, node_data, (x, y + 1))
            self._add_edge(node, node_data, (x, y - 1))
        self.shortest_paths = networkx.shortest_path_length(self.graph, target=self.end)

    def _add_edge(self, node, node_data, next_coords):
        try:
            next_node = self.graph.nodes[next_coords]
        except KeyError:
            return
        if next_node and next_node.get('height') in range(node_data.get('height') + 2):
            self.graph.add_edge(node, next_coords)

    def question1(self):
        return self.shortest_paths[self.start]

    def question2(self):
        sources = [node for node in self.shortest_paths if self.graph.nodes[node].get('height') == AoC12.HEIGHTS.get(AoC12.START)]
        return min(self.shortest_paths[start_point] for start_point in sources)
                

aoc = AoC12()

print(aoc.question1())
print(aoc.question2())
