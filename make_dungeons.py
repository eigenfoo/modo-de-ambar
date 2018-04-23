from random import shuffle, sample, randint
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)


def dungeon01():
    room1 = Room("""You enter your home.""")
    room1.desc = """
    Going abroad for college, you don’t really get to go home much. Most of
    your friends take a two or three hour train ride back to home, but it’s a
    16 hour flight for you.
    
    You’ve spent 18 years of your life in this home of homes, and one day you
    packed your life into a suitcase and left. That’s how you left home, and
    that’s how you come back to it: with a suitcase.
    """

    room2 = room1.west = Room("""
    You move into the kitchen.
    Your dad is cooking.
    It smells wonderful, as always.
    """)
    room2.desc = """
    A beef stew with salad: one of your dad’s specials.
    The smell of lovingly caramelized beef and delightfully cooked vegetables
    envelops the kitchen as your dad plates up the food.
    """
    # FIXME put dad here!

    room3 = room2.west = Room("""
    The dining table is set for dinner.
    Your mom is sitting watching the evening news on TV.
    """)
    room3.desc = """
    You mentally tune out the news.
    Something about more demonstrations and protests.
    You get so tired of the politicking that goes on here sometimes.
    """

    room4 = room3.south = Room("""
    The hallway is dark.
    You turn on the lights, which throws amber light
    on what would otherwise been bare white walls.
    """)
    room4.desc = """
    You’ve always thought that the walls should be decorated.
    Perhaps photos of dad, you think.
    He’s always the one taking photos, he always insists on it,
    but that means that no one takes photos of him.
    It’d be nice to see a photo of him.
    """

    room5 = room3.west = Room("""
    You enter your dad’s study.
    """)
    room5.desc = """
    The study is dark, but the light from the corridor pierces through
    the hinges of the door and collides into the bookshelf.
    It reflects off something, startling you.
    """

    room6 = room3.north = Room("""
    You enter the master bedroom.
    """)
    room6.desc = """
    It’s dark and cold.
    The lights are off, and your dad never turns off the air conditioning.
    The imperturbable blue light in corner of the ceiling stares back at you,
    as it continues to blow cold air into the room.
    """

    room7 = room6.north = Room("""
    You enter your helper’s room.
    """)
    room7.desc = """
    It’s by far the smallest of the rooms, and the most full of stuff.
    Growing up, you never really understood that domestic helpers weren’t common
    in other parts of the world...
    In fact, thinking about it now, it’s a bit strange
    to let someone else into your home
    and treat them basically as part of the family,
    but that they’re under your employ.
    """

    room8 = room1.north = Room("""
    You enter your room.
    """)
    room8.desc = """
    It’s your room.
    You can navigate even though its black as death.
    It’s pretty simple to navigate though,
    your dad made sure the bookshelf was placed in a way
    to make sure you wouldn’t accidentally hurt yourself.
    """

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'south'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]



def dungeon02():
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
