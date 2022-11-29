from multipledispatch import dispatch

class System(object):
    @dispatch(int, float, float, str, str=None, dict=None)
    def __init__(self, id: int, x: float, y: float, star_types: list, name: str = None, resources: dict = None):
        self.id = id
        self.x = x
        self.y = y
        self.starTypes = star_types
        self.name = name
        self.resources = resources

