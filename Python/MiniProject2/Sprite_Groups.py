"""
This file has the sprite groups
"""

import pygame as pg
from random import randint
from Sprites import LandingPad, Obstacle


landing_pads = pg.sprite.Group()  # Creates a landing pad sprite group
# Sprite group makes it easier to manipulate all of them
# randint generates random location
pad1 = LandingPad('Sprites/pad.png', randint(200, 400), 720).add(landing_pads)
pad2 = LandingPad('Sprites/pad.png', randint(440, 700), 620).add(landing_pads)
pad3 = LandingPad('Sprites/pad_tall.png', randint(900, 1000), 650).add(landing_pads)


obstacles = pg.sprite.Group()  # Creates a obstacles sprite group
# Sprite group makes it easier to manipulate all of them
# randint generates random location
ob1 = Obstacle("Sprites/building_dome.png", randint(400, 600), 450).add(obstacles)
ob2 = Obstacle("Sprites/pipe_ramp_NE.png", randint(30, 400), 600).add(obstacles)
ob3 = Obstacle("Sprites/rocks_NW.png", randint(30, 500), 360).add(obstacles)
ob4 = Obstacle("Sprites/satellite_SE.png", randint(40, 80), 126).add(obstacles)
ob5 = Obstacle("Sprites/building_station_NE.png", randint(500, 700), 84).add(obstacles)
