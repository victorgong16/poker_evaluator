"""Evaluator for the hand object"""

from card_objects import *

def compare_hands(hand1, hand2):
    """Master function to compare two hands"""
    if hand1.rank < hand2.rank:
        return 1
    elif hand2.rank < hand1.rank:
        return 2
    else:
        if hand1.rank == 8: #2 pair tiebreaker
            if hand1.high_card1 > hand2.high_card1 or \
               (hand1.high_card1 == hand2.high_card1 and hand1.high_card2 > hand2.high_card2) or \
               compare_kickers(hand1, hand2, len(hand1.kicker)):
                return 1
            elif hand1.high_card1 < hand2.high_card1 or \
                 (hand1.high_card1 == hand2.high_card1 and hand1.high_card2 < hand2.high_card2) or \
                 compare_kickers(hand2, hand1, len(hand1.kicker)):
                return 2
            else:
                return 3
        else:
            return compare_hands_helper(hand1, hand2)

def compare_hands_helper(hand1, hand2):
    """Helper function to compare all hands except 2 pair ties"""
    if hand1.high_card > hand2.high_card:
        return 1
    elif hand1.high_card < hand2.high_card:
        return 2
    else:
        if compare_kickers(hand1, hand2, len(hand1.kicker)):
            return 1
        elif compare_kickers(hand2, hand1, len(hand1.kicker)):
            return 2
        else:
            return 3

def compare_kickers(hand1, hand2, kicker_number):
    """Helper function to compare kickers"""
    for i in range(kicker_number):
        if hand1.kicker[i] > hand2.kicker[i]:
            return True
    return False
