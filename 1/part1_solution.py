import sys


def get_calibration_value(line: str) -> int:
    # Concatenation of the first and the last digit in
    # the line is needed.
    all_digits = [c for c in line if c.isdigit()]
    return int(all_digits[0] + all_digits[-1])


def main() -> None:
    answer = 0  # The sum of all calibration values

    # Process input.txt line by line while not EOF.
    for line in sys.stdin:
        answer += get_calibration_value(line)

    print(answer)


if __name__ == '__main__':
    main()
