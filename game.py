import os
import sys
import subprocess
from threading import Timer
from random import randint
from dungeons import (dungeon01, dungeon05, dungeon09, dungeon13,
                      dungeon02, dungeon06, dungeon10, dungeon14,
                      dungeon03, dungeon07, dungeon11, dungeon15,
                      dungeon04, dungeon08, dungeon12, dungeon16)
import interactions
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)


Room.items = Bag()

food = Item('food')
food.level = 10
bag = Bag([food])

possible_dungeons = [dungeon01, dungeon05, dungeon09, dungeon13,
                     dungeon02, dungeon06, dungeon10, dungeon14,
                     dungeon03, dungeon07, dungeon11, dungeon15,
                     dungeon04, dungeon08, dungeon12, dungeon16]


room11, room12, room13, room14, room15, room16, room17, room18, \
    wait1, exit_dir1 = dungeon16()
room21, room22, room23, room24, room25, room26, room27, room28, \
    wait2, exit_dir2 = dungeon03()
room31, room32, room33, room34, room35, room36, room37, room38, \
    wait3, exit_dir3 = dungeon06()

win_room = Room("""
You win!
""")

last_rooms = [(room18, exit_dir1), (room28, exit_dir2), (room38, exit_dir3)]
waits = [wait1, wait2, wait3]
current_room = room11


@when('forward', direction='north')
@when('back', direction='south')
@when('left', direction='east')
@when('right', direction='west')
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)

    if get_context() == 'wait.waiting':
        say('You must wait!')
        return

    if (current_room, direction) in last_rooms:
        say('You are about to leave this dungeon.')
        ans = input("Are you sure? (y/N) ")
        if ans == 'y':
            pass
        else:
            say('You choose not to leave just yet.')
            return

    if room:
        os.system('clear')
        current_room = room
        say('You go {}.'.format(direction))
        brief_look()
        if room in waits:
            set_context('wait.waiting')
        else:
            set_context('default')


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)

    if obj:
        if obj.name in interactions.items:
            i = interactions.items.index(obj.name)
            s1, s2 = interactions.helper_funcs[i]()
            say('{}'.format(s1))
            if s2:
                print('')
                say('{}'.format(s2))
            else:
                say('You pick up the {}.'.format(item))
            bag.add(obj)
        else:
            raise Exception("Item missing from interactions.py!!")
    else:
        say('There is no {} here.'.format(item))


@when('drop THING')
def drop(thing):
    if thing == 'food':
        say('You drop a food pack.')
        food = bag.find('food')
        food.level -= 1
        current_room.items.add(Item('food pack'))
        return

    obj = bag.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        if obj.name == 'dinner':
            say("""
            You drop the dinner plates off on the dining table.
            Your mother reaches for the remote control to turn off the TV.
            You have a couple more minutes before dinner starts.
            """)
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


def brief_look():
    say(current_room)
    print('')

    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)

    if 'north' in current_room.exits():
        print('      N\n      ^\n      |')
    else:
        print('\n\n\n')
    if 'west' in current_room.exits():
        sys.stdout.write('W < - o')
    else:
        sys.stdout.write('      o')
    if 'east' in current_room.exits():
        sys.stdout.write(' - > E')
    sys.stdout.write('\n')
    sys.stdout.flush()
    if 'south' in current_room.exits():
        print('      |\n      v\n      S')
    else:
        print('\n\n\n')


@when('look')
def look():
    say(current_room.desc)
    print('')


@when('bag')
def show_bag():
    if bag:
        say('You open your bag.')
        say('You have:')
        for thing in bag:
            if thing.name == 'food':
                food = bag.find('food')
                say('food: x{}'.format(food.level))
            else:
                say(thing)
    else:
        say('Your bag is empty!')


@when('wait', context='wait')
def wait():
    ''' FIXME note that sl is a requirement, but NOT a python requirement '''
    for i in range(2):
        subprocess.call(['sl'])

    global current_room
    if current_room == wait1:
        current_room = room21
        say('You find yourself in another dungeon.')
        brief_look()
    elif current_room == wait2:
        current_room = room31
        say('You find yourself in another dungeon.')
        brief_look()
    elif current_room == wait3:
        current_room = win_room
        brief_look()
        say('You win!')
        sys.exit(0)

    set_context('default')


if __name__ == '__main__':
    os.system('clear')
    brief_look()
    print('')
    start()
