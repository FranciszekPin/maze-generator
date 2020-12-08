import mazegen
import mazeshow

# edit this variables to create your custom maze
# --------------------
TILE_SIZE = 30          # defines the length of the edge of the square in pixels
NUMBER_OF_ROWS = 30     # defines number of tiles in column
NUMBER_OF_COLUMNS = 30  # defines number of tiles in row
# --------------------

maze = mazegen.get_maze(NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)
mazeshow.show_maze(maze, TILE_SIZE)
