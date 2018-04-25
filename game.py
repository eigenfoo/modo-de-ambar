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

win_room = Room("You win!")

last_rooms = [(room18, exit_dir1), (room28, exit_dir2), (room38, exit_dir3)]
waits = [wait1, wait2, wait3]
current_room = room11


def yoshua_minigame():
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
        return True
    else:
        print('')
        say('''You leave him alone. Yoshua continues to stand, enraptured and
            trembling.''')
        return False


def yann_minigame():
    say('''Atop a reeking pile of garbage and linear algebra sits Yann Raccoon
        the Famished, scavenging for his next dinner, or next publishable
        theorem.''')
    say('''He catches sight of you, and stops his ferreting to stare.''')
    print('')
    ans = input('Do you offer him food? (y/N) ')
    print('')

    if ans == 'y':
        say('''Yann scampers down from the mountain of linear trash.''')
        say('''He is actually extremely clean and hygienic, and very much
            despises the fact that he needs to rummage to find his meals.''')
        say('''As a gesture of gratitude and goodwill, he offers you a strange
            clockwork mechanism that he found in the pile.''')
        return True
    else:
        say('''You walk away in disgust. Yann continues his incessant
            scrouging.''')
        return False


def geoffrey_minigame():
    say('''Geoffrey Pinch-one the Miserly huddles over his treasure chest.''')
    say('''As you approach, he sniffs and snorts in indignant surprise, as if
        you had interrupted something.''')
    say('''His expression quickly turns to one of guilt and remorse.''')
    say('''He offers to leave you his treasure chest if you allow him to go on
        his way.''')
    print('')
    ans = input('Do you accept his offer? (y/N) ')

    if ans == 'y':
        s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit' \
            if randint(0, 1) == 1 \
            else 'Integer vestibulum aliquet orci ac pulvinar'

        print('')
        say('''You inspect the treasure chest closely.''')
        say('''It is locked.''')
        say('''But wait... there is an inscription on the padlock.''')
        print('')
        say('Press any key to examine the inscription.')
        ans = input('')
        print(s)
        print('')

        timeout = 5
        t = Timer(timeout, print, ['\n\nTimes up!'])
        t.start()
        ans = input('Quick! Reproduce the inscription! ')
        t.cancel()

        if ans == s:
            say('The treasure chest clicks open.')
            return True
        else:
            say('''You are unsuccessful. Geoffrey creeches in gleeful joy.''')
            return False
    else:
        print('')
        say('''You decline. Geoffrey snorts in disdain, and continues to huddle
            over his chest.''')
        return False


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
    try:
        proc = subprocess.Popen(['sh', 'train.sh'],
                                stdin=None,
                                stdout=None,
                                stderr=open('mini_canne/nil.txt'),
                                close_fds=True)
        os.system('clear')
        brief_look()
        print('')
        start()
    finally:
        proc.kill()
