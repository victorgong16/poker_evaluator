"""Card and Hand objects to represent poker card and 5-card poker hands respectively"""

from collections import Counter as counter

cards = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
         "8" : 8, "9" : 9, "0" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14,}

suits = {"D" : "Diamonds", "C" : "Clubs", "H" : "Hearts", "S" : "Spades"}

class card():
    """Card object with the card number/value and card suit"""

    def __init__(self, card):
        if type(card) is not str:
            raise TypeError("Parameter must be of type string")
        if card[0] not in cards or card[1] not in suits or len(card) != 2:
            raise ValueError
        self.card = cards[card[0]]
        self.suit = suits[card[1]]

    def __str__(self):
        return str(self.card) + " of " + self.suit

class hand():
    """Hand object with a list of five card objects"""
 
    def __init__(self, cards):
        if type(cards) is not list:
            raise TypeError("Parameter must be a list of 5 card objects")
        if not all(isinstance(x, card) for x in cards) or len(cards) != 5:
            raise ValueError
        self.cards = cards
        self.ranking()

    def check_straight(self):
        """Store the cards in the hand in sorted order by value"""
        return sorted([c.card for c in self.cards])

    def card_numbers(self):
        """Store the cards in the hand without sorting by value"""
        return [c.card for c in self.cards]

    def card_suits(self):
        """Store the cards in the hand without sorting by suits"""
        return [c.suit for c in self.cards]

    def ranking(self):
        """Determine the poker hand ranking and sets the hand's ranking from 1 to 10"""

        sorted_card_numbers = self.check_straight() #Sorted card numbers
        card_numbers = self.card_numbers() #Card numbers
        card_suits = self.card_suits()  #Card suits

        if len(counter(card_suits)) == 1:
            if (sorted_card_numbers == [10, 11, 12, 13, 14]):
                self.rank = 1 #Royal Flush
                self.high_card = 14
                self.kicker = [14]
            elif set(sorted_card_numbers) == set(range(sorted_card_numbers[0], sorted_card_numbers[0] + 5)):
                self.rank = 2 #Straight Flush
                self.high_card = sorted_card_numbers[4]
                self.kicker = [sorted_card_numbers[4]]
            else:
                self.rank = 5 #Flush
                self.high_card = sorted_card_numbers[4]
                self.kicker = sorted_card_numbers[:4][::-1]
        elif len(counter(card_numbers).keys()) == 2:
            if counter(card_numbers).most_common(1)[0][1] == 4:
                self.rank = 3 #4 of a kind
                self.high_card = counter(card_numbers).most_common(1)[0][0]
                self.kicker = [counter(card_numbers).most_common(2)[1][0]]
            else:
                self.rank = 4 #full house
                self.high_card = counter(card_numbers).most_common(1)[0][0]
                self.kicker = [counter(card_numbers).most_common(2)[1][0]]
        elif set(sorted_card_numbers) == set(range(sorted_card_numbers[0], sorted_card_numbers[0] + 5)):
            self.rank = 6 #Straight
            self.high_card = sorted_card_numbers[4]
            self.kicker = [sorted_card_numbers[4]]
        elif len(counter(card_numbers).keys()) == 3:
            if counter(card_numbers).most_common(1)[0][1] == 3:
                if 2 not in counter(card_numbers).values():
                    kickers = counter(card_numbers).most_common(3)
                    self.rank = 7 #3 of a kind
                    self.high_card = counter(card_numbers).most_common(1)[0][0]
                    self.kicker = [max(kickers[1][0], kickers[2][0])]
                    self.kicker.append(min(kickers[1][0], kickers[2][0]))
            else:
                kickers = counter(card_numbers).most_common(3)
                self.rank = 8 #2 pair
                self.high_card1 = max(kickers[0][0], kickers[1][0])
                self.high_card2 = min(kickers[0][0], kickers[1][0])
                self.kicker = [counter(card_numbers).most_common(3)[2][0]]

        elif len(counter(card_numbers).keys()) == 4:
            self.rank = 9 #1 pair
            self.high_card = counter(card_numbers).most_common(1)[0][0]
            self.kicker = sorted([counter(card_numbers).most_common(4)[1][0],
                                  counter(card_numbers).most_common(4)[2][0],
                                  counter(card_numbers).most_common(4)[3][0]])
        else:
            self.rank = 10
            self.high_card = sorted_card_numbers[4]
            self.kicker = sorted_card_numbers[:4][::-1]
