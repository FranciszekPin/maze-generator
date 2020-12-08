import mazegen
import mazeshow

# edit this vals to create your custom maze
# -------------
TILE_SIZE = 30
WIDTH = 30
HEIGHT = 30
# -------------

maze = mazegen.get_maze(WIDTH, HEIGHT)
mazeshow.show_maze(maze, TILE_SIZE)
