import numpy as np
from DecisionVariable import DecisionVariable
from copy import deepcopy
import random
import scipy.ndimage as ndimage

class ColourDecisionVariable(DecisionVariable[str]):
    colours = ['r', 'o', 'y', 'g', 'b']

    def __init__(self):
        DecisionVariable.__init__(self)
        self.options = deepcopy(ColourDecisionVariable.colours)


class ColouringAlgorithm:
    def __init__(self, board: np.array(int)):
        self.board = board
        self.current_decision_variable = 1

        self.coloured_board = np.array(board)

    def get_shape_properties(self, shape_number) -> (int, set[int]): #returns size and neighbouring numbers
        indices_current_shape = np.where(self.board == shape_number)
        size_current_shape = len(indices_current_shape)
        neighbouring_shape_numbers = set()
        footprint = np.array([[1, 1, 1],
                              [1, 0, 1],
                              [1, 1, 1]])

        def custom_function(values):
            for value in values:
                neighbouring_shape_numbers.add(value)

        results = ndimage.generic_filter(self.board, custom_function, footprint = footprint, mode = 'constant', cval = 0)
        neighbouring_shape_numbers.remove(shape_number)
        return size_current_shape, neighbouring_shape_numbers

