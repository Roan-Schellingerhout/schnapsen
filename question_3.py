from bots.ml import ml
from api import State, util, engine
from itertools import combinations
from collections import defaultdict 

if __name__ == '__main__':   
    rand = ml.Bot(model_file='bots/ml/rand-model.pkl')
    rdeep = ml.Bot(model_file='bots/ml/model.pkl')
    ml_rdeep = ml.Bot(model_file='bots/ml/ml_rdeep-model.pkl')

    combs = combinations([(rand, "rand"), (rdeep, "rdeep"), (ml_rdeep, "ml_rdeep")], 2)

    totalgames = 30
    playedgames = 0

    results = defaultdict(int)

    for players in combs:
        for r in range(10):
            state = State.generate()

            winner, score = engine.play(players[0][0], players[1][0], state, verbose=False)

            if winner is not None:
                winner = players[winner - 1][1]
                results[winner] += score

                playedgames += 1
                print('Played {} out of {:.0f} games ({:.0f}%): {} \r'.format(playedgames, totalgames, playedgames/float(totalgames) * 100, list(results.items())))

    print('Results:')
    for i in results.items():
        print('    bot {}: {} points'.format(i[0], i[1]))
