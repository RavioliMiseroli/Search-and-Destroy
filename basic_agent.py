from environment import dim, env, get_adjacent
import random
import collections
import numpy as np
from collections import deque

def initialize_belief():
    """
    Initializes the agent's belief state
    :return: belief state list
    """
    belief = []
    for row in range(0, dim):
        belief.append([])
        for col in range(0, dim):
            cell = 1/2500
            belief[row].append(cell)

    return belief

def find_highest_prob(_belief, row, col):
    #find max prob add to list
    max = 0
    coordinates = []
    for i in range(len(_belief)):
        for j in range(len(_belief)):
            if _belief[i][j] > max:
                max = _belief[i][j]
                
    for i in range(len(_belief)):
        for j in range(len(_belief)):
            if _belief[i][j] == max:
                coordinates.append((i, j))

    #find shortest distance add to list
    shortDistList = []
    minDist = 5000
    for i in coordinates:
        distance = abs(row - i[0]) + abs(col - i[1])
        if distance < minDist:
            minDist = distance

    for i in coordinates:
        distance = abs(row - i[0]) + abs(col - i[1])
        if distance == minDist:
            shortDistList.append(i)

    #return random coordinate thats max prob and shortest distance
    return shortDistList[random.randint(0, len(shortDistList)-1)]
            
def update_belief(_belief, _env, row, col):
    # P(search failed | target in cell): chance of target not found in search given target in cell: terrain type
    likelihood = _env[row][col][0]
    #print("likelihood: ", likelihood)
    # P(target in cell): prob of cell having target
    prior_prob = _belief[row][col]
    #print("prior_prob: ", prior_prob)
    # P(target not in cell)
    not_in_cell = 1 - prior_prob
    # P(searched failed): target not found in searched cell (compute from marginalization)
    target_not_in_searched_cell = (1*not_in_cell)+(likelihood*prior_prob)
    #print("target not in search cell: ", target_not_in_searched_cell)

    # P(target in cell | search failed)
    numerator = likelihood * prior_prob
    bayes_theorem = numerator/target_not_in_searched_cell
    #print("bayes_theorem: ", bayes_theorem)
    # print("bayes_theorem: ", bayes_theorem)
    _belief[row][col] = bayes_theorem
    # print("bayes * (1-likelihood): ", bayes_theorem * (1-likelihood))
    return _belief

def print_belief(_belief):
    total = 0
    print("---- BELIEF ----")
    #for r in range(0, dim):
        #print(_belief[r])

    for r in range(dim):
        for c in range(dim):
            total = total + _belief[r][c]
    print("Total probability should be 1: ", total)

def basic_agent(_env, _belief):
    searches = 0
    distance = 0
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)

    while True:
        #use chance of false negative
        chance = _env[row][col][0]

        #see if false negative occurs
        genChance = random.uniform(0, 1)
        if genChance < chance:
            _belief = update_belief(_belief, _env, row, col)
            belief_sum = np.sum(_belief)
            _belief = _belief/belief_sum
            #print_belief(_belief)
            searches+=1
        #if not then search
        else:
            if _env[row][col][1]:
                distance += (abs(row - nextCoord[0]) + abs(col - nextCoord[1]))
                return (searches, distance)
            else:
                _belief = update_belief(_belief, _env, row, col)
                belief_sum = np.sum(_belief)
                _belief = _belief/belief_sum
                #print_belief(_belief)
                searches+=1

        #go to next coord and process, add to distance
        nextCoord = find_highest_prob(_belief, row, col)
        distance += (abs(row - nextCoord[0]) + abs(col - nextCoord[1]))
        row = nextCoord[0]
        col = nextCoord[1]

    pass


belief = initialize_belief()

results = basic_agent(env, belief)
print(results[0] + results[1])



