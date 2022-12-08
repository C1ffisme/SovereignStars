from typing import List
from multipledispatch import dispatch
from game.objects.system import System


class Galaxy(object):
    @dispatch(list)
    def __init__(self, id_list: List[int]):
        self.id_list = id_list

    def add_system(self, system: System):
        self.add_system_id(system.id)

    def add_system_id(self, system_id: int):
        if system_id not in self.id_list:
            self.id_list.append(system_id)

    def id_in_galaxy(self, system_id: int):
        return system_id in self.id_list
