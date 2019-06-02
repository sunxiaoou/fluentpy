import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    # Card(rank='7', suit='diamonds')
    deck = FrenchDeck()
    print(len(deck))
    # 52

    print(deck[:3])
    # [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

    print(deck[12::13])
    # [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

    print(Card('Q', 'hearts') in deck)
    # True
    print(Card('Z', 'clubs') in deck)
    # False

    print()
    for card in deck:  # doctest: +ELLIPSIS
        print(card)
    # Card(rank='2', suit='spades')
    # Card(rank='3', suit='spades')
    # Card(rank='4', suit='spades')

    print()
    for card in reversed(deck):  # doctest: +ELLIPSIS
        print(card)
    # Card(rank='A', suit='hearts')
    # Card(rank='K', suit='hearts')
    # Card(rank='Q', suit='hearts')

    print()
    for n, card in enumerate(deck, 1):  # doctest: +ELLIPSIS
        print(n, card)
    # 1 Card(rank='2', suit='spades')
    # 2 Card(rank='3', suit='spades')
    # 3 Card(rank='4', suit='spades')

    print()
    # Rank test:
    print(spades_high(Card('2', 'clubs')))
    # 0
    print(spades_high(Card('A', 'spades')))
    # 51

    print()
    for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
        print(card)
    # Card(rank='2', suit='clubs')
    # Card(rank='2', suit='diamonds')
    # Card(rank='2', suit='hearts')
    # ...
    # Card(rank='A', suit='diamonds')
    # Card(rank='A', suit='hearts')
    # Card(rank='A', suit='spades')


if __name__ == "__main__":
    main()
