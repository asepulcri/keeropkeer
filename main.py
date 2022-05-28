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

# [[ 1.  2.  3.  3.  4.  4.  5.  5.  6.  7.  8.  9. 10. 10. 11.]
#  [ 1.  2.  3.  3. 12.  4. 13.  6.  6.  9.  9.  9. 10. 14. 14.]
#  [15. 16. 17.  3. 18. 18. 13. 13. 19.  9.  9. 20. 10. 14. 21.]
#  [22. 16. 17. 23. 24. 18. 18. 13. 19. 19. 25. 20. 10. 14. 21.]
#  [22. 22. 26. 23. 24. 27. 18. 13. 28. 19. 25. 20. 29. 14. 21.]
#  [22. 26. 26. 23. 24. 27. 27. 27. 28. 19. 25. 20. 29. 14. 21.]
#  [30. 30. 30. 30. 30. 30. 27. 27. 28. 28. 25. 29. 29. 29. 29.]]


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
