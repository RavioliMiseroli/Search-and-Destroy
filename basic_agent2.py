from pygame.display import update
from environment import *
import random
import numpy as np
import matplotlib.pyplot as plt 
import collections

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
            # P(target found in cell)
            belief[row].append(cell)

    return belief

def initialize_confidence():
    """
    Initializes the agent's belief state
    :return: belief state list
    """
    confidence = []
    for row in range(0, dim):
        confidence.append([])
        for col in range(0, dim):
            cell = 1/2500
            # P(target found in cell)
            prob_tf = cell * (1-env[row][col][0])
            confidence[row].append(prob_tf)

    return confidence

def get_highest_prob(_belief, _confidence, row, col):
    max = (0, 0)
    dupe_probs = [max]

    for r in range(dim):
        for c in range(dim):
            if _confidence[r][c] > _confidence[max[0]][max[1]]:
                max = (r, c)
                dupe_probs.clear()
                dupe_probs = [max]

            elif _confidence[r][c] == _confidence[max[0]][max[1]]:
                dupe_probs.append((r, c))

    # print("Highest prob: ", _belief[dupe_probs[0][0]][dupe_probs[0][1]])
    # print("Highest prob: ", _confidence[dupe_probs[0][0]][dupe_probs[0][1]])

    #find shortest distance add to list
    short_dist_list = []
    min_dist = 5000
    for i in dupe_probs:
        distance = abs(row - i[0]) + abs(col - i[1])
        if distance < min_dist:
            min_dist = distance

    for i in dupe_probs:
        distance = abs(row - i[0]) + abs(col - i[1])
        if distance == min_dist:
            short_dist_list.append(i)

    #return random coordinate thats max prob and shortest distance
    return short_dist_list[random.randint(0, len(short_dist_list)-1)]
            
def update_belief(_belief, _env, row, col, _confidence):
    # P(search failed | target in cell): chance of target not found in search given target in cell: terrain type
    likelihood = _env[row][col][0]
    # print("likelihood: ", likelihood)
    # P(target in cell): prob of cell having target
    prior_prob = _belief[row][col]
    # print("prior_prob: ", prior_prob)
    # P(target not in cell)
    not_in_cell = 1 - prior_prob
    # P(searched failed): target not found in searched cell (compute from marginalization)
    target_not_in_searched_cell = (1*not_in_cell)+(likelihood*prior_prob)
    # print("target not in search cell: ", target_not_in_searched_cell)

    # P(target in cell | search failed)
    numerator = likelihood * prior_prob
    bayes_theorem = numerator/target_not_in_searched_cell
    # print("bayes_theorem: ", bayes_theorem)
    # print("bayes_theorem: ", bayes_theorem)
    _belief[row][col] = bayes_theorem
    _confidence[row][col] = bayes_theorem * (1-likelihood)
    # print("bayes * (1-likelihood): ", bayes_theorem * (1-likelihood))
    return _belief

def print_belief(_belief):
    total = 0
    # print("---- BELIEF ----")
    # for r in range(0, dim):
    #     print(_belief[r])

    for r in range(dim):
        for c in range(dim):
            total = total + _belief[r][c]
    print("Total probability should be 1: ", total)

def print_confidence(_confidence):
    print("---- CONFIDENCE ----")
    for r in range(0, dim):
        print(_confidence[r])

def basic_agent2(_env, _belief, _confidence):
    searches = 0
    distance = 0
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)

    _target = target
    current = (row, col)

    target_not_found = True

    while target_not_found:

        # increment num of searches
        searches += 1
        # search cell
        # cell contains the target
        if current == _target:
            terrain_prob = _env[current[0]][current[1]][0]
            search_prob = random.uniform(0, 1)

            # search failed to find the target
            if search_prob < terrain_prob:
                update_belief(_belief, _env, current[0], current[1], _confidence)

                # normalize matrix
                belief_sum = np.sum(_belief)
                _belief = _belief/belief_sum

                con_sum = np.sum(_confidence)
                _confidence = _confidence/con_sum
                # print_belief(_belief)
            # search success, return total num of searches
            else:
                distance += (abs(row - current[0]) + abs(col - current[1]))
                target_not_found = False
                # print("num of searches ", searches)
                # print("target found at: ", current)
                # print("target terrain: ", _env[current[0]][current[1]][0])
                return (searches, distance)

        # cell doesnt contain the target, update belief state
        else:
            update_belief(_belief, _env, current[0], current[1], _confidence)

            # normalize matrix
            belief_sum = np.sum(_belief)
            _belief = _belief/belief_sum

            con_sum = np.sum(_confidence)
            _confidence = _confidence/con_sum

            # print_belief(_belief)

        current = get_highest_prob(_belief, _confidence, current[0], current[1])
        distance += (abs(row - current[0]) + abs(col - current[1]))
        row = current[0]
        col = current[1]


x = []
n = 1
while n <= 25:
    x.append(n)
    n+=1

y2 =[]

for i in range(25):
    env = get_env()
    belief = initialize_belief()
    confidence = initialize_confidence()
    get_target_coords = get_target(env)
    target = get_target_coords[1]

    results = basic_agent2(env, belief, confidence)
    score = results[0] + results[1]
    y2.append(score)

    # print("searches: " + str(results[0]) + " distance traveled: " + str(results[1]) + " total score: " + str(results[0]+results[1]))
# print_belief(belief)
# # print_confidence(confidence)
# print(target)

print(y2)
plt.plot(x, y2, label = "Basic Agent 2")
plt.xlabel(" Number of Maps ")
plt.ylabel(" Average of Total Score")
plt.title(" Average Total Score for Basic Agent 2")
plt.legend()
plt.show()