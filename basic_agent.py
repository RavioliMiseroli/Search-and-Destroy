from environment import dim, env, get_adjacent
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
            cell = 1/2500
            belief[row].append(cell)

    return belief

def print_belief(_belief):
    print("---- BELIEF ----")
    for r in range(0, dim):
        print(_belief[r])
    return

def basic_agent(_env, _belief):
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)

    current = (row, col)


belief = initialize_belief()

# print_belief(belief)

