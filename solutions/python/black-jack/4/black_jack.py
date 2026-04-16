"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ["J", "Q" ,"K"]:
        return 10
    if card == "A":
        return 1
    if card == "2" :
        return 2
    if card == "3" :
        return 3
    if card == "4":
        return 4
    if card == "5":
        return 5
    if card == "6":
        return 6
    if card == "7":
        return 7
    if card == "8":
        return 8
    if card == "9":
        return 9
    if card == "10":
        return 10
        


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card_two == card_one :
        return (card_one,card_two)
        
    if card_one == "A" and (card_one != card_two and card_two != "1"):
        return card_two
    if card_two == "A" and (card_two != card_one and card_one != "1"):
        return card_one
    if card_one in ["K", "J", "Q", "10"] and card_two == "10":
        return (card_one,card_two)
    if card_two in ["K", "J", "Q", "10"] and card_one == "10":
        return (card_one,card_two)
    if card_one in ["K", "J", "Q", "10"] and card_two in ["A","1","2","3","4","5","6","7","8","9"]:
        return card_one
    if card_two in ["K", "J", "Q", "10"] and card_one in ["A","1","2","3","4","5","6","7","8","9"]:
        return card_two
    if card_one.isdigit() and card_two.isdigit():
        if int(card_one) < int(card_two):
            return card_two
        if int(card_one)> int(card_two):
            return card_one
        return (card_one,card_two)
    
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one == "A"  and card_two  in ["K", "J", "Q","10", "9", "8", "7", "6", "5","4","3","2"]:
        return 1
    if card_two == "A"  and card_one  in ["K", "J", "Q","10", "9", "8", "7", "6", "5","4","3","2"]:
        return 1
    if card_one.isdigit() and card_two.isdigit():
            
        if int(card_one) + int(card_two) >= 11:
            return 1
        if int(card_one) + int(card_two) < 11:
            return 11
    if card_one in ["K", "J", "Q", "10"] or card_two in ["K", "J", "Q", "10"]:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one in ["K", "Q", "J", "10"] and card_two == "A":
        return True
    if card_one == "A" and card_two in ["K", "Q", "J", "10"]:
        return True
    return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one == card_two:
        return True
    elif card_one in ["K", "Q", "J", "10"] and card_two in ["K", "Q", "J", "10"]:
        return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one.isdigit() and card_two.isdigit():
        result = int(card_one) + int(card_two)
        if 9<=result<=11:
            return True
        return False
    if (card_one == "A" or card_one == "1") and card_two in ["K", "J", "Q","10", "9", "8", "7", "6", "5","4","3","2"]:
        return True 
    if card_one in ["K", "J", "Q","10", "9", "8", "7", "6", "5","4","3","2"] and (card_two == "A" or card_two == "1"):
        return True
    return False
    

