from basic_agent import initialize_belief, update_belief, print_belief
from environment import *
import random
import collections
import numpy as np
from collections import deque

def normalizePriority(priorities):
    for i in range(len(priorities)):
        for j in range(len(priorities)):
            priorities[i][j]["able"] = True

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

    #return whole lsit of coords
    return shortDistList

def advanced_agent(_env, _belief):
    searches = 0
    distance = 0
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)
    nextCoord = []
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
                if len(nextCoord) > 0:
                    distance += (abs(row - nextCoord[0]) + abs(col - nextCoord[1]))
                return (searches, distance)
            else:
                _belief = update_belief(_belief, _env, row, col)
                belief_sum = np.sum(_belief)
                _belief = _belief/belief_sum
                #print_belief(_belief)
                searches+=1

        #go to next coord and process, add to distance
        nextCoords = find_highest_prob(_belief, row, col)
        localBest = ()
        localBestBeliefSum = 0
        for i in nextCoords:
            sum = 0
            testBelief = update_belief(_belief, _env, i[0], i[1])
            testBeliefSum = np.sum(testBelief)
            testBelief = testBelief/testBeliefSum
            if i[0]+1 < 50 and i[0] +1 >= 0:
                sum += testBelief[i[0]+1, i[1]]
            if i[0]-1 < 50 and i[0]-1 >= 0:
                sum += testBelief[i[0]-1, i[1]]
            if i[1]-1 < 50 and i[1]-1 >= 0:
                sum += testBelief[i[0], i[1]-1]
            if i[1]+1 < 50 and i[1]+1 >= 0:
                sum += testBelief[i[0], i[1]+1]
            if sum > localBestBeliefSum:
                localBest = i
                localBestBeliefSum = sum

        nextCoord = localBest

        distance += (abs(row - nextCoord[0]) + abs(col - nextCoord[1]))
        row = nextCoord[0]
        col = nextCoord[1]

    pass

belief = initialize_belief()
env = get_env()
get_target_coords = get_target(env)
target = get_target_coords[1]
results = advanced_agent(env, belief)
print(results[0] + results[1])