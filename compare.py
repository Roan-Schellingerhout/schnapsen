from argparse import ArgumentParser
from api import State, util, engine
import random, time
from bots.kb_ml import kb_ml
from bots.ml_kb import ml_kb
from bots.project import project
from bots.kbbot import kbbot
from bots.rand import rand
from collections import defaultdict
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    bots = [("kb_ml", kb_ml.Bot()), ("ml_kb", ml_kb.Bot()), ("ml", project.Bot()), ("kb", kbbot.Bot())]

    results = defaultdict(list)

    for bot in bots:
        print(f"Current bot: {bot[0]}")
        for tour in tqdm(range(500)):
            t_score = [0, 0]
            for r in range(10):
                state = State.generate()
                winner, score = engine.play(bot[1], rand.Bot(), state, verbose=False, fast=True)
                t_score[winner - 1] += score
            results[bot[0]].append(tuple(t_score))

    df = pd.DataFrame(results)

    print(df)

    df.to_csv("results_slow.csv")