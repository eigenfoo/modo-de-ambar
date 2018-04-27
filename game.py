import os
import sys
import subprocess
import time
from dungeons import dungeon01, dungeon02, dungeon03, dungeon04
import interactions
from adventurelib import (when, start, Room, Item, Bag,
                          say, set_context, get_context)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

Room.items = Bag()

bag = Bag([])

possible_dungeons = [dungeon01, dungeon02, dungeon03, dungeon04]

room11, room12, room13, room14, room15, room16, room17, room18, \
    wait1, exit_dir1 = dungeon01()
room21, room22, room23, room24, room25, room26, room27, room28, \
    wait2, exit_dir2 = dungeon02()
room31, room32, room33, room34, room35, room36, room37, room38, \
    wait3, exit_dir3 = dungeon03()
room41, room42, room43, room44, room45, room46, room47, room48, \
    wait4, exit_dir4 = dungeon04()

last_rooms = [(room18, exit_dir1), (room28, exit_dir2),
              (room38, exit_dir3), (room48, exit_dir4)]
waits = [wait1, wait2, wait3, wait4]

current_room = room11
current_settings = {'corpus': ['lyre'],
                    'learning_rate': ['1e-3'],
                    'loss_function': ['sc'],
                    'LFO_Rate': ['40']}


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
        ans = input("Are you sure? (yes/no) ")
        if ans == 'yes':
            if bag.num_items() > 2:
                print('')
                print('You may only take two items with you!')
                return

            subprocess.call(['sh', 'shell_scripts/kill_train.sh'])

            subprocess.Popen(['sh',
                              'shell_scripts/call_generate.sh',
                              current_settings['LFO_Rate'][0],
                              '1500'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=open('mini_canne/nil.txt'),
                             close_fds=True)
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
            s1, s2, update = interactions.helper_funcs[i]()
            current_settings[update[0]].insert(0, update[1])

            subprocess.call(['sh', 'shell_scripts/kill_train.sh'])
            subprocess.Popen(['sh', 'shell_scripts/call_train.sh',
                              current_settings['corpus'][0],
                              current_settings['learning_rate'][0],
                              'False',
                              current_settings['loss_function'][0]],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=open('mini_canne/nil.txt'),
                             close_fds=True)

            for line in s1.split('\n'):
                print('{}'.format(line))
                time.sleep(2)

            if s2:
                print('{}'.format(s2))
            else:
                print('You pick up the {}.'.format(item))
            bag.add(obj)
        else:
            raise Exception("Item missing from interactions.py!!")
    else:
        say('There is no {} here.'.format(item))


@when('drop THING')
def drop(thing):
    obj = bag.take(thing)
    if not obj:
        say('You do not have a {}.'.format(thing))
    else:
        i = interactions.items.index(obj.name)
        _, _, update = interactions.helper_funcs[i]()
        current_settings[update[0]].remove(update[1])

        subprocess.call(['sh', 'shell_scripts/kill_train.sh'])
        subprocess.Popen(['sh', 'shell_scripts/call_train.sh',
                          current_settings['corpus'][0],
                          current_settings['learning_rate'][0],
                          'False',
                          current_settings['loss_function'][0]],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=open('mini_canne/nil.txt'),
                         close_fds=True)
        if obj.name == 'dinner':
            say("""
            You drop the dinner plates off on the dining table.
            Your mother reaches for the remote control to turn off the TV.
            You have a couple more minutes before dinner starts.
            """)
        say('You drop the {}.'.format(obj))
        current_room.items.add(obj)


def brief_look():
    for line in str(current_room).split('\n'):
        print(line)
        time.sleep(1)
    print('')

    if current_room.items:
        for i in current_room.items:
            say('A \033[91m{}\033[0m is here.'.format(i))

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
    for line in current_room.desc.split('\n'):
        print(line)
        time.sleep(2)


@when('bag')
def show_bag():
    if bag:
        say('You open your bag.')
        say('You have:')
        for thing in bag:
            say(thing)
    else:
        say('Your bag is empty!')


@when('wait', context='wait')
def wait():
    # FIXME note that sl is a requirement, but NOT a python requirement
    subprocess.call(['sh', 'shell_scripts/kill_play.sh'])

    for _ in range(3):
        subprocess.call(['sl'])

    subprocess.Popen(['sh', 'shell_scripts/call_play.sh'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=open('mini_canne/nil.txt'),
                     close_fds=True)

    global current_room
    if current_room == wait1:
        current_room = room21
    elif current_room == wait2:
        current_room = room31
    elif current_room == wait3:
        current_room = room41
    elif current_room == wait4:
        current_room = room11

    subprocess.call(['clear'])
    say('You find yourself someplace else.')
    print('')
    brief_look()
    set_context('default')


if __name__ == '__main__':
    try:
        subprocess.Popen(['sh', 'shell_scripts/call_play.sh'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=open('mini_canne/nil.txt'),
                         close_fds=True)
        subprocess.Popen(['sh', 'shell_scripts/call_train.sh',
                          current_settings['corpus'][0],
                          current_settings['learning_rate'][0],
                          'False',
                          current_settings['loss_function'][0]],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=open('mini_canne/nil.txt'),
                         close_fds=True)

        os.system('clear')
        brief_look()
        print('')
        start()
    finally:
        # Kill all python processes to stop play, train and generate
        subprocess.call(['sh', 'shell_scripts/kill_play.sh'])
        subprocess.call(['sh', 'shell_scripts/kill_train.sh'])
        subprocess.call(['sh', 'shell_scripts/kill_generate.sh'])
