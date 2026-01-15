from game.deck import create_deck, Card, shuffle_deck
from palace import deal_palace_setup

# Palace game: two players only
if __name__ == "__main__":
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)
    for card in shuffled_deck:
        print(f"{card.value} of {card.suit}")
    
    game = deal_palace_setup(shuffled_deck)