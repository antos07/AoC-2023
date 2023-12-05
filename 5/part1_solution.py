import bisect
import operator
import sys
from typing import Iterable


def read_seeds():
    return [int(seed) for seed in input().removeprefix('seeds: ').split()]


class RangeMapping:
    def __init__(self, range_mappings: Iterable[tuple[int, int, int]]):
        self.range_mappings = sorted(range_mappings,
                                     key=operator.itemgetter(1))

    def __getitem__(self, item: int):
        pos = bisect.bisect(self.range_mappings, item,
                            key=operator.itemgetter(1)) - 1
        if pos < 0:
            # No range found
            return item

        dist_start, source_start, length = self.range_mappings[pos]
        if source_start <= item < source_start + length:
            # Item in range
            return dist_start + item - source_start

        return item


def read_maps() -> Iterable[RangeMapping]:
    mappings: list[tuple[int, int, int]] = []
    for line in sys.stdin:
        line = line.rstrip()
        if not line or 'map' in line:
            if mappings:
                yield RangeMapping(mappings)
                mappings.clear()
            continue

        mappings.append(tuple(int(n) for n in line.split()))  # noqa
    if mappings:
        yield RangeMapping(mappings)


def main():
    seeds = read_seeds()

    for mapping in read_maps():
        seeds = [mapping[seed] for seed in seeds]

    print(min(seeds))


if __name__ == '__main__':
    main()
