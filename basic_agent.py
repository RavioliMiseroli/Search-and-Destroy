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

def find_highest_prob(_belief):
    return
            
def update_belief(_belief):
    return

def print_belief(_belief):
    total = 0
    print("---- BELIEF ----")
    for r in range(0, dim):
        print(_belief[r])

    for r in range(dim):
        for c in range(dim):
            total = total + _belief[r][c]
    print("Total probability should be 1: ", total)

def basic_agent(_env, _belief):
    # pick random location for agent
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)

    current = (row, col)


belief = initialize_belief()

print_belief(belief)

