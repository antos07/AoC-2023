import re
import sys

NAME_TO_DIGIT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_calibration_value(line: str) -> int:
    # Concatenation of the first and the last digit in
    # the line is needed.

    # Find all digits using regex with positive lookahead, which
    # also finds overlapping matches.
    regex = r'(?=(\d|' + '|'.join(NAME_TO_DIGIT) + '))'
    # And convert them into regular digits.
    all_digits = [
        NAME_TO_DIGIT.get(m.group(1), m.group(1))
        for m in re.finditer(regex, line)
    ]

    return int(all_digits[0] + all_digits[-1])


def main() -> None:
    answer = 0  # The sum of all calibration values

    # Process input.txt line by line while not EOF.
    for line in sys.stdin:
        answer += get_calibration_value(line)

    print(answer)


if __name__ == '__main__':
    main()
