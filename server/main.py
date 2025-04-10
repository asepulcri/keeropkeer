from server.DividerAlgorithm import *
from server.ColouringAlgorithm import *
from server.StarPlacingAlgorithm import *
import time


def generate_board():
    try:
        start_time = time.time()
        divided_board = DividerAlgorithm().run()
        if divided_board is None:
            exit("Ran out of time")

        print(f'Board generated in {round((time.time() - start_time), 2)}')

        colouring_algorithm = ColouringAlgorithm(np.array(divided_board))
        shape_to_colour_dict = colouring_algorithm.run()

        number_of_colours_used = max(shape_to_colour_dict.values()) + 1
        if number_of_colours_used > 5:
            exit("Colouring algorithm could not find solution")

        star_placement = StarPlacingAlgorithm(divided_board, shape_to_colour_dict).run()

        coloured_board = np.vectorize(shape_to_colour_dict.get)(divided_board)

        return {"board": coloured_board.tolist(), "stars": star_placement}

    except Exception:
        return generate_board()
