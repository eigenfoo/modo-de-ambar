import os
import sys
import subprocess
from random import randint
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


room11, room12, room13, room14, room15, room16, room17, room18, \
        wait1, exit_dir1 = dungeon01()
room21, room22, room23, room24, room25, room26, room27, room28, \
        wait2, exit_dir2 = dungeon02()
room31, room32, room33, room34, room35, room36, room37, room38, \
        wait3, exit_dir3 = dungeon03()

win_room = Room("""
You win!
""")

last_rooms = [(room18, exit_dir1), (room28, exit_dir2), (room38, exit_dir3)]
waits = [wait1, wait2, wait3]
current_room = room11


@when('take yoshua')
def yoshua_minigame():
    obj = current_room.items.take('yoshua')
    say('''In the far corner of the cavernous room, you spy Yoshua
        Better-than-you, First Lord and High Wizard of Mila.''')
    say('''He stands trembling, his arms spread out and his eyes fixed to the
        vaulted ceilings.''')
    say('He appears to be in pain.')
    print('')
    ans = input('Do you call out to him? (y/N) ')

    if ans == 'y':
        print('')
        say('''The Wizard howls in anguish as his spell wisps away into the
            air.''')
        say('''Infuriated that you have interrupted his incantations, he threatens
            you with his staff.''')
        print('')
        say('Press any key to engage in battle!')
        input('')
        roll = randint(0, 2)
        # FIXME add functionality here: change number of dungeons.
        if roll == 0:
            say('You lose!')
        elif roll == 1:
            say('You tie.')
        elif roll == 2:
            say('You win!')
        bag.add(obj)
        return
    else:
        print('')
        say('''You leave him alone. Yoshua continues to stand, enraptured and
            trembling.''')
        return


@when('take yann')
def yann_minigame():
    obj = current_room.items.take('yann')
    say('''Geoffrey Pinch-one the Miserly huddles over his treasure chest.''')
    say('''As you approach, he sniffs and snorts in indignant surprise, as if
        you had interrupted something.''')
    say('''His expression quickly turns to one of guilt and remorse''')
    say('''He offers to leave you his treasure chest if you allow him to go on
        his way.''')
    print('')
    ans = input('Do you accept his offer? (y/N) ')

    if ans == 'y':
        s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit' \
            if randint(0, 1) == 1 else 'Integer vestibulum aliquet orci ac pulvinar'

        print('')
        say('''You inspect the treasure chest closely.''')
        say('''It is locked.''')
        say('''But wait... there is an inscription on the padlock.''')
        print('')
        say('Press any key to examine the inscription.')
        ans = input('')
        print(s)
        print('')
        ans = input('Quick! Reproduce the inscription! ')
        if ans == s:
            say('The treasure chest clicks open.')
            bag.add(obj)
            return
        else:
            say('''You are unsuccessful. Geoffrey creeches in gleeful joy.''')
            return
    else:
        print('')
        say('''You decline. Geoffrey snorts in disdain, and continues to huddle
            over his chest.''')
        return


@when('take geoffrey')
def geoffrey_minigame():
    obj = current_room.items.take('geoffrey')
    say('''Geoffrey Pinch-one the Miserly huddles over his treasure chest.''')
    say('''As you approach, he sniffs and snorts in indignant surprise, as if
        you had interrupted something.''')
    say('''His expression quickly turns to one of guilt and remorse''')
    say('''He offers to leave you his treasure chest if you allow him to go on
        his way.''')
    print('')
    ans = input('Do you accept his offer? (y/N) ')

    if ans == 'y':
        s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit' \
            if randint(0, 1) == 1 else 'Integer vestibulum aliquet orci ac pulvinar'

        print('')
        say('''You inspect the treasure chest closely.''')
        say('''It is locked.''')
        say('''But wait... there is an inscription on the padlock.''')
        print('')
        say('Press any key to examine the inscription.')
        ans = input('')
        print(s)
        ans = input('Quick! Reproduce the inscription! ')
        if ans == s:
            say('The treasure chest clicks open.')
            bag.add(obj)
            return
        else:
            say('''You are unsuccessful. Geoffrey creeches in gleeful joy.''')
            return
    else:
        print('')
        say('''You decline. Geoffrey snorts in disdain, and continues to huddle
            over his chest.''')
        return


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
        if obj == 'spare tire':
            say('You think this will help to make your vehicle faster.')
            bag.add(obj)
        elif obj == 'scroll':
            say('You are possessed by a sense of loss...')
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
    os.system('clear')
    look()
    print('')
    start()
