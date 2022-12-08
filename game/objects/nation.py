from typing import List
from multipledispatch import dispatch
from game.objects.system import System


class Nation(object):
    @dispatch(str, int, list, int=None)
    def __init__(self, name: str, owner_id: int, owned_stars: List[int], capital: int = None):
        self.name = name
        self.owner_id = owner_id
        self.owned_stars = owned_stars
        self.claimed_stars = []

        if capital and capital not in owned_stars:
            self.capital = None
            print("WARNING: Attempted to declare a star not owned by player as capital. This is an invalid move!")
        else:
            self.capital = capital

    def add_system(self, system: System):
        self.add_system_id(system)

    def add_system_id(self, system_id: int):
        if system_id not in self.owned_stars:
            self.owned_stars.append(system_id)

    def claim_system(self, system: System):
        self.claim_system_id(system)

    def claim_system_id(self, system_id: int):
        if system_id not in self.claimed_stars:
            self.claimed_stars.append(system_id)



