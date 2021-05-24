from abc import abstractmethod, ABC

class Polygon(ABC):
    def __init__(self):
        self.sides = 0
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

class Square(Polygon):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 4

    def draw(self):
        print ("Polygon with 4 sides is a square")


class Triange(Polygon):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 3

    def draw(self):
        print ("Polygon with 3 sides is a triangle")

class Hexagon(Polygon):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 6

    def draw(self):
        print ("Polygon with 6 sides is a hexagon")


def polygonFactory(shape="Triangle"):
    shapes = {
        "Triange": Triange,
        "Square": Square,
        "Hexagon": Hexagon
    }
    return shapes[shape]()

if __name__ == "__main__":
    shapes = ["Square", "Hexagon"]
    for shape in shapes:
        polygonFactory(shape).draw()
