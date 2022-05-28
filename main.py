import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib
from functions2 import *
import time

start_time = time.time()

# Initialise board
# board = np.array(np.zeros((7, 16)))
#
# colours = [1, 2, 3, 4, 5]
#
# for colour in colours:
#     y, x = pick_random_empty_index(board)
#     board[y, x] = colour
#     create_shape_of_size_n(colour, 6, board, y, x)

game = DividerAlgorithm()

game.run()

print(f'Board generated in {round((time.time() - start_time),2)}')


# cmap = colors.ListedColormap(['white', 'red', 'blue', 'green', 'orange', 'yellow'])
# bounds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# norm = colors.BoundaryNorm(bounds, cmap.N)
#
# fig, ax = plt.subplots()
# ax.imshow(board, cmap=cmap, norm=norm)
#
# # draw gridlines
# ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
# ax.set_xticks(np.arange(-0.5, 15, 1));
# ax.set_yticks(np.arange(-0.5, 6, 1));
#
# plt.show()
