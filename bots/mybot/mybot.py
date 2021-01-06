"""
RandomBot -- A simple strategy: enumerates all legal moves, and picks one
uniformly at random.
"""

# Import the API objects
from api import State
import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
       	TODO: add some more explanation
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        # All legal moves
        moves = state.moves()

        # Calculations and metadata
        opcard = state.get_opponents_played_card()
        suits = ["C", "D", "H", "S"]

        trump_suit = state.get_trump_suit() 
        trump_moves = [card for card in state.hand() if suits[card // 5] == trump_suit]

        if state.get_phase() == 1:
            if opcard:
        
                op_suit = suits[opcard // 5]
                suit_moves = [card for card in state.hand() if suits[card // 5] == op_suit]
        
                # if the opponent played a trump card
                if trump_suit == op_suit:
                    # find all trump suit cards in our hand that are better than the opponent's trump suit card
                    better_trumps = [move for move in trump_moves if move < opcard]
                    return (max(better_trumps), None) if len(better_trumps) else (max([card % 5 for card in state.hand()]), None)

                # if the opponent played a different suit than the trump suit
                else:
                    # if we do not have a trump-suit card, play our worst card in the given suit
                    if not(trump_moves):
                        better_in_suit = [move for move in suit_moves if move < opcard]
                        return (max(better_in_suit), None) if len(better_in_suit) else (max([card % 5 for card in state.hand()]), None)

                    # if we do have a trump-suit card, play our lowest trump-suit card. 
                    else:
                        return (max(trump_moves), None)
            
            else:
                # if marriage or trump exchange, do it

        # Return a random choice
        return random.choice(moves)