from possible_shapes import Shape
from typing import TypeVar, Generic

T = TypeVar("T")


class DecisionVariable(Generic[T]):
    def __init__(self):
        self.picked = None

    def pick_shape(self, option: T):
        self.picked = option