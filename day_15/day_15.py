import re
from shapely.geometry import LineString, MultiPolygon, Polygon

class AoC15:

    def __init__(self) -> None:
        self.beacons = set()
        polygons = []
        self.min_x = 0
        self.max_x = 0
        with open('input.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                re_match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
                sx, sy, bx, by = [int(value) for value in re_match.groups()]
                self.beacons.add((bx, by))
                distance = abs(sx - bx) + abs(sy - by)
                dist_min_x = sx - distance
                if dist_min_x < self.min_x:
                    self.min_x = dist_min_x
                dist_max_x = sx + distance 
                if dist_max_x> self.max_x:
                    self.max_x = dist_max_x
                polygons.append(Polygon((
                    (dist_min_x, sy),
                    (sx, sy - distance),
                    (dist_max_x, sy),
                    (sx, sy + distance)
                ))) 
        self.area = MultiPolygon(polygons).buffer(0)
      
    def question1(self):
        line_to_check = 2_000_000
        line = LineString(((self.min_x, line_to_check), (self.max_x, line_to_check)))
        return int(self.area.intersection(line).length)

    def question2(self):
        limit = 4_000_000
        search_area = Polygon(((0, limit), (limit, 0), (limit, limit), (0, limit)))
        beacon = search_area.difference(self.area).centroid
        return int(beacon.x * limit + beacon.y)

aoc = AoC15()

print(aoc.question1())
print(aoc.question2())
