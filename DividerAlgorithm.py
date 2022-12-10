from typing import Dict

from DecisionVariable import DecisionVariable
from possible_shapes import *
import random
from copy import deepcopy
import time

BOARD_WIDTH = 7
BOARD_HEIGHT = 15


class ShapeDecisionVariable(DecisionVariable[Shape]):
    picked: Shape

    def __init__(self, options: Dict[str, List[Shape]]):
        self.options = options
        self.picked = None

    def pick_shape(self, shape: Shape):
        self.picked = shape


class DividerAlgorithm:
    board: np.ndarray
    shapes: List[Shape]
    next_coordinate_to_fill: Tuple[int, int]

    number_of_shapes_per_size: Dict[str, int]
    counter: int
    shape_1: ShapeDecisionVariable
    shape_2: ShapeDecisionVariable
    shape_3: ShapeDecisionVariable
    shape_4: ShapeDecisionVariable
    shape_5: ShapeDecisionVariable
    shape_6: ShapeDecisionVariable
    shape_7: ShapeDecisionVariable
    shape_8: ShapeDecisionVariable
    shape_9: ShapeDecisionVariable
    shape_10: ShapeDecisionVariable
    shape_11: ShapeDecisionVariable
    shape_12: ShapeDecisionVariable
    shape_13: ShapeDecisionVariable
    shape_14: ShapeDecisionVariable
    shape_15: ShapeDecisionVariable
    shape_16: ShapeDecisionVariable
    shape_17: ShapeDecisionVariable
    shape_18: ShapeDecisionVariable
    shape_19: ShapeDecisionVariable
    shape_20: ShapeDecisionVariable
    shape_21: ShapeDecisionVariable
    shape_22: ShapeDecisionVariable
    shape_23: ShapeDecisionVariable
    shape_24: ShapeDecisionVariable
    shape_25: ShapeDecisionVariable
    shape_26: ShapeDecisionVariable
    shape_27: ShapeDecisionVariable
    shape_28: ShapeDecisionVariable
    shape_29: ShapeDecisionVariable
    shape_30: ShapeDecisionVariable

    def __init__(self):
        self.board = np.array(np.zeros((BOARD_HEIGHT, BOARD_WIDTH)))
        self.shapes = []

        self.shape_1 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_2 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_3 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_4 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_5 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_6 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_7 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_8 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_9 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_10 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_11 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_12 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_13 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_14 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_15 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_16 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_17 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_18 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_19 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_20 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_21 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_22 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_23 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_24 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_25 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_26 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_27 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_28 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_29 = ShapeDecisionVariable(deepcopy(all_shapes))
        self.shape_30 = ShapeDecisionVariable(deepcopy(all_shapes))

        self.decision_variables = [
            self.shape_1,
            self.shape_2,
            self.shape_3,
            self.shape_4,
            self.shape_5,
            self.shape_6,
            self.shape_7,
            self.shape_8,
            self.shape_9,
            self.shape_10,
            self.shape_11,
            self.shape_12,
            self.shape_13,
            self.shape_14,
            self.shape_15,
            self.shape_16,
            self.shape_17,
            self.shape_18,
            self.shape_19,
            self.shape_20,
            self.shape_21,
            self.shape_22,
            self.shape_23,
            self.shape_24,
            self.shape_25,
            self.shape_26,
            self.shape_27,
            self.shape_28,
            self.shape_29,
            self.shape_30,
        ]

        self.number_of_shapes_per_size = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
        self.counter = 1

    def find_next_coordinate_to_fill(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y, x] == 0:
                    self.next_coordinate_to_fill = y, x
                    return y, x

    def try_to_place(self, shape: Shape) -> bool:
        y_board, x_board = self.find_next_coordinate_to_fill()
        for y in range(len(shape.config)):
            for x in range(len(shape.config[y])):
                try:
                    if x_board + x - shape.leftmost_top_pixel[1] < 0:
                        return False
                    board_coordinate = self.board[y_board + y][x_board + x - shape.leftmost_top_pixel[1]]
                except IndexError:  # TODO check for indices instead of causing an exception
                    return False
                shape_coordinate = shape.config[y][x]
                if int(shape_coordinate) == 1 and int(board_coordinate) != 0:
                    return False

        self.place_shape(shape)
        return True

    def place_shape(self, shape: Shape):
        y_board, x_board = self.next_coordinate_to_fill
        for y in range(len(shape.config)):
            for x in range(len(shape.config[y])):
                self.board[y_board + y, x_board + x - shape.leftmost_top_pixel[1]] += shape.config[y][x] * self.counter

    def pick_random_shape_size_between_1_and_6(self, decision_variable: ShapeDecisionVariable):
        possible_shape_sizes: [int] = []
        for size in range(1, 7):
            if len(decision_variable.options[str(size)]) > 0 and self.number_of_shapes_per_size[str(size)] < 5:
                possible_shape_sizes.append(size)
        if len(possible_shape_sizes) == 0:
            return -1
        weighting = []
        for size in possible_shape_sizes:
            weighting.append(2 ** ((5 - self.number_of_shapes_per_size[str(size)]) ** 2))
        return random.choices(possible_shape_sizes, weights=weighting)[0]

    def run(self):
        start_time = time.time()
        iterations = 0
        while self.counter < 31:
            if (time.time() - start_time) > 5:
                return None
            iterations += 1
            next_decision_variable = self.decision_variables[self.counter - 1]
            picked_shape_size_between_1_and_6 = self.pick_random_shape_size_between_1_and_6(next_decision_variable)
            # Step back if there are no available options
            if picked_shape_size_between_1_and_6 == -1:
                next_decision_variable.options = deepcopy(all_shapes)
                self.number_of_shapes_per_size[str(self.decision_variables[self.counter - 2].picked.size)] -= 1
                self.board[self.board == self.counter - 1] = 0
                self.counter -= 1
                continue
            picked_shape = random.choice(next_decision_variable.options[str(picked_shape_size_between_1_and_6)])
            next_decision_variable.options[str(picked_shape_size_between_1_and_6)].remove(picked_shape)
            successful_placement_possible: bool = self.try_to_place(picked_shape)
            if successful_placement_possible:
                next_decision_variable.pick_shape(picked_shape)
                self.number_of_shapes_per_size[str(picked_shape_size_between_1_and_6)] += 1
                self.counter += 1
        
        return np.transpose(self.board)
