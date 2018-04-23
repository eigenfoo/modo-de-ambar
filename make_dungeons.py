from random import shuffle, sample, randint
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)

COLORS = range(9)


def dungeon01():
    ''' George '''

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
    The dining table is set for dinner.
    Your mom is sitting watching the evening news on TV.
    """)
    room2.desc = """
    You mentally tune out the news.
    Something about more demonstrations and protests.
    You get so tired of the politicking that goes on here sometimes.
    """
    room2.dinner = False

    room3 = room2.west = Room("""
    The hallway is dark.
    You turn on the lights, which throws amber light
    on what would otherwise been bare white walls.
    """)
    room3.desc = """
    You’ve always thought that the walls should be decorated.
    Perhaps photos of dad, you think.
    He’s always the one taking photos, he always insists on it,
    but that means that no one takes photos of him.
    It’d be nice to see a photo of him.
    """

    room6 = room3.north = Room("""
    You enter your dad’s study.
    """)
    room6.desc = """
    The study is dark, but the light from the corridor pierces through
    the hinges of the door and collides into the bookshelf.
    It reflects off something, startling you.
    """
    photo = Item('framed photograph')
    room6.items = Bag({photo})

    room7 = room6.north = Room("""
    You enter the master bedroom.
    """)
    room7.desc = """
    It’s dark and cold.
    The lights are off, and your dad never turns off the air conditioning.
    The imperturbable blue light in corner of the ceiling stares back at you,
    as it continues to blow cold air into the room.
    """

    room4 = room3.south = Room("""
    You enter your helper’s room.
    """)
    room4.desc = """
    It’s by far the smallest of the rooms, and the most full of stuff.
    Growing up, you never really understood that domestic helpers weren’t common
    in other parts of the world...
    In fact, thinking about it now, it’s a bit strange
    to let someone else into your home
    and treat them basically as part of the family,
    but that they’re under your employ.
    """

    room5 = room3.west = Room("""
    You enter your room.
    """)
    room5.desc = """
    It’s your room.
    You can navigate even though its black as death.
    It’s pretty simple to navigate though,
    your dad made sure the bookshelf was placed in a way
    to make sure you wouldn’t accidentally hurt yourself.
    """
    music_box = Item('music box')
    room5.items = Bag({music_box})

    room8 = room1.north = Room("""
    You move into the kitchen.
    Your dad is cooking.
    It smells wonderful, as always.
    """)
    room8.desc = """
    A beef stew with salad: one of your dad’s specials.
    The smell of lovingly caramelized beef and delightfully cooked vegetables
    envelops the kitchen as your dad plates up the food.
    """
    dad = Item('Dad')
    dinner = Item('dinner')
    room8.items  = Bag({dad, dinner})

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

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
    You wake up to the faint smell of morning air.
    """)
    room1.desc = """
    The ambient snoring of your friend fills the room.
    It suddenly dawns upon you that you are in an AirBnb in Kyoto.
    You should probably get ready and prepare for a full day of adventuring.
    """
    phone = Item('phone')
    friend = Item('friend')
    room1.items = Bag({phone, friend})

    room2 = room1.north = Room("""
    The sliding door to the balcony is slightly ajar.
    """)
    room2.desc = """
    The dawn light streams through the curtains in a surreal manner.
    The buildings of Kyoto stand proud against the horizon.
    A chilly breeze continuously enters the room from beyond the balcony.
    """

    room3 = room2.north = Room("""
    You open the sliding door and step onto the balcony.
    """)
    room3.desc = """
    It isn’t such a windy day today, thankfully.
    You were lucky with this AirBnb, the view is incredible.
    You can see all the way to the river.
    Perhaps today would be a good day to go to the Kyoto Animation Store. 
    """

    room4 = room3.west = Room("""
    You are faced with a giant building.
    """)
    room4.desc = """
    Well, not every direction can have amazing views.
    """

    room5 = room1.west = Room("""
    The bathroom is pretty small.
    """)
    room5.desc = """
    In fact, the entire room is the shower room.
    The plumbing is amazing though.
    The shower is hot and has high water pressure.
    """
    shower = Item('shower')
    towel = Item('towel')
    soap = Item('soap')
    room5.items = Bag({shower, towel, soap})

    room6 = room5.south = Room("""
    The kitchen area is pretty small.
    """)
    room5.desc = """
    There’s barely enough space for 1 stove burner and a tiny sink.
    This is where the two of you store your toothbrushes.
    """
    toothbrush = Item('toothbrush')
    toothpaste = Item('toothpaste')
    sink = Item('sink')
    room5.items = Bag({toothbrush, toothpaste, sink})

    room7 = room6.south = Room("""
    A dark hallway.
    """)
    room7.desc = """
    Strangely, this part of the apartment doesn’t have lights.
    How peculiar. 
    """

    room8 = room7.east = Room("""
    The entrance to the apartment.
    """)
    room8.desc = """
    Your shoes are neatly arranged in the corner.
    """
    shoes = Item('shoes')
    room8.items = Bag({shoes})

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
    """)
    room1.desc = """
    asdf
    """

    room2 = room1.east = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    room3 = room1.north = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    room4 = room3.west = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    room5 = room3.north = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    room6 = room5.east = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    room7 = room6.north = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """
    foo = Item('foobar')
    room7.items = Bag({foo})

    room8 = room6.east = Room("""
    You are in a {} room.
    """)
    room1.desc = """
    asdf
    """

    wait = room8.east = Room("""
    You are in a waiting room.
    """)

    exit_dir = 'east'

    return [room1, room2, room3, room4, room5, room6, room7, room8,
            wait, exit_dir]
