# @Author: Brandon Baars <brandon>
# @Date:   Saturday, June 24th 2017, 3:25:47 pm
# @Filename: Pygame.py
# @Last modified by:   brandon
# @Last modified time: Monday, June 26th 2017, 11:06:29 pm

import pygame


def checkCollision(x, y, treasureX, treasureY):
    """Check to see if there is a collsion of the passed objects."""
    global screen

    collisionState = False

    # checks from player moving upward (head)
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True
        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True
    # checks from player moviing down on the treasure. (tail)
    # the coordinates are from top left of player, that's why we need
    # to add 40 (player height) and 35 (player width)
    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            y = 650
            collisionState = True
        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True

    return collisionState, y


# calling the init function
pygame.init()

# an object inside pygame where we set mode to the size of the window
screen = pygame.display.set_mode((900, 700))

finished = False

# postion on the x axis
x = 450 - 35/2

# position on the y axis
y = 650

# add in our player image and convert the size to 30px by 30px
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (35, 40))
playerImage = playerImage.convert_alpha()

# add in our enemy images and convert the size
enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (35, 40))
enemyImage = enemyImage.convert_alpha()

# add in our background image
backgroundImage = pygame.image.load("background.png")
backgroundImage = \
    pygame.transform.scale(backgroundImage, (900, 700))
screen.blit(backgroundImage, (0, 0))

# load our treasure image
treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35, 40))
treasureImage = treasureImage.convert_alpha()
treasureX = 450 - 35/2
treasureY = 50
collisionTreasure = False
screen.blit(treasureImage, (treasureX, treasureY))

# enemy positons
enemyX = 100
enemyY = 570
movingRight = True
collisionEnemy = False
name = ""

enemies = [(enemyX, enemyY, movingRight)]
enemyNames = {0: 'Max', 1: 'Brandon', 2: 'Diana', 3: 'Britt', 4: 'Jon'}

# add text to the game
font = pygame.font.SysFont("comicsans", 70)

# Level Counter
level = 1

# add a frame rate
frame = pygame.time.Clock()

while not finished:

    # takes care of all the events going on
    for event in pygame.event.get():

        # checks if the window is closed (i.e red 'x' is pressed)
        if event.type == pygame.QUIT:
            finished = True

    # check if a certain key is pressed (returns the pressed keys)
    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_SPACE] == 1:
        y -= 5

    # fill the screen with black before moving our player
    screen.blit(backgroundImage, (0, 0))

    # draw on our player and treasure at the x , y position
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (x, y))

    enemyIndex = 0
    # checks for all enemies on the map
    for enemyX, enemyY, movingRight in enemies:

        if enemyX >= 800 - 35:
            movingRight = False
        elif enemyX <= 100:
            movingRight = True

        if movingRight:
            enemyX += 5 * level
        else:
            enemyX -= 5 * level

        # update our enemy, add to the screen and check for collision
        enemies[enemyIndex] = (enemyX, enemyY, movingRight)
        screen.blit(enemyImage, (enemyX, enemyY))
        collisionEnemy, y = checkCollision(x, y, enemyX, enemyY)

        if collisionEnemy:
            name = enemyNames[enemyIndex]
            collisionText = \
                font.render("You were killed by " + name,
                            True, (0, 0, 0))
            screen.blit(collisionText, (450 - collisionText.get_width()
                        / 2, 350 - collisionText.get_height() / 2))
            pygame.display.flip()
            pygame.event.pump()
            frame.tick(1)

        enemyIndex += 1

    # returns to us whether or not there was a collision and the y value
    collisionTreasure, y = checkCollision(x, y, treasureX, treasureY)

    if collisionTreasure:
        level += 1

        # add a new enemy that is shifted relatvie to the level
        enemies.append((enemyX - 50 * level, enemyY - 50 * level, False))
        textWin = \
            font.render("You've reached level " + str(level),
                        True, (0, 0, 0))

        screen.blit(textWin, (450 - textWin.get_width() / 2,
                    350 - textWin.get_height() / 2))
        pygame.display.flip()

        # ensure the program can internally interact
        pygame.event.pump()
        frame.tick(1)

    # need to update our display after we've drawn our rectangle
    pygame.display.flip()

    # Set frame rate to 1/30th of a second
    frame.tick(30)
