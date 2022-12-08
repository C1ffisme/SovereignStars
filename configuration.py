from typing import List

import config


def get_star_types():
    rlist = []
    stlist = read_tuple_file("star_types.txt", ["id", "name"])
    for stype in stlist:
        rlist.append((stype["id"], stype["name"]))

    return rlist


def get_ship_types():
    rlist = []
    stlist = read_tuple_file("ship_types.txt", ["id", "name", "station", "attack", "armor"])
    for stype in stlist:
        rlist.append((stype["id"], stype["name"], stype["station"], stype["attack"], stype["armor"]))

    return rlist

def get_attack_types():
    rlist = []
    stlist = read_tuple_file("attack_types.txt", ["id", "name"])
    for stype in stlist:
        rlist.append((stype["id"], stype["name"]))

    return rlist


def read_tuple_file(filename: str, columns: list) -> List:
    file = open(config.__path__[0] + "/" + filename, "r")

    # The first line in our config files will be used for column names for documentation purposes.
    file.readline()
    returnlist = []
    for line in file:
        # Python leaves an ugly /n at the end of lines, so we want to strip that off.
        splitline = line[:-1].split(", ")
        row = {}
        try:
            i = 0
            for column in columns:
                row[column] = splitline[i]
                i += 1

            returnlist.append(row)
        except IndexError:
            # Skip a broken line
            print("WARNING: invalid line found in config file "+filename+":")
            print(line)
            continue

    file.close()
    return returnlist


