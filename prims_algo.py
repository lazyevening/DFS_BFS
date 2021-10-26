from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def get_min_distance(self, dots: Set[Point]) -> (int, Point):
        assert self not in dots
        assert dots
        min_distant_point = dots.pop()
        min_distant = self._get_distance_to(min_distant_point)
        for point in dots:
            distant = self._get_distance_to(point)
            if distant < min_distant:
                min_distant = distant
                min_distant_point = point
        return min_distant_point, min_distant

    def _get_distance_to(self, point: Point) -> int:
        return abs(self.x - point.x) + abs(self.y - point.y)


def get_data(input_filename: str) -> (int, List[Point]):
    with open(input_filename) as file:
        lines = file.readlines()
        n = lines[0]
        dots = [Point(*map(int, x.split())) for x in lines[1:]]
    return n, dots

def write_data(components: List[List[int]], summary: int) -> None:
    components = components[1:]
    res: str = ''
    for line in components:
        for component in line:
            res += f'{component} '
        res += '0\n'
    res += str(summary)
    with open('out.txt', mode='w') as file:
        file.write(res)

def main(n: int, dots: List[Point]):
    summary = 0
    point_to_num_map = {}
    for point, num in zip(dots, range(1, len(dots) + 1)):
        point_to_num_map[point] = num
    components = [[] for _ in range(len(dots) + 1)]
    dots = set(dots)
    vertexes = set()
    vertexes.add(dots.pop())
    while dots:
        min_distance = float('inf')
        min_distance_point = None
        from_what = None
        for vertex in vertexes:
            min_point, distant = vertex.get_min_distance(dots.copy())
            if distant < min_distance:
                min_distance = distant
                min_distance_point = min_point
                from_what = vertex
        components[point_to_num_map[from_what]].append(point_to_num_map[min_distance_point])
        components[point_to_num_map[min_distance_point]].append(point_to_num_map[from_what])
        vertexes.add(min_distance_point)
        dots.remove(min_distance_point)
        summary += min_distance
    write_data(components, summary)


if __name__ == '__main__':
    input_file = 'in.txt'
    main(*get_data(input_file))
