import sys
from pygame import *
from Sprites import *
from Sprite_Groups import obstacles, landing_pads

pg.init()  # Initialises pygame

# Comic Sans is the only font that should be used
mars_font = pg.font.SysFont("comicsansms", 15)
alert_font = pg.font.SysFont("comicsansms", 35)
crash_font = pg.font.SysFont("comicsansms", 35)

FPS = 60  # Sets FPS
WIDTH = 1200  # Sets WIDTH
HEIGHT = 720  # Sets HEIGHT
game_clock = pg.time.Clock()  # Sets game clock

pg.event.set_blocked(MOUSEMOTION)  # User cannot use the mouse
screen = pg.display.set_mode((1200, 750))  # Sets screen size
rover = MarsRover("Sprites/lander.png", [randint(0, 1120), 0])  # Sets the rover
BackGround = Background('Sprites/mars_background_instr.png', 0, 0)  # Sets the background image
pg.display.set_caption("Mars Lander")  # Sets caption
game_score = 0  # Sets game_score to zero

while not rover.mars_game_over():
    game_clock.tick(FPS)  # Sets game clock to FPS
    screen.fill([255, 255, 255])  # Creates a blank white screen
    screen.blit(BackGround.image, BackGround.rect)  # Puts the background image on the screen
    landing_pads.draw(screen)  # Draws the landing pads to the screen
    obstacles.draw(screen)  # Draws the obstacles to the screen
    screen.blit(rover.rotated_image, rover.rect)   # Displays the rover

    my_clock = pg.time.get_ticks() / 1000  # Divides by 1000 to display the clock in seconds
    my_time = mars_font.render(' {:.1f}'.format(my_clock), False, (255, 255, 255))  # Renders the time
    my_fuel = mars_font.render(" {}".format(rover.fuel), False, (255, 255, 255))  # Renders amount of fuel
    my_damage = mars_font.render(str(rover.damage), False, (255, 255, 255))  # Renders the damage
    altitude = mars_font.render("{:.1f}".format(1000 * (1 - (rover.rect.top / HEIGHT))), False, (255, 255, 255))  # Renders altitude
    x_velocity = mars_font.render("{:.1f}".format(rover.speed_x), False, (255, 255, 255))  # Renders x_velocity
    y_velocity = mars_font.render("{:.1f}".format(rover.speed_y), False, (255, 255, 255))  # Renders y_velocity
    my_score = mars_font.render("{}".format(game_score), False, (255, 255, 0))  # Renders my_score

    # Below displays all the correct stats in the instrument panel
    screen.blit(my_time, (74, 12))
    screen.blit(my_fuel, (74, 32))
    screen.blit(my_damage, (100, 57))
    screen.blit(altitude, (269, 14))
    screen.blit(x_velocity, (310, 37))
    screen.blit(y_velocity, (310, 60))
    screen.blit(my_score, (74, 85))

    # Mains game loop
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()  # Exits pygame
            sys.exit()  # Closes the program
    landing_pad_collision = pg.sprite.spritecollideany(rover, landing_pads)  # If the rover collides with the landing pad
    obstacle_collision = pg.sprite.spritecollideany(rover, obstacles)  # If the rover collides with the sprite
    if landing_pad_collision:  # If a landing pad collision happens
        # Below checks the speed and damage of the rover to see if it's a crash or not
        if rover.landing_condition() and rover.rect.left > landing_pad_collision.rect.left and rover.rect.right \
                <= landing_pad_collision.rect.right and rover.check_landing_speed():
            game_score += 50  # Plus 50 to the score if it's not a crash
            rover.reset_stats()  # Respawns rover.
        else:
            MarsRover.crashed()  # Calls the crashed function
            pg.time.wait(10)  # Waits 10 milliseconds
            pg.event.clear()  # Clears event so the user can press a button
            event = pg.event.wait()  # Waits for event to happen
            if event.type == QUIT:  # Still gives the user an option to quit
                pg.quit()  # Quits pygame
                sys.exit()  # Exits the system
            elif event.type == KEYDOWN:  # Event = when user presses a button
                rover.lives -= 1  # Takes away one life
                rover.reset_stats()  # Resets the stats and respawns
                landing_pads.draw(screen)  # Puts everything in new place
                obstacles.draw(screen)  # Puts everything in a new place

    if obstacle_collision:  # If the rover collides with a obstacle
        MarsRover.damage_taken(rover)  # Calls the damage_taken function

    keys_pressed = pg.key.get_pressed()  # When the user presses a key
    # If rover still has fuel and less than 100% damage, then the user
    # can still move it around
    if rover.fuel > 0 and rover.damage < 100:
        MarsRover.key_disable()  # Calls the key_disable function to randomly turn off keys
        # If key_pressed is true and key_disabled is not 1
        if keys_pressed[pg.K_LEFT] and MarsRover.key_disable() is not 1:
            rover.move_left()  # Calls the move_left function to rotate the rover
        # If key_pressed is true and key_disabled is not 2
        if keys_pressed[pg.K_RIGHT] and MarsRover.key_disable() is not 2:  # If both are True
            rover.move_right()
        # If key_pressed is true and key_disabled is not 3
        if keys_pressed[pg.K_SPACE] and MarsRover.key_disable() is not 3:  # If both are True
            thrust = Thrust('Sprites/thrust.png', rover.rect.left + 31, rover.rect.bottom - 12)
            thrust.rotated()  # Calls the rotate function
            rover.engine()  # Calls the engine function
            screen.blit(thrust.image_rotated, thrust.rect)  # Displays the rotated image
            pg.display.update()  # Updates the screen

    pg.display.update()  # Updates the screen

    rover.gravity()  # Calls the gravity function on the rover
    rover.positions()  # Calls the positions on the rover
    pg.display.flip()  # Flips display
