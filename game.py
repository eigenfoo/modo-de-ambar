import sys
import subprocess
from make_dungeons import (dungeon01, dungeon05, dungeon09, dungeon13,
                           dungeon02, dungeon06, dungeon10, dungeon14,
                           dungeon03, dungeon07, dungeon11, dungeon15,
                           dungeon04, dungeon08, dungeon12, dungeon16)
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)


Room.items = Bag()
bag = Bag()

possible_dungeons = [dungeon01, dungeon05, dungeon09, dungeon13,
                     dungeon02, dungeon06, dungeon10, dungeon14,
                     dungeon03, dungeon07, dungeon11, dungeon15,
                     dungeon04, dungeon08, dungeon12, dungeon16]


room11, room12, room13, room14, room15, room16, room17, room18, wait1, exit_dir1 = dungeon01()
room21, room22, room23, room24, room25, room26, room27, room28, wait2, exit_dir2 = dungeon02()
room31, room32, room33, room34, room35, room36, room37, room38, wait3, exit_dir3 = dungeon03()

win_room = Room("""
You win!
""")

last_rooms = [(room18, exit_dir1), (room28, exit_dir2), (room38, exit_dir3)]
waits = [wait1, wait2, wait3]
current_room = room11


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
        current_room = room
        say('You go {}.'.format(direction))
        look()
        if room in waits:
            set_context('wait.waiting')
        else:
            set_context('default')


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        bag.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = bag.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('bag')
def show_bag():
    if bag:
        say('You open your bag.')
        say('You have:')
        for thing in bag:
            say(thing)
    else:
        say('Your bag is empty!')


@when('cast', context='magic_aura', magic=None)
def cast(magic):
    if magic is None:
        say("Which magic you would like to spell?")


@when('wait', context='wait')
def wait():
    ''' FIXME note that sl is a requirement, but NOT a python requirement '''
    for i in range(3):
        subprocess.call(['sl'])

    global current_room
    if current_room == wait1:
        current_room = room21
        say('You find yourself in another dungeon.')
    elif current_room == wait2:
        current_room = room31
        say('You find yourself in another dungeon.')
    elif current_room == wait3:
        current_room = win_room
        say('You win!')
        sys.exit(0)

    set_context('default')


if __name__ == '__main__':
    look()
    print('')
    start()
