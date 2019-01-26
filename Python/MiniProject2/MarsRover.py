"""
This is the MarsRover class, which has all the fucntions for the
rover.
"""

import sys
import pygame as pg  # Imports pygame as pg for clarity when used.
from pygame import *
from random import randint, random, uniform  # Imports select functions from random
from math import sin, cos, radians  # Imports select functions from math

pg.init()  # Initiates pygame

# Font is comic sans because that's the only font that should be used.
mars_font = pg.font.SysFont("comicsansms", 15)
alert_font = pg.font.SysFont("comicsansms", 35)
crash_font = pg.font.SysFont("comicsansms", 35)
screen = pg.display.set_mode((1200, 750))  # Sets the display screen
pg.event.set_blocked(MOUSEMOTION)  # Mouse button cannot be used

FPS = 60  # Sets FPS
WIDTH = 1200  # Sets WIDTH
HEIGHT = 720  # Sets HEIGHT
game_clock = pg.time.Clock()  # Sets game clock


class MarsRover(pg.sprite.Sprite):
    """Houses all the functions for the MarsRover"""
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)  # Loads image file of sprite
        self.rect = self.image.get_rect()  # Creates a rectangle around the image
        self.rect.left, self.rect.top = location  # Spawn location
        self.speed_y = random()
        self.speed_x = uniform(-1, 1)
        self.lives = 3  # Number of lives
        self.rotated_image = self.image  # Saves a copy of the sprite to be rotated
        self.fuel = 500  # Sets fuel amount
        self.damage = 0  # Sets damage amount
        self.angle = 0  # Sets angle for rotation

    def mars_game_over(self):
        """Tells the game when game is over"""
        return self.lives < 1

    def gravity(self):
        """Defines the gravity for the game"""
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.speed_y += 0.1

    def engine(self):
        """This is the engine used for thrust when the player wants to move"""
        self.speed_x += 0.33 * sin(radians(-self.angle))
        self.speed_y -= 0.33 * cos(radians(self.angle))
        self.fuel -= 5

    def reset_stats(self):
        """When the rover crashes all stats are reset and rover respwans"""
        self.rect.top = 0
        self.speed_y = random()
        self.speed_x = uniform(-1, 1)
        self.rotated_image = self.image
        self.fuel = 500
        self.damage = 0
        self.angle = 0

    def positions(self):
        """
        Allows the rover to wrap around the screen,
        and crash if at the bottom
        """
        if self.rect.bottom > HEIGHT:  # If the lander is at the bottom of the screen
            MarsRover.crashed()  # Calls the crashed function
            pg.time.wait(60)  # Waits 10 milliseconds
            pg.event.clear()  # Clears event so the user can press a button
            event = pg.event.wait()  # Waits for event to happen
            if event.type == QUIT:  # Still gives the user an option to quit
                pg.quit()  # Quits pygame
                sys.exit()  # Exits the system
            elif event.type == KEYDOWN:  # Event = when user presses a button
                rover.lives -= 1  # Takes away one life
                rover.reset_stats()  # Resets the stats and respawns
        # Two if statements below allow the rover to wrap around the screen
        if self.rect.left >= WIDTH:
            self.rect.left = 0
        if self.rect.right <= 0:
            self.rect.right = WIDTH
        if self.rect.top < 0:  # Prevents it from going past the top
            self.rect.top = 0
            self.speed_y = 0

    def move_left(self):
        """Allows the rover to be rotated left"""
        self.angle += 1  # Adds one to angle to rotate left
        self.rotated_image = pg.transform.rotate(self.image, self.angle)

    def move_right(self):
        """Allows the rover to be rotated right"""
        self.angle -= 1  # Adds one to angle to rotate right
        self.rotated_image = pg.transform.rotate(self.image, self.angle)

    def landing_condition(self):
        """Checks the landing conditions of the rover"""
        return self.fuel > 0 and self.damage < 100

    def check_landing_speed(self):
        """Checks the landing speed of the rover"""
        return -5 < self.speed_x < 5 and self.speed_y < 5

    @staticmethod
    def crashed():
            crash = crash_font.render("YOU HAVE CRASHED", 1, (255, 0, 0))
            crash_rect = crash.get_rect(center=(WIDTH / 2, HEIGHT / 2))  # Displays centre screen
            screen.blit(crash, crash_rect)

    def damage_taken(self):
        """Function adds damage"""
        if self.damage < 100:
            self.damage += 25

    @staticmethod
    def key_disable():
        """
        Static method as it takes no input
        This method is working but it just doesn't
        last long enough
        """
        disabled_period = 1000000000 # 2 seconds in milliseconds
        timer = 0  # Timer is set to 0
        alarm = alert_font.render("ALERT", False, (255, 0, 0))  # Alert message in red
        x = randint(0, 7400)  # Generates random numbers
        if x < 25:  # If x is less than 25
            timer += 1  # Timer adds one
            if timer <= disabled_period:  # If the timer is less than the disables period
                screen.blit(alarm, (74, 100))  # Displays alarm message
                return 1  # Returns 1 to disable left_movement
        if 26 < x <= 75:
            timer += 1  # Timer adds one
            if timer <= disabled_period:  # If the timer is less than the disables period
                screen.blit(alarm, (74, 100))  # Displays alarm message
                return 2  # Returns 2 to disable right_movement
        if 76 < x <= 125:
            timer += 1  # Timer adds one
            if timer <= disabled_period:  # If the timer is less than the disables period
                screen.blit(alarm, (74, 100))  # Displays alarm message
                return 3  # Returns 3 to disable right_movement
        else:  # Otherwise returns true
            return True


rover = MarsRover("lander.png", [randint(0, 1120), 0])  # The Rover

