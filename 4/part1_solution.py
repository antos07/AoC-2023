import sys


def get_card_score(card_data: str) -> int:
    winning_numbers, actual_numbers = card_data.split(' | ')
    winning_numbers = {int(n) for n in winning_numbers.split()}
    actual_numbers = [int(n) for n in actual_numbers.split()]

    score = 0
    for n in actual_numbers:
        if n not in winning_numbers:
            continue

        if score == 0:
            score = 1
        else:
            score *= 2

    return score


def main():
    answer = 0  # The sum of scores

    for line in sys.stdin:
        card_name, data = line.rstrip().split(':')
        answer += get_card_score(data)

    print(answer)


if __name__ == '__main__':
    main()
