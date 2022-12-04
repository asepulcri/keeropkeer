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

    def reset(self):
        self.options = deepcopy(ColourDecisionVariable.colours)
        self.picked = None


class ColouringAlgorithm:
    def __init__(self, board: np.array(int)):
        self.board = board
        self.current_decision_variable = 1
        self.coloured_board = board.astype(str)

        self.decision_variables = [ColourDecisionVariable() for _ in range(30)]
        self.decision_variables_properties: list[tuple[int, Set[int]]]= [self.get_shape_properties(i) for i in range(1,31)]

    def get_shape_properties(self, shape_number) -> (int, Set[int]):  # returns size and neighbouring numbers
        indices_current_shape = np.where(self.board == shape_number)
        indices_current_shape = np.dstack(indices_current_shape)
        size_current_shape = len(indices_current_shape)
        neighbouring_shape_numbers: Set[int] = set()

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

    # def remove_colour_from_neighbours(self, decision_variable: ColourDecisionVariable):
    #     picked_colour = decision_variable.picked
    #     neighbours = decision_variable.
    #
    #     return

    def is_legal_pick(self, decision_variable_number: int, colour: str) -> bool:
        decision_variable_properties = self.decision_variables_properties[decision_variable_number - 1]
        size, neighbouring_numbers = decision_variable_properties
        for neighbouring_number in neighbouring_numbers:
            neighbour_decision_variable = self.decision_variables[int(neighbouring_number) - 1]
            if neighbour_decision_variable.picked == colour:
                return False

        for i in range(1, decision_variable_number):
            decision_variable = self.decision_variables[i - 1]

            if decision_variable.picked == colour and self.decision_variables_properties[i - 1][0] == size:
                return False

        return True

    def colour_board(self):
        for i in range(1, 31):
            colour = self.decision_variables[i-1].picked
            np.where(self.coloured_board == str(i), colour, self.coloured_board)


    def run(self):
        attempts = 0
        while self.current_decision_variable < 31 and self.current_decision_variable > 0:
            attempts += 1
            decision_variable : ColourDecisionVariable = self.decision_variables[self.current_decision_variable - 1]
            decision_variable_properties = self.decision_variables_properties[self.current_decision_variable - 1]
            if len(decision_variable.options) < 1:
                decision_variable.reset()
                self.current_decision_variable -= 1
            colour = random.choice(decision_variable.options)
            decision_variable.options.remove(colour)
            if self.is_legal_pick(self.current_decision_variable, colour):
                decision_variable.picked = colour
                self.current_decision_variable += 1

        self.colour_board()

        return self.coloured_board


