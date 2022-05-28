import random
import numpy as np


def pick_random_empty_index(board: np.ndarray) -> tuple[int, int]:
    y = random.randint(0, 6)
    x = random.randint(0, 15)
    if board[y, x] == 0:
        return y, x
    else:
        return pick_random_empty_index(board)


class Shape:
    def __init__(self, coordinates: list[tuple[int, int]], colour, size):
        self.coordinates = coordinates
        self.colour = colour
        self.size = size

    @staticmethod
    def get_adjacent_coordinates(board, coordinates: list[tuple[int, int]]):
        adjacent_coordinates = []
        for y, x in coordinates:
            if y - 1 >= 0 and (y - 1, x) not in coordinates:
                adjacent_coordinates.append((y - 1, x))
            if y + 1 <= 6 and (y + 1, x) not in coordinates:
                adjacent_coordinates.append((y + 1, x))
            if x - 1 >= 0 and (y, x - 1) not in coordinates:
                adjacent_coordinates.append((y, x - 1))
            if x + 1 <= 15 and (y, x + 1) not in coordinates:
                adjacent_coordinates.append((y, x + 1))
        return adjacent_coordinates

    def is_attached_to_other_shape_of_same_colour(self, board: np.ndarray, y, x, colour):
        adjacent_coordinates = Shape.get_adjacent_coordinates(board, [(y, x)])
        for y, x in adjacent_coordinates:
            if board[y, x] == colour and (y, x) not in self.coordinates:
                return True
        return False

    def extend_shape(self, board):
        possible_coordinates = []

        adjacent_coordinates = self.get_adjacent_coordinates(board, self.coordinates)
        for y, x in adjacent_coordinates:
            if board[y, x] == 0 and not self.is_attached_to_other_shape_of_same_colour(board, y, x, self.colour):
                possible_coordinates.append((y, x))

        if len(possible_coordinates) > 0:
            to_colour = random.choice(possible_coordinates)
            board[to_colour] = self.colour
            self.coordinates.append(to_colour)
            return

        raise Exception


def create_shape_of_size_n(colour, size, board, y, x):
    shape = Shape([(y, x)], colour, size)
    for i in range(size - 1):
        shape.extend_shape(board)
