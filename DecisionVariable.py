from possible_shapes import Shape


class DecisionVariable():
    picked: Shape

    def __init__(self, options: dict[str, list[Shape]]):
        self.options = options
        self.picked = None

    def pick_shape(self, shape: Shape):
        self.picked = shape