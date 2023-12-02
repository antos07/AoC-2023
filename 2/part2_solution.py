import sys
from dataclasses import dataclass


@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_string(cls, s: str) -> 'CubeSet':
        kwargs = {
            split.split()[1]: int(split.split()[0])
            for split in s.split(', ')
        }
        return cls(**kwargs)


def get_min_cube_set(game_data: str) -> CubeSet:
    min_cube_set = CubeSet()
    for cube_subset in game_data.split(';'):
        cube_subset = CubeSet.from_string(cube_subset)
        if cube_subset.red > min_cube_set.red:
            min_cube_set.red = cube_subset.red
        if cube_subset.green > min_cube_set.green:
            min_cube_set.green = cube_subset.green
        if cube_subset.blue > min_cube_set.blue:
            min_cube_set.blue = cube_subset.blue
    return min_cube_set


def main():
    answer = 0  # The sum of ids of all impossible games

    # Process input line by line until EOF.
    for line in sys.stdin:
        game_name, game_data = line.split(':')
        min_cube_set = get_min_cube_set(game_data)
        answer += min_cube_set.red * min_cube_set.green * min_cube_set.blue

    print(answer)


if __name__ == '__main__':
    main()
