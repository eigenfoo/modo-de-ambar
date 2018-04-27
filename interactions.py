from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)


def dad():
    s1 = """
    Your dad chastises you for standing around, taking up space in the kitchen.
    He tells you to take the three plated dishes out to the dining room.
    """

    s2 = " "

    update = ('corpus', 'didgeridoo')

    return s1, s2, update


def dinner():
    s1 = """
    As you pick up the plate, you notice that the beef
    has been cooked so well that it practically falls off the bone.
    Your mouth waters.
    """

    s2 = ""

    update = ('learning_rate', '1e-5')

    return s1, s2, update


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

    update = ('LFO_Rate', '10')

    return s1, s2, update


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

    update = ('corpus', 'lyre')

    return s1, s2, update


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

    update = ('corpus', 'guitar')

    return s1, s2, update


def friend():
    s1 = """
    You decide to wake up your friend.
    You need an early start to get the most out of exploring Kyoto today.
    """

    s2 = " "

    update = ('LFO_Rate', '80')

    return s1, s2, update


def shower():
    s1 = """
    You spend 15 minutes in the shower.
    """

    s2 = "You feel refreshed."

    update = ('LFO_Rate', '40')

    return s1, s2, update


def towel():
    s1 = """
    A common white bath towel.
    There is nothing special about it.
    """

    s2 = ""

    update = ('loss_function', 'mae')

    return s1, s2, update


def soap():
    s1 = """
    Common bar soap.
    There is nothing special about it,
    except for the slight fragrance of lavender.
    """

    s2 = ""

    update = ('learning_rate', '1e-4')

    return s1, s2, update


def toothbrush():
    s1 = """
    A small travel sized toothbrush.
    """

    s2 = ""

    update = ('loss_function', 'mse')

    return s1, s2, update


def toothpaste():
    s1 = """
    A small tube of travel sized toothpaste.
    """

    s2 = ""

    update = ('learning_rate', '1e-6')

    return s1, s2, update


def sink():
    s1 = """
    You take 2 minutes to brush your teeth.
    This is not the electric toothbrush you are used to.
    Your hand feels slightly out of shape.
    """

    s2 = "You finish brushing your teeth."

    update = ('LFO_Rate', '100')

    return s1, s2, update


def shoes():
    s1 = """
    You slip into your very worn Nike Monarchs.
    """

    s2 = ""

    update = ('LFO_Rate', '40')

    return s1, s2, update


def rope():
    s1 = """
    A strong fibrous rope. You aren’t quite sure what it’s used for.
    """

    s2 = ""

    update = ('loss_function', 'sc')

    return s1, s2, update


def backpack():
    s1 = """
    The camping backpack you brought to Alaska.
    """

    s2 = ""

    update = ('corpus', 'cello')

    return s1, s2, update


def anchor():
    s1 = """
    Seems important.
    Large heavy and connected by a thick chain.
    """

    s2 = ""

    update = ('learning_rate', '1e-3')

    return s1, s2, update


def fishing_rod():
    s1 = """
    A fishing rod dedicated to deep sea fishing.
    It’s heavy and has many complicated levers.
    You should probably find an instructor to use it.
    """

    s2 = ""

    update = ('loss_function', 'mse')

    return s1, s2, update


def fishing_station():
    s1 = """
    The captain sets both you and your friend up with the fishing station.
    """

    s2 = """
    Your friend catches a flounder first.
    It’s a huge flounder, the captain shoots it
    and quickly throws it into the storage bellow.
    You catch a slightly smaller flounder.
    The captain just gaffs it and throws it into storage.
    You both safely return to Anchorage.
    """

    update = ('corpus', 'guitar')

    return s1, s2, update


def pen():
    s1 = """
    Grandma hands you her Porsche pen. The pen is heavy  
    and warm where she held it. Stainless 
    steel spokes twist around its body. You fill in 
    53 Across: 
    P-I-K-M-I-N
    """

    s2 = ""

    update = ('corpus', 'didgeridoo')

    return s1, s2, update


def small_painting():
    s1 = """
    The painting depicts a young girl standing in a garden. 
    She has long red curls and bright red blush 
    on both cheeks. She dangles a teddy bear by the arm 
    with her right hand. She stares at you with a quizzical look.
    """

    s2 = ""

    update = ('LFO_Rate', '200')

    return s1, s2, update


items = \
    ['Dad', 'dinner', 'framed photograph', 'music box',
     'phone', 'friend', 'shower', 'towel', 'soap', 'toothbrush', 'toothpaste',
     'sink', 'pair of shoes',
     'rope', 'backpack', 'anchor', 'fishing rod', 'fishing station',
     'pen', 'small painting']


helper_funcs = \
    [dad, dinner, photo, music_box,
     phone, friend, shower, towel, soap, toothbrush, toothpaste, sink, shoes,
     rope, backpack, anchor, fishing_rod, fishing_station,
     pen, small_painting]
