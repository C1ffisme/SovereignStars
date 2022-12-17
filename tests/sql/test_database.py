import os
from unittest import TestCase
from sql.database import Database
import sql.database
import configuration


class TestGame(TestCase):
    def setUp(self):
        db_path = os.path.abspath("../../databases/")+"/"+"unittest_db.db"
        if os.path.exists(db_path):
            os.remove(db_path)
        self.db1 = Database("unittest_db")

    def testSaveDirectory(self):
        self.assertEqual(sql.database.get_save_directory(), os.path.abspath("../../databases/"))
        self.assertEqual(self.db1.run_query("SELECT count(*) FROM star_type")[0][0],
                         len(configuration.get_star_types()))
        self.assertEqual(self.db1.run_query("SELECT count(*) FROM ship_type")[0][0],
                         len(configuration.get_ship_types()))

