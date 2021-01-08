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
            # If we move second
            if opcard:
                # find the opponent's suit and all moves we have in that suit
                op_suit = suits[opcard // 5]
                suit_moves = [card for card in state.hand() if suits[card // 5] == op_suit]
        
                # if the opponent played a trump card
                if trump_suit == op_suit:
                    # find all trump suit cards in our hand that are better than the opponent's trump suit card
                    better_trumps = [move for move in trump_moves if move < opcard]
                    # play our worst better trump-suit card, or throw away a card if we have none
                    return (max(better_trumps), None) if len(better_trumps) else (max([card % 5 for card in state.hand()]), None)

                # if the opponent played a different suit than the trump suit
                else:
                    better_in_suit = [move for move in suit_moves if move < opcard]

                    # if we have a better card in the played suit, play the best one we have.
                    if better_in_suit:
                        return (min(better_in_suit), None)

                    # if we don't have a better in-suit card, play our lowest trump-suit card. 
                    elif trump_moves:
                        return (max(trump_moves), None)

                    # if we have neither, throw our worst card away. 
                    else:
                        return (max([card % 5 for card in state.hand()]), None)
            
            else:
                # if we can make a special move (marriage, trump exchange), make it
                special_moves = [i for i in moves if i[1]]
                if any(special_moves):
                    return special_moves[0]

                # otherwise, play the highest non-trump card in your hand, to force the opponent to trump or give up points
                else:
                    return (min([card for card in state.hand() if suits[card // 5] != trump_suit], key = lambda x: x // 5), None)
        
        else:
            if not opcard:
                if trump_moves:
                    return (max(trump_moves), None)
                else:
                    return (max(moves, key = lambda x: x[0] % 5))
            # Return a random choice
            return random.choice(moves)