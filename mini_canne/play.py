import sys
from mini_canne import *
import os
import pygame
import time


def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)
    pygame.init()
    pygame.mixer.music.load('loop.wav')
    pygame.mixer.music.play(-1)
    time.sleep(6000)


if __name__ == '__main__':
    main()
