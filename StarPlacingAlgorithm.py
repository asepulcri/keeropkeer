import numpy as np
import copy
import random


class ColumnDecisionVariable:
    row_indices = [i for i in range(7)]
    options: list[int]

    def __init__(self):
        self.picked_row_index: int = -1
        self.picked_shape_number = -1
        self.options = copy.deepcopy(self.row_indices)

    def pick(self, picked_shape_number: int, picked_row_index: int):
        self.picked_row_index = picked_row_index
        self.picked_shape_number = picked_shape_number
        self.options.remove(picked_row_index)

    def remove_option(self, picked_row_index: int):
        self.options.remove(picked_row_index)


class StarPlacingAlgorithm:

    def __init__(self, board: np.array(int), shape_to_colour_dict: dict[int, int]):
        self.board = board
        self.shape_to_colour_dict = shape_to_colour_dict
        self.column_decision_variables = [ColumnDecisionVariable() for i in range(15)]
        self.current_column_index: int = 0
        self.stars_per_colour = [0 for i in range(5)]
        self.shape_numbers_with_stars: list[int] = []

    def is_legal(self, picked_row_index: int, picked_shape_number: int, picked_shape_colour: int) -> bool:
        x = self.current_column_index
        y = picked_row_index

        # check that left neighbour was not picked
        if x > 0 and self.column_decision_variables[x - 1].picked_row_index == picked_row_index:
            return False

        if self.stars_per_colour[picked_shape_colour] == 3:
            return False

        if picked_shape_number in self.shape_numbers_with_stars:
            return False

        return True

    def run(self):
        while self.current_column_index < 15:
            decision_variable = self.column_decision_variables[self.current_column_index]

            # Check if there are any options
            if len(decision_variable.options) == 0:
                self.column_decision_variables[self.current_column_index] = ColumnDecisionVariable()
                self.current_column_index -= 1
                continue

            picked_row_index = random.choice(decision_variable.options)
            picked_shape_number = self.board[picked_row_index][self.current_column_index]
            picked_shape_colour = self.shape_to_colour_dict[picked_shape_number]

            if self.is_legal(picked_row_index, picked_shape_number, picked_shape_colour):
                decision_variable.pick(picked_shape_number, picked_row_index)
                self.current_column_index += 1
                self.stars_per_colour[picked_shape_colour] += 1
                self.shape_numbers_with_stars.append(picked_shape_number)
            else:
                decision_variable.remove_option(picked_row_index)

        picked_row_indices = [dv.picked_row_index for dv in self.column_decision_variables]
        return picked_row_indices
