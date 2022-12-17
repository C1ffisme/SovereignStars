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

    def test_add_delete_hyperlanes(self):
        self.game1.add_hyperlane(1, 2)  # This should add 1 hyperlane
        self.game1.add_hyperlane(2, 1)  # This shouldn't: it's a duplicate of the previous hyperlane.
        self.game1.add_hyperlane(420, 2)  # This also shouldn't: it's referencing a non-existent star.
        self.assertEqual(1, len(self.game1.hyperList))
        self.game1.delete_hyperlane(2, 1) # Should delete our only hyperlane even though the numbers are in reverse.
        self.assertEqual(0, len(self.game1.hyperList))

    def test_add_nation(self):
        nation1 = self.game1.new_nation("No-Capital Nation", 0, [0, 3], 2)
        nation2 = self.game1.new_nation("Just One Star", 1, [2], 2)
        self.game1.new_nation("Literally no capital", 1, [1])

        self.assertIn(nation1, self.game1.nationList)
        self.assertEqual(self.game1.nationList[0].name, "No-Capital Nation")
        self.assertEqual(self.game1.nationList[1].name, "Just One Star")
        self.assertEqual(self.game1.nationList[2].name, "Literally no capital")
        self.assertEqual(-1, self.game1.nationList[0].capital)
        self.assertNotEqual(-1, self.game1.nationList[1].capital)
        self.assertEqual(-1, self.game1.nationList[2].capital)

        self.assertEqual(nation2, self.game1.get_nation_by_name("Just One Star"))

        self.game1.delete_nation(1)
        self.assertNotIn(nation2, self.game1.nationList)
        self.assertEqual(2, len(self.game1.nationList))
