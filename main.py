import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib
from DividerAlgorithm import *
from ColouringAlgorithm import *
import time

game = DividerAlgorithm()

start_time = time.time()
divided_board = game.run()

colouring_algorithm = ColouringAlgorithm(np.array(divided_board))
coloured_board = colouring_algorithm.run()

print(f'Board generated in {round((time.time() - start_time), 2)}')

print(coloured_board)
