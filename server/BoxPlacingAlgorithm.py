import numpy as np
import copy
import random

from typing import List, Tuple

class BoxPlacingAlgorithm:

    def __init__(self, block_locations: List[List[Tuple[int, int]]], star_locations: List[int]):
        self.block_locations = block_locations
        self.star_locations = star_locations
        self.current_shape_index: int = 0

        self.special_box_locations = []

    def run(self):
        while self.current_shape_index < 5:
            picked = False

            while not picked:
                picked_box = random.choice(self.block_locations[self.current_shape_index])

                if self.star_locations[picked_box[1]] != picked_box[0]:
                    self.special_box_locations.append(list(picked_box))
                    picked = True
                    self.current_shape_index += 1

        return self.special_box_locations