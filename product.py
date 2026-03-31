
from enum import Enum



class Product:
    """Product."""
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Color(Enum):
    """Color."""
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    """Size."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
