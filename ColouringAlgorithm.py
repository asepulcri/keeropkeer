import numpy as np
from DecisionVariable import DecisionVariable



class ColouringAlgorithm:
    def __init__(self, board: np.array[int]):
        self.board = board
        self.colours = ['r', 'y', 'b', 'o', 'g']
        self.decision_variables = np.array(30)

        self.decision_variables[:] = DecisionVariable