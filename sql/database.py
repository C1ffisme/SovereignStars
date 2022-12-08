import os
import sqlite3
from multipledispatch import dispatch
import game.game
import databases # Needed to find the save directory.
import configuration

class Database(object):
    @dispatch(str)
    def __init__(self, database_id: str):
        self.con = sqlite3.connect(self.get_save_directory() + "/" + database_id + ".db")
        self.cur = self.con.cursor()

        self.set_up_initial_tables(self.cur)

        self.con.commit()

    def set_up_initial_tables(self, cur):
        cur.execute("CREATE TABLE system(system_id, name, galaxy_id, nation_id)")
        cur.execute("CREATE TABLE star(system_id, star_type_id)")
        cur.execute("CREATE TABLE star_type(star_type_id, name)")

        star_types = configuration.get_star_types()
        cur.executemany("INSERT INTO star_type VALUES(?,?)", star_types)

    def run_query(self, query: str):
        # TEMPORARY METHOD. WILL NOT BE LEFT IN FINAL PRODUCT.
        res = self.cur.execute(query)
        return res.fetchall()

    def get_save_directory(self):
        return databases.__path__[0]
