import numpy as np
from typing import Set

from DecisionVariable import DecisionVariable
from copy import deepcopy
import random


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

    def get_shape_properties(self, shape_number) -> (int, Set[int]):  # returns size and neighbouring numbers
        indices_current_shape = np.where(self.board == shape_number)
        indices_current_shape = np.dstack(indices_current_shape)
        size_current_shape = len(indices_current_shape)
        neighbouring_shape_numbers = set()

        for index in indices_current_shape[0]:
            neighbouring_shape_numbers = neighbouring_shape_numbers.union(self.get_neighbours(index[1], index[0]))
        if shape_number in neighbouring_shape_numbers:
            neighbouring_shape_numbers.remove(shape_number)
        return size_current_shape, neighbouring_shape_numbers

    def get_neighbours(self, x, y) -> Set[int]:
        neighbouring_shape_numbers = set()
        if y + 1 < self.board.shape[0]:
            neighbouring_shape_numbers.add(self.board[y + 1][x])
        if y - 1 >= 0:
            neighbouring_shape_numbers.add(self.board[y - 1][x])
        if x + 1 < self.board.shape[1]:
            neighbouring_shape_numbers.add(self.board[y][x + 1])
        if x - 1 >= 0:
            neighbouring_shape_numbers.add(self.board[y][x - 1])

        return neighbouring_shape_numbers
