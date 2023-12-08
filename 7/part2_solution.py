import enum
import sys
from collections import Counter
from functools import total_ordering
from typing import Iterable


class HandType(enum.IntEnum):
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TWO_PAIRS = enum.auto()
    THREE_OF_ANY_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_ANY_KIND = enum.auto()
    FIVE_OF_ANY_KIND = enum.auto()


def most_common_no_jokers(card_counter: Counter) -> list[int]:
    return [number for card, number in card_counter.most_common() if not card == "J"]


@total_ordering
class Hand:
    CARDS = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

    def __init__(self, cards: Iterable[str]) -> None:
        self.cards = tuple(cards)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented

        return self.cards == other.cards

    def __lt__(self, other) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented

        if self.type != other.type:
            return self.type < other.type

        for own_card, other_card in zip(self.cards, other.cards):
            own_card_index = self.CARDS.index(own_card)
            other_card_index = self.CARDS.index(other_card)
            if own_card_index != other_card_index:
                return own_card_index > other_card_index
        return False

    @property
    def type(self) -> HandType:
        card_counter = Counter(self.cards)

        if (
            card_counter["J"] == 5
            or card_counter["J"] + most_common_no_jokers(card_counter)[0] == 5
        ):
            return HandType.FIVE_OF_ANY_KIND
        if card_counter["J"] + most_common_no_jokers(card_counter)[0] == 4:
            return HandType.FOUR_OF_ANY_KIND
        if card_counter["J"] + sum(most_common_no_jokers(card_counter)[:2]) == 5:
            return HandType.FULL_HOUSE
        if card_counter["J"] + most_common_no_jokers(card_counter)[0] == 3:
            return HandType.THREE_OF_ANY_KIND
        if card_counter["J"] + sum(most_common_no_jokers(card_counter)[:2]) == 4:
            return HandType.TWO_PAIRS
        if card_counter["J"] + most_common_no_jokers(card_counter)[0] == 2:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


def main():
    bids = [(Hand(line.split()[0]), int(line.split()[1])) for line in sys.stdin]
    bids.sort()

    answer = sum(bid * i for i, (hand, bid) in enumerate(bids, start=1))
    print(answer)


if __name__ == "__main__":
    main()
