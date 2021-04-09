from pygame.display import update
from environment import dim, env, get_adjacent, target
import random
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
            cell = 1/100
            belief[row].append(cell)

    return belief

def get_highest_prob(_belief):
    max = (0, 0)
    dupe_probs = [max]

    for r in range(dim):
        for c in range(dim):
            if _belief[r][c] > _belief[max[0]][max[1]]:
                max = (r, c)
                dupe_probs.clear()
                dupe_probs = [max]

            elif _belief[r][c] == _belief[max[0]][max[1]]:
                dupe_probs.append((r, c))

    rand = random.randint(0, len(dupe_probs) - 1)
    # print("Highest prob: ", _belief[dupe_probs[0][0]][dupe_probs[0][1]])
    print("Highest prob: ", _belief[dupe_probs[0][0]][dupe_probs[0][1]])
    return dupe_probs[rand]
            
def update_belief(_belief, _env, row, col):
    for r in range(dim):
        for c in range(dim):
            if (r, c) == (row, col):
                continue
            # P(search failed | target in cell)
            likelihood = 1
            # P(target in cell): prob of cell having target
            prior_prob = _belief[r][c]
            # P(target not in cell)
            not_in_cell = 1 - prior_prob
            # P(searched failed): prob of cell not having target (compute from marginalization)
            not_prior_prob = (1*not_in_cell)+(_env[r][c][0]*prior_prob)
            # P(target in cell | search failed)
            bayes_method = (likelihood*prior_prob)/not_prior_prob

            _belief[r][c] = bayes_method

            # # P(target not in cell | search fail)
            # final_belief = (1 - bayesian_method)
            # print("final belief ", final_belief)

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

def basic_agent(_env, _belief):
    searches = 0
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)

    _target = target
    current = (row, col)

    target_not_found = True

    while target_not_found:
        # not the initial search
        if searches != 0:
            current = get_highest_prob(_belief)

        # increment num of searches
        searches += 1
        # search cell
        # cell contains the target
        if current == _target:
            terrain_prob = _env[current[0]][current[1]][0]
            search_prob = random.uniform(0, 1)

            # search failed to find the target
            if search_prob > terrain_prob:
                # update all cells using bayes theorem

                # P(search failed | target in cell): terrain prob
                likelihood = _env[current[0]][current[1]][0]
                # print("likelihood: ", likelihood)

                # P(target in cell): prob of cell having target
                prior_prob = _belief[current[0]][current[1]]
                # print("prior prob: ", prior_prob)

                # P(target not in cell)
                not_in_cell = 1 - prior_prob
                # P(searched failed): prob of cell not having target (compute from marginalization)
                not_prior_prob = 1*(not_in_cell)+likelihood*prior_prob
                # print("not prior prob: ", not_prior_prob)

                # P(target in cell | search failed)
                bayesian_method = (likelihood*prior_prob)/(not_prior_prob)
                # print("bayes method ", bayesian_method)

                # P(target not in cell | search fail)
                final_belief = (1 - bayesian_method)
                # print("final belief ", final_belief)

                _belief[current[0]][current[1]] = bayesian_method
                update_belief(_belief, _env, current[0], current[1])

            # search success, return total num of searches
            else:
                target_not_found = False
                print("num of searches ", searches)
                print("target found at: ", current)
                print("target terrain: ", _env[current[0]][current[1]][0])
                return searches

        # cell doesnt contain the target, update belief state
        else:
            # P(search failed | target in cell)
            likelihood = 1
            # print("likelihood: ", likelihood)

            # P(target in cell): prob of cell having target
            prior_prob = _belief[current[0]][current[1]]
            # print("prior prob: ", prior_prob)

            # P(target not in cell)
            not_in_cell = 1 - prior_prob
            # print("not in cell: ", not_in_cell)

            # P(searched failed): prob of cell not having target (compute from marginalization)
            not_prior_prob = (1*not_in_cell)+(_env[current[0]][current[1]][0]*prior_prob)
            # print("not prior prob: ", not_prior_prob)

            # P(target in cell | search failed)
            bayes_method = (likelihood*prior_prob)/not_prior_prob
            # print("bayes method ", bayes_method)

            _belief[current[0]][current[1]] = bayes_method

            # # P(target not in cell | search fail)
            # final_belief = (1 - bayesian_method)
            # print("final belief ", final_belief)

            update_belief(_belief, _env, current[0], current[1])


belief = initialize_belief()

basic_agent(env, belief)

print_belief(belief)

print(target)

