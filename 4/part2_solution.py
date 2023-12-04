import heapq
import sys


def get_card_score(card_data: str) -> int:
    winning_numbers, actual_numbers = card_data.split(' | ')
    winning_numbers = {int(n) for n in winning_numbers.split()}
    actual_numbers = (int(n) for n in actual_numbers.split())

    return sum(1 for n in actual_numbers if n in winning_numbers)


def main():
    answer = 0  # The total number of cards

    # The idea is to store the number of copied cards as multiplier.
    # It can be increased each time we process a new card by
    # the score of the card and decreased when we processed the last
    # copied card for some card (stored as added_card_barriers).
    multiplier = 1
    added_card_barriers: list[tuple[int, int]] = []
    for card_id, line in enumerate(sys.stdin, start=1):
        card_name, card_data = line.rstrip().split(':')

        answer += multiplier

        score = get_card_score(card_data)
        if score:
            heapq.heappush(added_card_barriers, (card_id + score, multiplier))
            multiplier += multiplier

        # Decrease multiplier by the number copies that end now.
        while added_card_barriers and added_card_barriers[0][0] == card_id:
            multiplier -= added_card_barriers[0][1]
            heapq.heappop(added_card_barriers)

    print(answer)


if __name__ == '__main__':
    main()
