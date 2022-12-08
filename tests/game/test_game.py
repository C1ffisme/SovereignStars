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

    def test_add_delete_systems(self):
        system1 = self.game1.new_system(0)
        system2 = self.game1.new_system()

        self.assertIn(system1, self.game1.systemList)
        self.assertIn(system2, self.game1.systemList)
        self.assertEqual(len(self.game1.systemList), 6)
        self.assertIn(system1.id, self.game1.galaxyList[0].id_list)
        self.assertNotIn(system2.id, self.game1.galaxyList[0].id_list)

        self.game1.delete_system(3)

        self.assertEqual(len(self.game1.systemList), 5)
        self.assertEqual(len(self.game1.galaxyList[0].id_list), 4)
