from game.objects.galaxy import Galaxy
from game.objects.hyperlane import Hyperlane
from game.objects.nation import Nation
from game.objects.system import System


class Game(object):
    def __init__(self):
        self.galaxyList: list[Galaxy] = []
        self.nationsList: list[Nation] = []
        self.systemList: list[System] = []
        self.hyperList: list[Hyperlane] = []
        self.turn = 0

        # self.shipTypesList = []

    def new_galaxy(self, random_systems: int = 0):
        id_list = []
        for i in range(random_systems):
            id_list.append(self.new_system().id)

        self.galaxyList.append(Galaxy(id_list))

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


    def next_turn(self):
        # WIP: This is where ALL game logic will take place (with some exceptions)
        self.turn += 1
