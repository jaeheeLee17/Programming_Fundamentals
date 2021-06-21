import random

class Card:
    """defines Card class"""
    __suits = ("Diamond", "Heart", "Spade", "Clover")
    __ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, rank, face_up=True):
        """
        initalizes a playing card object arguments:
        suit -- must be in Card.__suits
        rank -- must be in Card.__ranks
        face_up -- True or False (default True)
        """
        if suit in Card.__suits and rank in Card.__ranks:
            self.__suit = suit
            self.__rank = rank
            self.__face_up = face_up
        else:
            print("Error: Not a valid card")
        self.__value = Card.__ranks.index(self.__rank) + 1
        if self.__value > 10:
            self.__value = 10

    def __str__(self):
        """returns its string representation"""
        if self.__face_up:
            return self.__suit + "." + self.__rank
        else:
            return "XXX"

    @property
    def suit(self):
        """returns its suit value"""
        return self.__suit

    @property
    def rank(self):
        """returns its rank value"""
        return self.__rank

    @property
    def face_up(self):
        """returns its face_up value"""
        return self.__face_up

    @property
    def value(self):
        """returns its face value (according to blackjack rule)"""
        return self.__value

    def flip(self):
        """flips itself"""
        self.__face_up = not self.__face_up

    @staticmethod
    def fresh_deck():
        """
        returns a brand-new deck of shuffled cards
        with all face down
        """
        cards = []
        for s in Card.__suits:
            for r in Card.__ranks:
                cards.append(Card(s, r, False))
        random.shuffle(cards)
        return cards

class Deck:
    """defines Deck class"""
    def __init__(self):
        """creates a deck object consisting of 52 cards shuffled"""
        self.__deck = Card.fresh_deck()
        print("<< A brand-new deck of card! >>")

    def next(self, open=True):
        """
        removes a card from deck and returns the card
        with its face up if open == True, or
        with its face down if open == False
        """
        if self.__deck == []:
            self.__deck = Card.fresh_deck()
            print("<< A brand-new deck of card! >>")
        card = self.__deck.pop()
        if open:
            card.flip()
        return card

class Hand:
    """defines Hand class"""
    def __init__(self, name="Smavi"):
        """
        creates player/dealer's empty hand
        argument:
        name -- player's name in string (default: 'Dealer')
        """
        self.__name = name
        self.__hand = []

    @property
    def name(self):
        """its name: either player's name or 'Dealer'"""
        return self.__name

    @property
    def hand(self):
        return self.__hand

    @property
    def total(self):
        """the total value of its hand"""
        point = 0
        number_of_ace = 0
        for card in self.__hand:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += card.value
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point

    def get(self, card):
        """gets a card from deck and puts the card into its hand"""
        self.__hand.append(card)

    def clear(self):
        """empties its hand"""
        self.__hand = []

    def open(self):
        """turns all of its hand's cards' faces up"""
        for card in self.__hand:
            if not card.face_up:
                card.flip()

class PlayerHand(Hand):
    """
    defines PlayerHand class. This class inherits Hand class.
    """
    def __init__(self, name):
        """
        creates player's empty hand with the capability
        of counting chips it owns argument:
        name -- player's name in string
        """
        super().__init__(name)
        self.__chips = 0

    def earn_chips(self, n):
        """increases the number of chips by n"""
        self.__chips += n
        print("You have", self.__chips, "chips.")

    def lose_chips(self, n):
        """decreases the number of chips by n"""
        self.__chips -= n
        print("You have", self.__chips, "chips.")

class Reader:
    """defines Reader class"""
    @staticmethod
    def register():
        """gets player's name and returns it (string)"""
        return input("Enter your name: ")

    def ox(message):
        """
        returns True if player inputs 'o' or 'O',
        False if player inputs 'x' or 'X'
        """
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'

class BlackjackController:
    """defines BlackjackController class"""
    def __init__(self, name):
        """
        creates player/dealer's empty hand and
        a deck of cards argument:
        name -- player's name in string (default: 'Dealer')
        """
        self.__player = PlayerHand(name)
        self.__dealer = Hand()
        self.__deck = Deck()

    def play(self):
        """plays a round of blackjack game"""
        print("== new game ==")
        player = self.__player
        dealer = self.__dealer
        deck = self.__deck
        player.get(deck.next())
        dealer.get(deck.next())
        player.get(deck.next())
        dealer.get(deck.next(open=False))
        print(dealer.name, ":", end=' ')
        for dealercard in dealer.hand:
            print(dealercard, end=' ')
        print()
        print(player.name, ":", end=' ')
        for playercard in player.hand:
            print(playercard, end=' ')
        print()
        if player.total == 21:
            print("Blackjack!", player.name, "wins.")
            player.earn_chips(2)
        else:
            while player.total < 21 and Reader.ox(player.name + ": Hit? (o/x) "):
                player.get(deck.next())
                print(player.name, ":", end=' ')
                for playercard in player.hand:
                    print(playercard, end=' ')
                print()
            if player.total > 21:
                print(player.name, "busts!")
                player.lose_chips(1)
            else:
                while dealer.total <= 16:
                    dealer.get(deck.next())
                if dealer.total > 21:
                    print("Dealer busts!")
                    player.earn_chips(1)
                elif dealer.total == player.total:
                    print("We draw.")
                elif dealer.total > player.total:
                    print(player.name, "loses.")
                    player.lose_chips(1)
                else:
                    print(player.name, "wins.")
                    player.earn_chips(1)
            dealer.open()
            print(dealer.name, ":", end=' ')
            for dealercard in dealer.hand:
                print(dealercard, end=' ')
            print()
        player.clear()
        dealer.clear()

def main():
    print("Welcome to SMaSH Casino!")
    name = Reader.register()
    game = BlackjackController(name)
    while True:
        game.play()
        if not Reader.ox("Play more, " + name + "? (o/x) "):
            break
    print("Bye, " + name + "!")

if __name__ == "__main__":
    main()
