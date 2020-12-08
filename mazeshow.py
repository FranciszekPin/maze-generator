import pygame


def draw_maze(maze, screen, tile_size):
    column_number = len(maze[0])
    row_number = len(maze)
    for i in range(column_number):
        for j in range(row_number):
            if maze[j][i] == 'x':
                draw_tile(screen, i * tile_size, j * tile_size, tile_size)


def draw_tile(screen, x, y, tile_size):
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, tile_size, tile_size))


def show_maze(maze, tile_size):
    column_number = len(maze[0])
    row_number = len(maze)
    pygame.init()
    screen = pygame.display.set_mode((tile_size * column_number, tile_size * row_number))

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        draw_maze(maze, screen, tile_size)
        pygame.display.flip()
