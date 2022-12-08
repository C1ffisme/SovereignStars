from multipledispatch import dispatch


class Fleet(object):
    @dispatch(int, int, int)
    def __init__(self, created_system: int, fleet_size: int, ship_type: int):
        self.orbitingStarID = created_system
        self.fleet_size = fleet_size
        self.ship_type = ship_type
