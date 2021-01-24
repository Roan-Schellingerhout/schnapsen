from argparse import ArgumentParser
from api import State, util, engine
import random, time
from kb_ml import kb_ml
from ml_kb import ml_kb
from project import project
from kbbot import kbbot

def run_tournament(options):

    botnames = options.players.split(",")

    bots = []
    for botname in botnames:
        bots.append(util.load_player(botname))

    n = len(bots)
    wins = [0] * len(bots)
    matches = [(p1, p2) for p1 in range(n) for p2 in range(n) if p1 < p2]

    totalgames = (n*n - n)/2 * options.repeats
    playedgames = 0

    print('Playing {} games:'.format(int(totalgames)))
    for a, b in matches:
        for r in range(options.repeats):

            if random.choice([True, False]):
                p = [a, b]
            else:
                p = [b, a]

            # Generate a state with a random seed
            state = State.generate(phase=int(options.phase))

            winner, score = engine.play(bots[p[0]], bots[p[1]], state, options.max_time*1000, verbose=options.verbose, fast=options.fast)

            if winner is not None:
                winner = p[winner - 1]
                wins[winner] += score

            playedgames += 1
            print('Played {} out of {:.0f} games ({:.0f}%): {} \r'.format(playedgames, totalgames, playedgames/float(totalgames) * 100, wins))

    print('Results:')
    for i in range(len(bots)):
        print('    bot {}: {} points'.format(bots[i], wins[i]))