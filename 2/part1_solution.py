# I know it's ugly...

import sys
from dataclasses import dataclass


def get_game_id(game_name: str) -> int:
    # Convert 'Game X' to X
    return int(game_name.removeprefix('Game '))


@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other):
        try:
            return (self.red <= other.red
                    and self.green <= other.green
                    and self.blue <= other.blue)
        except AttributeError:
            return NotImplemented

    @classmethod
    def from_string(cls, s: str) -> 'CubeSet':
        kwargs = {
            split.split()[1]: int(split.split()[0])
            for split in s.split(', ')
        }
        return cls(**kwargs)


MAX_CUBE_SET = CubeSet(12, 13, 14)


def is_game_data_valid(game_data: str) -> bool:
    for cube_subset in game_data.split(';'):
        if not CubeSet.from_string(cube_subset) <= MAX_CUBE_SET:
            return False
    return True


def main():
    answer = 0  # The sum of ids of all impossible games

    # Process input line by line until EOF.
    for line in sys.stdin:
        game_name, game_data = line.split(':')
        if is_game_data_valid(game_data):
            answer += get_game_id(game_name)

    print(answer)


if __name__ == '__main__':
    main()
