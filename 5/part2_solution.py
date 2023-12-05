import operator
import sys
from typing import Iterable


def read_seed_ranges():
    values = [int(v) for v in input().removeprefix('seeds: ').split()]
    return [
        (start, start + length)
        for start, length in zip(values[::2], values[1::2])
    ]


def read_maps() -> Iterable[list[tuple[int, int, int]]]:
    mappings: list[tuple[int, int, int]] = []
    for line in sys.stdin:
        line = line.rstrip()
        if not line or 'map' in line:
            if mappings:
                yield mappings.copy()
                mappings.clear()
            continue

        mappings.append(tuple(int(n) for n in line.split()))  # noqa
    if mappings:
        yield mappings


def main():
    seed_ranges = read_seed_ranges()

    for mapping in read_maps():
        seed_ranges.sort()
        mapping.sort(key=operator.itemgetter(1))
        # Append unreachable mapping range
        mapping.append((10 ** 20, 10 ** 20, 1))

        mapping_iterator = iter(mapping)
        dest_start, source_start, length = next(mapping_iterator)
        new_seed_ranges = []
        for seed_start, seed_end in seed_ranges:
            while seed_start <= seed_end:
                # Move to the first range that is not to the left
                # of the seed range
                while source_start + length <= seed_start:
                    dest_start, source_start, length = next(mapping_iterator)

                if seed_start < source_start:
                    new_seed_start = min(seed_end + 1, source_start)
                    new_seed_ranges.append((seed_start, new_seed_start - 1))
                    seed_start = new_seed_start
                    continue

                new_seed_start = min(seed_end + 1, source_start + length)
                new_seed_ranges.append((
                    dest_start + seed_start - source_start,
                    dest_start + new_seed_start - source_start - 1
                ))
                seed_start = new_seed_start

        seed_ranges = new_seed_ranges

    print(min(seed_ranges)[0])


if __name__ == '__main__':
    main()
