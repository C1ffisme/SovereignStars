from random import random
from multipledispatch import dispatch


class System(object):
    @dispatch(int, float, float, list[str], str=None, dict=None)
    def __init__(self, id: int, x: float, y: float, star_types: list[str], name: str = None, resources: dict = None):
        self.id = id
        self.x = x
        self.y = y
        self.starTypes = star_types
        self.name = name
        self.resources = resources

    @dispatch(int)
    def __init__(self, id: int):
        self.id = id
        # WIP: Place stars based on id, galaxy size/type.
        self.x = random()
        self.y = random()
        self.name = ""

        # WIP: Randomized parameters based on config file

    def __str__(self):
        name = "Unnamed System"
        if self.name != "":
            name = self.name

        return "(System "+str(self.id)+": "+name+")"
