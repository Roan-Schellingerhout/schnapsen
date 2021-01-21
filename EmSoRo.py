"""
Train a machine learning model for the classifier bot. We create a player, and watch it play games against itself.
Every observed state is converted to a feature vector and labeled with the eventual outcome
(-1.0: player 2 won, 1.0: player 1 won)

This is part of the second worksheet.
"""
from api import State, util
import pickle
import os.path
from argparse import ArgumentParser
import time
import sys

# This package contains various machine learning algorithms
import sklearn
import sklearn.linear_model
from sklearn.svm import SVC
import joblib

import pandas as pd

from bots.rand import rand
from bots.project import project
from bots.project.project import features

def create_dataset(path, player=rand.Bot(), games=10, phase=1):
    """Create a dataset that can be used for training the ML bot model.
    The dataset is created by having the player (bot) play games against itself.
    The games parameter indicates how many games will be started.
    
    Each game will be played and the game situations will be stored.
    Then, the game ends and it is recorded whether the game situations resulted in a win or loss for player 1.
    In other words, each game situation is stored with the corresponding class label (won/lost).

    Keyword arguments
    path -- the pathname where the dataset is to be stored
    player -- the player which will play against itself, default the rand Bot
    games -- the number of games to play, default 2000
    phase -- wheter to start the games in phase 1, the default, or phase 2
    """ 
    
    data = []
    target = []

    # For progress bar
    bar_length = 30
    start = time.time()

    for g in range(games-1):

        # For progress bar
        if g % 10 == 0:
            percent = 100.0*g/games
            sys.stdout.write('\r')
            sys.stdout.write("Generating dataset: [{:{}}] {:>3}%".format('='*int(percent/(100.0/bar_length)),bar_length, int(percent)))
            sys.stdout.flush()

        # Randomly generate a state object starting in specified phase.
        state = State.generate(phase=phase)

        state_vectors = []

        while not state.finished():

            # Give the state a signature if in phase 1, obscuring information that a player shouldn't see.
            given_state = state.clone(signature=state.whose_turn()) if state.get_phase() == 1 else state

            # Add the features representation of a state to the state_vectors array
            state_vectors.append(features(given_state))

            # Advance to the next state
            move = player.get_move(given_state)
            state = state.next(move)

        winner, score = state.winner()

        for state_vector in state_vectors:
            data.append(state_vector)

            if winner == 1:
                result = 'won'

            elif winner == 2:
                result = 'lost'

            target.append(result)

    with open(path, 'wb') as output:
        pickle.dump((data, target), output, pickle.HIGHEST_PROTOCOL)

    # For printing newline after progress bar
    print("\nDone. Time to generate dataset: {:.2f} seconds".format(time.time() - start))

    return data, target


## Parse the command line options
parser = ArgumentParser()

parser.add_argument("-d", "--dset-path",
                    dest="dset_path",
                    help="Optional dataset path",
                    default="dataset.pkl")

parser.add_argument("-m", "--model-path",
                    dest="model_path",
                    help="Optional model path. Note that this path starts in bots/ml/ instead of the base folder, like dset_path above.",
                    default="model.pkl")

parser.add_argument("-o", "--overwrite",
                    dest="overwrite",
                    action="store_true",
                    help="Whether to create a new dataset regardless of whether one already exists at the specified path.")

parser.add_argument("--no-train",
                    dest="train",
                    action="store_false",
                    help="Don't train a model after generating dataset.")


options = parser.parse_args()

if options.overwrite or not os.path.isfile(options.dset_path):
    create_dataset(options.dset_path, player=rand.Bot(), games=1000)

if options.train:

    with open(options.dset_path, 'rb') as output:
        data, target = pickle.load(output)

    # Train/test split
    df = pd.DataFrame(data)
    
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df.values, target, test_size = 0.2)

    minmax = sklearn.preprocessing.MinMaxScaler().fit(X_train)
    X_train_scaled = minmax.transform(X_train)
    X_test_scaled = minmax.transform(X_test)

    measures = {"Kernel":[], "C":[], "Accuracy":[], "Precision":[],"Recall":[]}

    # Train a neural network
    for kernel in ["rbf", "sigmoid", "poly", "linear"]:
        print(f"Testing {kernel}")
        for C in [0.1, 1, 10, 100]:
            if kernel != "linear" or C < 1:
                print(f"    C = {C}")
                learner = SVC(kernel=kernel, C=C, random_state=0, probability=True).fit(X_train_scaled, y_train)
                y_pred = learner.predict(X_test_scaled)

                measures["C"].append(C)

                measures["Kernel"].append(kernel)

                measures["Accuracy"].append(sklearn.metrics.accuracy_score(y_test, learner.predict(X_test_scaled)))

                measures["Precision"].append(sklearn.metrics.precision_score(y_test, learner.predict(X_test_scaled), pos_label="won"))

                measures["Recall"].append(sklearn.metrics.recall_score(y_test, learner.predict(X_test_scaled), pos_label="won"))

    print(pd.DataFrame(measures))