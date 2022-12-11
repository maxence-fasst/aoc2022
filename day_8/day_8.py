class AoC8:

    def __init__(self) -> None:
        with open('input.txt') as f:
            self.lines = [line.replace('\n', '') for line in f.readlines()]
            self.columns = list(map(list, zip(*self.lines)))

    def _is_visible(self, tree_position, size):
        line_index, column_index = tree_position
        line = self.lines[line_index]
        # left
        left_trees = line[0:column_index]
        if all(tree < size for tree in left_trees):
            return True
        # Right
        rigt_trees = line[column_index + 1:]
        if all(tree < size for tree in rigt_trees):
            return True
        
        column = self.columns[column_index]
        # Top
        top_trees = column[0:line_index]
        if all(tree < size for tree in top_trees):
            return True
        # Bottom
        bottom_trees = column[line_index + 1:]
        if all(tree < size for tree in bottom_trees):
            return True
        return False

    def _get_visibility(self, tree_position, size):
        line_index, column_index = tree_position
        line = self.lines[line_index]
        # left
        left_trees = line[0:column_index]
        nb_left = 0
        for left_tree in reversed(left_trees):
            nb_left += 1
            if left_tree >= size:
                break         
        # Right
        right_trees = line[column_index + 1:]
        nb_right = 0
        for right_tree in right_trees:
            nb_right += 1
            if right_tree >= size:
                break

        column = self.columns[column_index]
        # Top
        top_trees = column[0:line_index]
        nb_top = 0
        for top_tree in reversed(top_trees):
            nb_top += 1
            if top_tree >= size:
                break  
        # Bottom
        bottom_trees = column[line_index + 1:]
        nb_bottom = 0
        for bottom_tree in bottom_trees:
            nb_bottom += 1
            if bottom_tree >= size:
                break

        return nb_left * nb_right * nb_top * nb_bottom
     
    def question1(self):
        nb_visible_trees = 0
        for line_index, line in enumerate(self.lines):
            for column_index, tree_size in enumerate(line):
                if self._is_visible((line_index, column_index), size=tree_size):
                    nb_visible_trees += 1
        return nb_visible_trees

    def question2(self):
        max_visibility = 0
        for line_index, line in enumerate(self.lines):
            if line_index in [0, len(self.lines) - 1]:
                continue
            for column_index, tree_size in enumerate(line):
                if column_index in [0, len(line) - 1]:
                    continue
                visibility = self._get_visibility((line_index, column_index), size=tree_size)
                if visibility > max_visibility:
                    max_visibility = visibility
        return max_visibility
                

aoc = AoC8()
print(aoc.question1())
print(aoc.question2())
