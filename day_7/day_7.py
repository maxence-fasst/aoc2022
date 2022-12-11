class AoC7:

    def __init__(self) -> None:
        self.file_system = {'/': {}}
        self.current_path = []
        self.directories = set('/')
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if line == '$ ls':
                    continue
                elif line.startswith('$ cd'):
                    path = line.split(' ')[-1]
                    if path == '..':
                        self.current_path.pop()
                    else: 
                        self.current_path.append(path)
                else:
                    self._append_to_current_path(line)
        self.sizes_dir = { k: self._get_directory_size(k.split('.')) for k in self.directories }

    def _append_to_current_path(self, value):
        if value.startswith('dir'):
            key = value.split(' ')[-1]
            value = {}
            self.directories.add('.'.join(self.current_path + [key]))
        else:
            value, key = value.split(' ')
            value = int(value)
        self._get_recursive_value(self.file_system, self.current_path)[key] = value

    def _get_recursive_value(self, data, keys):
        if not keys:
            return data
        actual, *next = keys
        return self._get_recursive_value(data.get(actual), next)

    def _get_directory_size(self, path):
        directory = self._get_recursive_value(self.file_system, path)
        files_size = sum(v for k, v in directory.items() if isinstance(v, int))
        subdirectories = {k: v for k, v in directory.items() if isinstance(v, dict)}
        if not subdirectories:
            return files_size
        return files_size + sum(self._get_directory_size([*path, k]) for k in subdirectories.keys())
     
    def question1(self):
        return sum(v for v in self.sizes_dir.values() if v <= 100_000)

    def question2(self):
        max_size = 70_000_000
        root_size = self.sizes_dir.pop('/')
        unused = max_size - root_size
        needed_space = 30_000_000 - unused
        all_sizes = self.sizes_dir.values()
        return min(size for size in all_sizes if size >= needed_space)

aoc = AoC7()
print(aoc.question1())
print(aoc.question2())
