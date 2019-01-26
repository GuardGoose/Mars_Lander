"""
This is all the Sprite classes
"""


import pygame as pg
from MarsRover import MarsRover
from random import randint
pg.init()


mars_font = pg.font.SysFont("comicsansms", 15)
alert_font = pg.font.SysFont("comicsansms", 35)
crash_font = pg.font.SysFont("comicsansms", 35)

FPS = 60
WIDTH = 1200
HEIGHT = 720
game_clock = pg.time.Clock()

rover = MarsRover("Sprites/lander.png", [randint(0, 1120), 0])


class Sprite(pg.sprite.Sprite):
    """Main sprite file from which the others inherit from"""
    def __init__(self, image_file, left, top):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pg.image.load(image_file)  # Load image file
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top


class Background(Sprite):
    """Background image"""
    def __init__(self, image_file, left, top):
        super().__init__(image_file, left, top)


class Thrust(Sprite):
    """Thrust class"""
    def __init__(self, image_file, left, top):
        super().__init__(image_file, left, top)
        self.image_rotated = self.image  # Stores the image that is rotated

    def rotated(self):
        """Rotates the sprite"""
        self.image_rotated = pg.transform.rotate(self.image, rover.angle)


class LandingPad(Sprite):
    """Landing pad sprite"""
    def __init__(self, image_file, left, top):
        super().__init__(image_file, left, top)


class Obstacle(Sprite):
    """Obstacle class"""
    def __init__(self, image_file, left, top):
        super().__init__(image_file, left, top)
