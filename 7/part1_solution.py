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


@total_ordering
class Hand:
    CARDS = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

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

        if len(card_counter) == 1:
            return HandType.FIVE_OF_ANY_KIND
        if len(card_counter) == 5:
            return HandType.HIGH_CARD
        if len(card_counter) == 4:
            return HandType.ONE_PAIR
        if len(card_counter) == 3:
            if card_counter.most_common()[0][1] == 3:
                return HandType.THREE_OF_ANY_KIND
            return HandType.TWO_PAIRS

        if card_counter.most_common()[0][1] == 4:
            return HandType.FOUR_OF_ANY_KIND
        return HandType.FULL_HOUSE


def main():
    bids = [
        (Hand(line.split()[0]), int(line.split()[1]))
        for line in sys.stdin
    ]
    bids.sort()

    answer = sum(bid * i for i, (hand, bid) in enumerate(bids, start=1))
    print(answer)


if __name__ == '__main__':
    main()
