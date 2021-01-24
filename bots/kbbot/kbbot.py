from api import State, util, Deck
import random
from . import load
from .kb import KB, Boolean, Integer


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()
        random.shuffle(moves)
        played_card = state.get_opponents_played_card()
        beats_opponents_card = []

        def is_trump_suit(card):
            if Deck.get_suit(card) is state.get_trump_suit():
                return True
            return False

        def is_same_suit(card1, card2):
            if Deck.get_suit(card1) is Deck.get_suit(card2):
                return True
            return False

        def is_cheap(card):
            if Deck.get_rank(card) == "J" or Deck.get_rank(card) == "Q" or Deck.get_rank(card) == "K":
                return True
            return False

        if played_card is not None:
            for move in moves:
                if is_trump_suit(played_card):
                    if is_trump_suit(move[0]) and move[0] % 5 < played_card % 5:
                        beats_opponents_card.append(move)
                else:
                    if is_same_suit(move[0], played_card) and move[0] % 5 < played_card % 5:
                        beats_opponents_card.append(move)
                    elif is_trump_suit(move[0]):
                        beats_opponents_card.append(move)

        # game is in phase 1
        if state.get_phase() == 1:
            #print("P:1")
            # in lead
            if state.get_opponents_played_card() is None:
                #print("In lead")
                for move in moves:
                    # trump exchange
                    if move[0] is None:
                        #print("Play trump ex")
                        return move
                    # marriage
                    if move[0] is not None and move[1] is not None:
                        #print("Play marriage")
                        return move
                for move in moves:
                    if not self.ace_consistent(state, move):
                        #print("Play any Ace")
                        return move
                for move in moves:
                    if not self.ten_consistent(state, move):
                        #print("Play any Ten")
                        return move
                for move in moves:
                    if not self.king_consistent(state, move) and not is_trump_suit(move[0]):
                        #print("Play any K")
                        return move
                for move in moves:
                    if not self.queen_consistent(state, move) and not is_trump_suit(move[0]):
                        #print("Play any Q")
                        return move
                for move in moves:
                    if not self.jack_consistent(state, move) and not is_trump_suit(move[0]):
                        #print("Play any J")
                        return move
                return random.choice(moves)
            # opponent in lead
            else:
                #print("Op in lead")
                if is_cheap(played_card) and not is_trump_suit(played_card):
                    #print("PC non trump J || Q || K")
                    if len(beats_opponents_card) > 0:
                        #print("Exists a card that can beat it")
                        for move in beats_opponents_card:
                            if not not self.ace_consistent(state, move) and not is_trump_suit(move[0]):
                                #print("Beat with non trump A")
                                return move
                        for move in beats_opponents_card:
                            if not self.ten_consistent(state, move) and not is_trump_suit(move[0]):
                                #print("Beat with non trump 10")
                                return move
                        for move in beats_opponents_card:
                            if not self.cheap_consistent(state, move) and not is_trump_suit(move[0]):
                                # #print("Beat with non trump J || Q || K")
                                return move
                        else:
                            #print("Beat with first trump card")
                            return beats_opponents_card[0]
                    # if can't beat the card, play cheapest
                    else:
                        #print("Can't beat op card")
                        for move in moves:
                            if not self.cheap_consistent(state, move):
                                #print("Play J || Q || K")
                                return move
                        for move in moves:
                            if not self.ten_consistent(state, move):
                                #print("Play 10")
                                return move
                        for move in moves:
                            if not self.ace_consistent(state, move):
                                #print("Play A")
                                return move
                            else:
                                #print("Random move")
                                return random.choice(moves)
                # try to win the trick any way possible
                else:  # opponents cars is 10 or A (trump or non trump)
                    #print("PC 10 || A (trump || non trump)")
                    if len(beats_opponents_card) > 0:
                        #print("Exists a card that can beat it")
                        #print("Beat with the first card")
                        return beats_opponents_card[0]
                    else:  # if can't beat the card, play the cheapest
                        #print("Can't beat op card")
                        for move in moves:
                            if not self.cheap_consistent(state, move):
                                #print("Play J || Q || K")
                                return move
                        for move in moves:
                            if not self.ten_consistent(state, move):
                                #print("Play 10")
                                return move
                        for move in moves:
                            if not self.ace_consistent(state, move):
                                #print("Play A")
                                return move
                        else:
                            #print("Random move")
                            return random.choice(moves)

                #print("Random move")
                return random.choice(moves)
        # game is in phase 2
        else:
            #print("P:2")
            # in lead
            if state.get_opponents_played_card() is None:
                #print("In lead")
                for move in moves:
                    # marriage
                    if move[0] is not None and move[1] is not None:
                        #print("Play marriage")
                        return move
                for move in moves:
                    #print("Play first trump card")
                    return move
                for move in moves:
                    if not is_trump_suit(move[0]):
                        #print("Play first non trump card")
                        return move
            # opponent in lead
            else:
                #print("Op in lead")
                for move in moves:
                    if is_same_suit(move[0], played_card) and move[0] > played_card:
                        #print("Play first bigger same suit card")
                        return move
                for move in moves:
                    if is_same_suit(move[0], played_card):
                        #print("Play first smaller same suit card")
                        return move
                for move in moves:
                    if is_trump_suit(move[0]) and not self.cheap_consistent(state, move):
                        #print("Play first J || Q || K trump card")
                        return move
                for move in moves:
                    if not self.ten_consistent(self, move) and is_trump_suit(move[0]):
                        #print("Play first 10 trump card")
                        return move
                for move in moves:
                    if not self.ten_consistent(self, move) and is_trump_suit(move[0]):
                        #print("Play first A trump card")
                        return move
                for move in moves:
                    #print("Play random card, bc can't beat op")
                    return random.choice(moves)
        #print("Random move")
        return random.choice(moves)

    def jack_consistent(self, state, move):
        # type: (State, move) -> bool
        kb = KB()

        load.jack_information(kb)
        load.jack_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def queen_consistent(self, state, move):
        kb = KB()

        load.queen_information(kb)
        load.queen_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def king_consistent(self, state, move):
        kb = KB()

        load.king_information(kb)
        load.king_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def ten_consistent(self, state, move):
        kb = KB()

        load.ten_information(kb)
        load.ten_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def ace_consistent(self, state, move):
        kb = KB()

        load.ace_information(kb)
        load.ace_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

    def cheap_consistent(self, state, move):
        kb = KB()

        load.cheap_information(kb)
        load.cheap_knowledge(kb)

        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()
