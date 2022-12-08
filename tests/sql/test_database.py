import os
from unittest import TestCase
from sql.database import Database

class TestGame(TestCase):
    def setUp(self):
        db_path = os.path.abspath("../../databases/")+"/"+"unittest_db.db"
        if os.path.exists(db_path):
            os.remove(db_path)
        self.db1 = Database("unittest_db")

    def testSaveDirectory(self):
        self.assertEqual(self.db1.get_save_directory(), os.path.abspath("../../databases/"))
        self.assertEqual(self.db1.run_query("SELECT * FROM star_type"), [(1, "Yellow Dwarf"), (2, "Red Dwarf")])
