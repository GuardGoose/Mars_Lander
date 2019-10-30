Mars Lander Project 

One of the first arcade games to be based on a real space mission and using pseudo-realistic physics was Lunar Lander (Atari, 1979). The aim of this project is to create a similar application about landing on Mars.

In the game, players control a space vehicle as it makes its approach to the surface of the moon. By pressing various keyboard keys, the vehicle can be rotated right or left, or the main rocket engine fired (to decelerate the vehicle). Fuel is limited, so the player has to carefully manage use of the main engine. Points are scored by landing on various landing zones, but the vehicle must have horizontal and vertical velocity below certain acceptable limits or it is destroyed. Similarly, attempting to land outside a landing zone results in a crash. A successful landing triggers an award of points, and a new landing mission (with landing zones in new, random locations).

CONTROLS:

• Tilt Right (1 degree) = right-arrow key
• Tilt Left (1 degree) = left-arrow key
• Thrust = Spacebar

Description:

• The player as 3 lives.
• The player starts with 0% damage; 100% resulting in a crash and lost life
• The lander begins at a random position 1000m above the surface, it can wrap around the left and right of the screen, but it cannot go   any higher than the top of the screen
• Each lander has 500kf of rocket fuel, and each time the thrust (spacebar) is used it uses 5kg of rocket fuel
• When the thrust is used there's a small image to illustrate the it has been used
• Three landing pads are randomly generated on the map; if the lander misses then it will crash. If lander lands on a pad with             horizontal velocity (veloc_x) < 5.0 m/s and vertical velocity (veloc_y) < 5.0 m/s then the user is rewarded with 50 points and the       lander does not crash
• There are 5 randomly generated obstacles, if the lander collides with them it will undergo 25% damage
• During a mission, various instruments display flight data to the player. These are: time (mins:secs) since start of the mission; fuel   (kg); damage (%age); altitude (m); x-velocity (m/s); y-velocity (m/s). These are updated continuously in the top-left (instrument       panel) region of the main game screen.

The following equations are used for the small physics engine of the game:

veloc_xi+1 = veloc_xi + 0.33 x sin(-angle)

veloc_yi+1 = veloc_yi - 0.33 x cos(angle)

Gravity acts as a puller so when the lander is at rest it will begin its desent towards the surface at a rate of 0.1 m/s.

Issues:

• If the user crashes on the surface sometimes the game won't restart when the user presses spacebar to restart. 
• Sometimes the damange from collision can jump straight to 100%


The image collection used for the creation of this application belongs to the University of Aberdeen
