from random import shuffle
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)


COLORS = ['green', 'red', 'blue', 'purple',
          'orange', 'white', 'yellow', 'black']

def dungeon01():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.south = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.east = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.east = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.east = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.south = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon02():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.north = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.west = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room8 = room4.north = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    room7 = room8.east = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    wait = room8.north = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'north'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon03():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.south = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.south = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.west = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room5.south = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.south = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.west = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'west'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon04():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.south = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.east = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room2.south = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.south = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room2.west = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.west = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.south = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon05():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.north = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.east = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.north = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room2.south = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.east = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.south = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon06():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.north = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.west = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.south = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.south = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon07():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.east = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.east = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.east = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.east = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.east = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room7.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon08():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.south = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.west = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room8 = room3.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    room5 = room8.north = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room8.east = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.south = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon09():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.west = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.north = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room8 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    room6 = room8.south = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room8.east = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    wait = room8.north = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'north'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon10():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.west = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.north = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room3.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.west = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room8 = room1.south = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    room7 = room8.west = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon11():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.east = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.south = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.north = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.north = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room5.south = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon12():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.north = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.north = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room5.west = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room5.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon13():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room1.west = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.west = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room3.south = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.south = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.west = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room6.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon14():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.south = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.south = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room4.west = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.west = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room5.south = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room4.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.south = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon15():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room2.east = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.east = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room8 = room5.north = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    room7 = room8.north = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room6 = room7.north = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]

def dungeon16():
    shuffle(COLORS)

    room1 = Room("""
    You are in a {} room.
    """.format(COLORS[0]))

    room2 = room1.east = Room("""
    You are in a {} room.
    """.format(COLORS[1]))

    room3 = room1.north = Room("""
    You are in a {} room.
    """.format(COLORS[2]))

    room4 = room3.west = Room("""
    You are in a {} room.
    """.format(COLORS[3]))

    room5 = room3.north = Room("""
    You are in a {} room.
    """.format(COLORS[4]))

    room6 = room5.east = Room("""
    You are in a {} room.
    """.format(COLORS[5]))

    room7 = room6.north = Room("""
    You are in a {} room.
    """.format(COLORS[6]))

    room8 = room6.east = Room("""
    You are in a {} room.
    """.format(COLORS[7]))

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]
