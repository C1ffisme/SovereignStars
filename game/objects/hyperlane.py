from multipledispatch import dispatch

class Hyperlane(object):
    @dispatch(int, int, int, bool)
    def __init__(self, id1: int, id2: int, width: int, wormhole: bool):
        self.id1 = id1
        self.id2 = id2
        self.width = width
        self.wormhole = wormhole