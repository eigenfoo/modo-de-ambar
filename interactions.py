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


items = ['Dad', 'dinner', 'framed photograph', 'music box']
helper_funcs = [dad, dinner, photo, music_box]
