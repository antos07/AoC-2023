import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


@dataclass
class NumberPosition:
    line: int
    start: int
    end: int

    def adjacent_coords(self) -> Iterable[tuple[int, int]]:
        coords = []
        if self.start > 0:
            y_range_start = self.start - 1
            coords.append((self.line, self.start - 1))
        else:
            y_range_start = self.start

        # Ignore the upper bounds because accessing those cells
        # will raise an exception anyway.
        coords.append((self.line, self.end))
        if self.line > 0:
            coords += [
                (self.line - 1, y) for y in range(y_range_start, self.end + 1)
            ]
        coords += [
            (self.line + 1, y) for y in range(y_range_start, self.end + 1)
        ]

        return coords

    def get_number(self, engine_plan: list[str]) -> int:
        return int(engine_plan[self.line][self.start: self.end])


def find_number_positions(engine_plan: list[str]) -> Iterable[NumberPosition]:
    for i, line in enumerate(engine_plan):
        start_pos = None

        for j, c in enumerate(line):
            if c.isdigit() and start_pos is None:
                # The start of a number
                start_pos = j
            elif not c.isdigit() and start_pos is not None:
                # The end of a number
                yield NumberPosition(i, start_pos, j)
                start_pos = None

        if start_pos:
            yield NumberPosition(i, start_pos, len(line))


def filter_part_positions(
        engine_plan: list[str],
        number_positions: Iterable[NumberPosition]
) -> Iterable[NumberPosition]:
    for position in number_positions:
        for x, y in position.adjacent_coords():
            try:
                symbol = engine_plan[x][y]
            except IndexError:
                continue
            if symbol != '.' and not symbol.isdigit():
                yield position
                break


def find_gear_ratios(
        engine_plan: list[str],
        part_positions: Iterable[NumberPosition]
) -> Iterable[int]:
    gear_stats = defaultdict(lambda: (0, 1))
    for position in part_positions:
        for x, y in position.adjacent_coords():
            try:
                symbol = engine_plan[x][y]
            except IndexError:
                continue
            if symbol == '*':
                cnt, ratio = gear_stats[x, y]
                gear_stats[x, y] = (
                    cnt + 1, ratio * position.get_number(engine_plan)
                )
    for cnt, ratio in gear_stats.values():
        if cnt == 2:
            yield ratio


def main():
    engine_plan = read_input()
    number_positions = find_number_positions(engine_plan)
    part_postions = filter_part_positions(engine_plan, number_positions)

    answer = sum(find_gear_ratios(engine_plan, part_postions))
    print(answer)


if __name__ == '__main__':
    main()
