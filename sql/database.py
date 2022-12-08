import os
import sqlite3
from multipledispatch import dispatch
import databases  # Needed to find the save directory.
import configuration


def set_up_initial_tables(cur):
    cur.execute("CREATE TABLE system(system_id PRIMARY KEY, name, galaxy_id, nation_id)")
    cur.execute("CREATE TABLE star(system_id, star_type_id, PRIMARY KEY (system_id, star_type_id))")
    cur.execute("CREATE TABLE star_type(star_type_id PRIMARY KEY, name)")
    cur.execute("CREATE TABLE hyperlane(id1, id2, width, wormhole, PRIMARY KEY (id1, id2))")

    cur.execute("CREATE TABLE nation(nation_id PRIMARY KEY, name, color1, color2, capital, owner_discord_id)")
    cur.execute("CREATE TABLE fleet(fleet_id PRIMARY KEY, nation_id, orbiting_system, ship_type_id)")
    cur.execute("CREATE TABLE claim(system_id, nation_id, PRIMARY KEY (nation_id, system_id))")
    cur.execute("CREATE TABLE ship_type(ship_type_id PRIMARY KEY, name, station, attack, armor)")

    star_types = configuration.get_star_types()
    cur.executemany("INSERT INTO star_type VALUES(?,?)", star_types)

    ship_types = configuration.get_ship_types()
    cur.executemany("INSERT INTO ship_type VALUES(?,?,?,?,?)", ship_types)


def get_save_directory():
    return databases.__path__[0]


class Database(object):
    @dispatch(str)
    def __init__(self, database_id: str):
        db_path = get_save_directory() + "/" + database_id + ".db"
        newfile = True
        if os.path.exists(db_path):
            newfile = False

        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

        if newfile:
            set_up_initial_tables(self.cur)

        self.con.commit()

    def run_query(self, query: str):
        # TEMPORARY METHOD. WILL NOT BE LEFT IN FINAL PRODUCT.
        res = self.cur.execute(query)
        return res.fetchall()
