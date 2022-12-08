from unittest import TestCase
from game.game import Game
from game.objects.system import System


class TestGame(TestCase):
    def setUp(self):
        self.game1 = Game()
        self.game1.new_galaxy(4)

    def test_galaxy_generation(self):
        self.assertEqual(len(self.game1.systemList), 4)
        self.assertEqual(len(self.game1.systemList), len(self.game1.galaxyList[0].id_list))
        self.assertEqual(type(self.game1.systemList[1]), System)

        print("The following systems were created:")
        for system in self.game1.systemList:
            print(system)
