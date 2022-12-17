from typing import List

from game.objects.galaxy import Galaxy
from game.objects.hyperlane import Hyperlane
from game.objects.nation import Nation
from game.objects.system import System


class Game(object):
    def __init__(self):
        self.galaxyList: list[Galaxy] = []
        self.nationList: list[Nation] = []
        self.systemList: list[System] = []
        self.hyperList: list[Hyperlane] = []
        self.turn = 0

        # self.shipTypesList = []

    """ GALAXY MANAGEMENT """

    def new_galaxy(self, random_systems: int = 0):
        id_list = []
        for i in range(random_systems):
            id_list.append(self.new_system().id)

        self.galaxyList.append(Galaxy(id_list))

    def delete_galaxy(self):
        pass

    """ SYSTEM MANAGEMENT """

    def new_system(self, galaxy_id: int = -1) -> System:
        if len(self.systemList) == 0:
            system = System(0)
        else:
            # The new ID will be 1 + the last id we entered in.
            system = System(self.systemList[-1].id + 1)
        self.systemList.append(system)
        if galaxy_id >= 0:
            self.galaxyList[galaxy_id].add_system_id(system.id)
        return system

    def get_system(self, system_id: int):
        for system in self.systemList:
            if system_id == system.id:
                return system

        return None

    def delete_system(self, system_id: int):
        for system in self.systemList:
            if system_id == system.id:
                self.systemList.remove(system)

        for galaxy in self.galaxyList:
            for systemid in galaxy.id_list:
                if systemid == system_id:
                    galaxy.id_list.remove(systemid)

    """ NATION MANAGEMENT"""

    def new_nation(self, name: str, owner_id: int, owned_stars: List[int], capital=-1):
        if len(self.nationList) == 0:
            nation = Nation(0, name, owner_id, owned_stars, capital)
        else:
            # The new ID will be 1 + the last id we entered in.
            nation = Nation(self.nationList[-1].id + 1, name, owner_id, owned_stars, capital)
        self.nationList.append(nation)
        return nation

    def get_nation(self, nation_id: int):
        for nation in self.nationList:
            if nation_id == nation.id:
                return nation

        return None

    def get_nation_by_name(self, nation_name: str):
        for nation in self.nationList:
            if nation_name == nation.name:
                return nation

        return None

    def delete_nation(self, nation_id: int):
        for nation in self.nationList:
            if nation_id == nation.id:
                self.nationList.remove(nation)

    """ HYPERLANE MANAGEMENT """

    def get_hyperlane_index(self, star1: int, star2: int):
        index = 0
        for hyperlane in self.hyperList:
            if (star1 == hyperlane.id1 and star2 == hyperlane.id2) or (
                    star2 == hyperlane.id1 and star1 == hyperlane.id2):
                return index
            index += 1

        return -1

    def add_hyperlane(self, star1: int, star2: int, width: int = 1, wormhole: bool = False):
        if self.get_system(star1) is None or self.get_system(star2) is None:
            print("WARNING: Attempted to build a hyperlane to a non-existent star. This is an invalid move!")
            return

        index = self.get_hyperlane_index(star1, star2)
        if index == -1:
            self.hyperList.append(Hyperlane(star1, star2, width, wormhole))
        else:
            self.hyperList[index].width = width
            self.hyperList[index].wormhole = wormhole

    def delete_hyperlane(self, star1, star2):
        self.hyperList.pop(self.get_hyperlane_index(star1, star2))

    def next_turn(self):
        # WIP: This is where ALL game logic will take place (with some exceptions)
        self.turn += 1
