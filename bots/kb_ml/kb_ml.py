# Import the API objects
from api import State
from bots.kbbot import kbbot
from bots.project import project

class Bot:

    def __init__(self):
        self.kb_bot = kbbot.Bot()
        self.ml_bot = project.Bot()

    def get_move(self, state):
        if state.get_phase() == 1:
            return self.kb_bot.get_move(state)
        else:
            return self.ml_bot.get_move(state)
        