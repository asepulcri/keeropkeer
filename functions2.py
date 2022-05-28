import numpy as np
from possible_shapes import *
import random
from copy import deepcopy
from exceptions import *

class DecisionVariable():
    picked: Shape

    def __init__(self, options: dict[int, list[Shape]]):
        self.options = options

    def pick_shape(self, shape: Shape):
        self.picked = shape





class DividerAlgorithm:
    board: np.ndarray
    shapes: list[Shape]
    next_coordinate_to_fill: tuple[int, int]

    number_of_shapes_per_size: list[int]
    counter: int
    shape_1: DecisionVariable
    shape_2: DecisionVariable
    shape_3: DecisionVariable
    shape_4: DecisionVariable
    shape_5: DecisionVariable
    shape_6: DecisionVariable
    shape_7: DecisionVariable
    shape_8: DecisionVariable
    shape_9: DecisionVariable
    shape_10: DecisionVariable
    shape_11: DecisionVariable
    shape_12: DecisionVariable
    shape_13: DecisionVariable
    shape_14: DecisionVariable
    shape_15: DecisionVariable
    shape_16: DecisionVariable
    shape_17: DecisionVariable
    shape_18: DecisionVariable
    shape_19: DecisionVariable
    shape_20: DecisionVariable
    shape_21: DecisionVariable
    shape_22: DecisionVariable
    shape_23: DecisionVariable
    shape_24: DecisionVariable
    shape_25: DecisionVariable
    shape_26: DecisionVariable
    shape_27: DecisionVariable
    shape_28: DecisionVariable
    shape_29: DecisionVariable
    shape_30: DecisionVariable

    def __init__(self):
        self.board = np.array(np.zeros((7, 16)))
        self.shapes = []

        self.shape_1 = DecisionVariable(deepcopy(all_shapes))
        self.shape_2 = DecisionVariable(deepcopy(all_shapes))
        self.shape_3 = DecisionVariable(deepcopy(all_shapes))
        self.shape_4 = DecisionVariable(deepcopy(all_shapes))
        self.shape_5 = DecisionVariable(deepcopy(all_shapes))
        self.shape_6 = DecisionVariable(deepcopy(all_shapes))
        self.shape_7 = DecisionVariable(deepcopy(all_shapes))
        self.shape_8 = DecisionVariable(deepcopy(all_shapes))
        self.shape_9 = DecisionVariable(deepcopy(all_shapes))
        self.shape_10 = DecisionVariable(deepcopy(all_shapes))
        self.shape_11 = DecisionVariable(deepcopy(all_shapes))
        self.shape_12 = DecisionVariable(deepcopy(all_shapes))
        self.shape_13 = DecisionVariable(deepcopy(all_shapes))
        self.shape_14 = DecisionVariable(deepcopy(all_shapes))
        self.shape_15 = DecisionVariable(deepcopy(all_shapes))
        self.shape_16 = DecisionVariable(deepcopy(all_shapes))
        self.shape_17 = DecisionVariable(deepcopy(all_shapes))
        self.shape_18 = DecisionVariable(deepcopy(all_shapes))
        self.shape_19 = DecisionVariable(deepcopy(all_shapes))
        self.shape_20 = DecisionVariable(deepcopy(all_shapes))
        self.shape_21 = DecisionVariable(deepcopy(all_shapes))
        self.shape_22 = DecisionVariable(deepcopy(all_shapes))
        self.shape_23 = DecisionVariable(deepcopy(all_shapes))
        self.shape_24 = DecisionVariable(deepcopy(all_shapes))
        self.shape_25 = DecisionVariable(deepcopy(all_shapes))
        self.shape_26 = DecisionVariable(deepcopy(all_shapes))
        self.shape_27 = DecisionVariable(deepcopy(all_shapes))
        self.shape_28 = DecisionVariable(deepcopy(all_shapes))
        self.shape_29 = DecisionVariable(deepcopy(all_shapes))
        self.shape_30 = DecisionVariable(deepcopy(all_shapes))

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

        self.number_of_shapes_per_size = [0, 0, 0, 0, 0, 0]
        self.counter = 1

    def find_next_coordinate_to_fill(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y,x] == 0:
                    self.next_coordinate_to_fill = y, x
                    return y, x

    def try_to_place(self, shape: Shape):
        y_board, x_board = self.find_next_coordinate_to_fill()
        for y in range(len(shape.config)):
            for x in range(len(shape.config[y])):
                try:
                    board_coordinate = self.board[y_board + y][x_board + x - shape.leftmost_top_pixel[1]]
                except IndexError:
                    raise OutofBoundsException()
                shape_coordinate = shape.config[y][x]
                if int(shape_coordinate) == 1 and int(board_coordinate) != 0:
                    raise OverlappingShapeException()

        self.place_shape(shape)
        return

    def place_shape(self, shape: Shape):
        y_board, x_board = self.next_coordinate_to_fill
        for y in range(len(shape.config)):
            for x in range(len(shape.config[y])):
                self.board[y_board + y, x_board + x - shape.leftmost_top_pixel[1]] += shape.config[y][x] * self.counter

    def pick_random_shape_size_between_1_and_6(self, decision_variable: DecisionVariable):
        possible_shape_sizes : [int] = []
        for size in range(1, 7):
            if len(decision_variable.options[size]) > 0 and self.number_of_shapes_per_size[size-1] < 6:
                possible_shape_sizes.append(size)
        if len(possible_shape_sizes) == 0:
            return -1
        return random.choice(possible_shape_sizes)


    def run(self):
        next_decision_variable = self.decision_variables[self.counter - 1]
        for i in range(999):
            picked_shape_size = self.pick_random_shape_size_between_1_and_6(next_decision_variable)

            # picked_shape_size = random.randint(0, 5)
            picked_shape: Shape = None
            # noinspection PyBroadException
            print(self.board)
            try:
                picked_shape = random.choice(next_decision_variable.options[picked_shape_size])
                self.try_to_place(picked_shape)
                self.number_of_shapes_per_size[picked_shape_size - 1] += 1
                # if self.number_of_shapes_per_size[picked_shape_size - 1] == 6:
                #     next_decision_variable.options.remove(picked_shape_size)
                self.counter += 1
            except (OverlappingShapeException, OutofBoundsException):
                if picked_shape is not None:
                    next_decision_variable.options[picked_shape_size].remove(picked_shape)
