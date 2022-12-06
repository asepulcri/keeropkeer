import numpy as np
from typing import Set
import networkx as nx
from DecisionVariable import DecisionVariable
from copy import deepcopy
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap


class ColourDecisionVariable(DecisionVariable[str]):
    colours = ['r', 'o', 'y', 'g', 'b']

    def __init__(self):
        DecisionVariable.__init__(self)
        self.options = deepcopy(ColourDecisionVariable.colours)

    def reset(self):
        self.options = deepcopy(ColourDecisionVariable.colours)
        self.picked = None


class ColouringAlgorithm:
    colours = ['r', 'o', 'y', 'g', 'b']

    def __init__(self, board: np.array(int)):
        self.board = board
        self.current_decision_variable = 1
        self.coloured_board = board.astype(str)
        self.coloured_board_ints = board

        self.decision_variables = [ColourDecisionVariable() for _ in range(30)]
        self.decision_variables_properties: list[tuple[int, Set[int]]]= [self.get_shape_properties(i) for i in range(1,31)]

        self.shape_numbers_per_size = [[] for i in range(6)]

    def get_shape_properties(self, shape_number) -> (int, Set[int]):  # returns size and neighbouring numbers
        indices_current_shape = np.where(self.board == shape_number)
        indices_current_shape = np.dstack(indices_current_shape)
        size_current_shape = np.count_nonzero(self.board == shape_number)
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

    def set_shape_numbers_per_size(self):
        for i, properties in enumerate(self.decision_variables_properties):
            size, _ = properties
            self.shape_numbers_per_size[size-1].append(i+1)
        return

    def create_network(self) -> nx.Graph:
        network = nx.Graph()
        network.add_nodes_from(range(1, 31))
        for i, properties in enumerate(self.decision_variables_properties):
            size, neighbours = properties
            for neighbour in neighbours:
                network.add_edge(i+1, neighbour)
            for shape_number in self.shape_numbers_per_size[size-1]:
                if shape_number != i + 1:
                    network.add_edge(i+1, shape_number)
        return network

    def colour_network(self, network: nx.Graph) -> dict:
        network_colours_dictionary = nx.greedy_color(G=network, strategy="largest_first", interchange=True)
        return network_colours_dictionary

    def run(self):
        self.set_shape_numbers_per_size()

        network = self.create_network()

        network_colours_dictionary = self.colour_network(network)

        print(network_colours_dictionary)

        for key, value in network_colours_dictionary.items():
            shape_number = key
            assigned_colour = self.colours[value]
            self.coloured_board_ints[self.board == shape_number] = value

        labels = self.coloured_board
        cmap = ListedColormap(['red', 'orange', 'yellow', 'green', 'blue'])
        sns.heatmap(self.coloured_board_ints, cmap=cmap, annot=self.coloured_board_ints, cbar=False)
        plt.show()
        return
