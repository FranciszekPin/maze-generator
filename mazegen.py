from random import randint

maze = []

dirX = [1, 0, -1, 0, 1, 1, -1, -1]
dirY = [0, 1, 0, -1, 1, -1, 1, -1]


def init_empty_maze(width, height):
    for i in range(height):
        new_row = []
        for j in range(width):
            new_row.append("x")
        maze.append(new_row)


def print_maze(width, height):
    print("--------------------------")
    for i in range(height):
        for j in range(width):
            print(maze[i][j], end='')
        print()
    print("--------------------------")


def make_basic_path(x, y, width, height):
    maze[y][x] = " "
    for i in get_random_permutation():
        move_x = x + dirX[i]
        move_y = y + dirY[i]
        if not possible_to_go(move_x, move_y, width, height):
            continue
        make_basic_path(move_x, move_y, width, height)


def possible_to_go(x, y, width, height):
    is_possible = True

    if not is_in_range(x, y, width, height):
        is_possible = False

    elif maze[y][x] == " ":
        is_possible = False

    number_of_neighbour_paths = 0
    if is_possible:
        for i in range(8):
            move_x = x + dirX[i]
            move_y = y + dirY[i]
            if not is_in_range(move_x, move_y, width, height):
                continue
            if maze[move_y][move_x] == " ":
                number_of_neighbour_paths += 1

    if number_of_neighbour_paths > 3:
        is_possible = False

    return is_possible


def is_in_range(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def get_random_permutation():
    arr = [0, 1, 2, 3]
    result = []
    for i in range(4):
        result.append(arr.pop(randint(0, 3 - i)))

    return result


def get_maze(width, height):
    init_empty_maze(width, height)

    make_basic_path(0, 0, width, height)

    return maze
