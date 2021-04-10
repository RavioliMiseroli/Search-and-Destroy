import random

global env
dim = 50

def get_env():
    """
    Creates 50x50 grid
    :return: env as a grid/2 dimensional list
    """
    env = []
    for row in range(dim):
        env.append([])
        for col in range(dim):
            # make cell a random terrain type
            # 0 = flat, 1 = hilly, 2 = forest, 3 = cave
            env[row].append([random.choices([0.1, 0.3, 0.7, 0.9])[0], False])
    return env

def get_target(_env):
    """
    Selects a random cell and makes it the target.
    :param _maze: maze as a grid
    :return: tuple of the new maze and the coordinates of the selected block.
    """
    row = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)
    _env[row][col][1] = True
    return _env, (row, col)


def get_adjacent(row: int, col: int):
    """
    Returns adjacent neighbors' coordinates.
    :param col:
    :param row:
    :return:
    """
    neighbors = set()
        
    # left
    if row > 0:
        neighbors.add((row - 1, col))
    # right
    if row + 1 < dim:
        neighbors.add((row + 1, col))
    # down
    if col > 0:
        neighbors.add((row, col - 1))
    # up
    if col + 1 < dim:
        neighbors.add((row, col + 1))

    return neighbors

env = get_env()
get_target_coords = get_target(env)
target = get_target_coords[1]

print(target)
