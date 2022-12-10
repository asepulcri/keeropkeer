import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib
from DividerAlgorithm import *
from ColouringAlgorithm import *
from StarPlacingAlgorithm import *
import time

game = DividerAlgorithm()

start_time = time.time()
divided_board = game.run()
if divided_board is None:
    exit("Ran out of time")

print(f'Board generated in {round((time.time() - start_time), 2)}')

colouring_algorithm = ColouringAlgorithm(np.array(divided_board))
shape_to_colour_dict = colouring_algorithm.run()

number_of_colours_used = max(shape_to_colour_dict.values()) + 1
if number_of_colours_used > 5:
    exit("Colouring algorithm could not find solution")


star_placement = StarPlacingAlgorithm(divided_board, shape_to_colour_dict).run()
print(star_placement)