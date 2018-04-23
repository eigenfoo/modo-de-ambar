from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)

def dad():
    s1 = """
    Your dad chastises you for standing around, taking up space in the kitchen.
    He tells you to take the three plated dishes out to the dining room.
    """

    s2 = " "

    return s1, s2


def dinner():
    s1 = """
    As you pick up the plate, you notice that the beef
    has been cooked so well that it practically falls off the bone.
    Your mouth waters.
    """

    s2 = ""
    
    return s1, s2


def photo():
    s1 = """
    You inspect the photo for what must be the 100th time.
    You’re sitting right in front of the camera, with a pudgy face, bald head
    and distracted by something slightly to the left of the camera.
    You know that your dad was the one who took the photo:
    something about the way the photo is composed…
    Something possesses you to pocket the photo.
    """

    s2 = ""

    return s1, s2


def music_box():
    s1 = """
    A gift from your dad.
    You’ve always been amazed at how the clockwork manages
    to produce not just one, but six
    distinct classical melodies from its metal organs.
    You still remember the day you realized that the gears
    were beginning to rust, and that you couldn’t fix them
    without shattering the glass.
    That wasn’t a great day.
    """

    s2 = ""

    return s1, s2


def phone():
    s1 = """
    A black iPhone, plus model.
    It has seen years of use which is apparent on the aluminum finish.
    With its long battery life, it is sure to last an entire day’s sightseeing.
    You’ve only been using it to take pictures of your vacation journey.
    The excitement of being in a foreign country has eased
    your addiction to mobile games.
    """

    s2 = ""

    return s1, s2


def friend():
    s1 = """
    You decide to wake up your friend.
    You need an early start to get the most
    out of exploring Kyoto today. 
    """

    s2 = " "
    
    return s1, s2


def shower():
    s1 = """
    You spend 15 minutes in the shower.
    """

    s2 = "You feel refreshed."

    return s1, s2


def towel():
    s1 = """
    A common white bath towel.
    There is nothing special about it.
    """

    s2 = ""

    return s1, s2


def soap():
    s1 = """
    Common bar soap.
    There is nothing special about it,
    except for the slight fragrance of lavender.
    """

    s2 = ""

    return s1, s2


def toothbrush():
    s1 = """
    A small travel sized toothbrush.
    """

    s2 = ""

    return s1, s2

def toothpaste():
    s1 = """
    A small tube of travel sized toothpaste.
    """

    s2 = ""

    return s1, s2


def sink():
    s1 = """
    You take 2 minutes to brush your teeth.
    This is not the electric toothbrush you are used to.
    Your hand feels slightly out of shape. 
    """

    s2 = "You finish brushing your teeth."

    return s1, s2


def shoes():
    s1 = """
    You slip into your very worn Nike Monarchs.
    """
    
    s2 = ""

    return s1, s2


def rope():
    s1 = """
    A strong fibrous rope. You aren’t quite sure what it’s used for.
    """

    s2 = ""

    return s1, s2


def backpack():
    s1 = """
    The camping backpack you brought to Alaska.
    """

    s2 = ""

    return s1, s2


def anchor():
    s1 = """
    Seems important.
    Large heavy and connected by a thick chain. 
    """

    s2 = ""

    return s1, s2


def fishing_rod():
    s1 = """
    A fishing rod dedicated to deep sea fishing.
    It’s heavy and has many complicated levers.
    You should probably find an instructor to use it.
    """
    
    s2 = ""

    return s1, s2


def fishing_stations():
    s1 = """
    The captain sets both you and your friend up with the fishing stations.
    """

    s2 = """
    Your friend catches a flounder first.
    It’s a huge flounder, the captain shoots it
    and quickly throws it into the storage bellow.
    You catch a slightly smaller flounder.
    The captain just gaffs it and throws it into storage.
    You both safely return to Anchorage. 
    """

    return s1, s2


items = \
    ['Dad', 'dinner', 'framed photograph', 'music box',
     'phone', 'friend', 'shower', 'towel', 'soap', 'toothbrush', 'toothpaste',
     'sink',
     'rope', 'backpack']


helper_funcs = \
    [dad, dinner, photo, music_box,
     phone, friend, shower, towel, soap, toothbrush, toothpaste, sink,
     rope, backpack]
