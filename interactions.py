from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)

def dad():
    s1 = """
    Your dad chastises you for standing around, taking up space in the kitchen.
    He tells you to take the three plated dishes out to the dining room.
    """

    s2 = " "

    return s1, s2


items = ['Dad']
helper_funcs = [dad]
