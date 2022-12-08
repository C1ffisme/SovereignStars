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
            id_list.append(self.new_star().id)

        self.galaxyList.append(Galaxy(id_list))

    def new_star(self):
        system = System(len(self.systemList))
        self.systemList.append(system)
        return system
