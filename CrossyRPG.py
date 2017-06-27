import pygame


def checkCollision(x,y,treasureX,treasureY):
    global screen,textWin
    collisionState = False
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX+35:
            y = 650
            collisionState = True
            
        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True
            
    elif y + 40 >= treasureY and y + 40<= treasureY + 40:
        if x >= treasureX and x<= treasureX+35:
            y = 650
            collisionState = True
            
        elif x+35 >= treasureX and x+35 <= treasureX + 35:
            y = 650
            collisionState = True
    return collisionState, y
pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False # 0 < 10 - > True/ 10<10 ->False
x = 450-35/2
y = 650
#if state/condition == True:
#    code
#index = [0,1,2,3, 4]
#array = [0,1.2,4.5,"Hello"]
#print(array[-2])
#print pygame.K_SPACE
playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage, (35,40))
playerImage = playerImage.convert_alpha()

backgroundImage = pygame.image.load("ground.png")
backgroundImage = pygame.transform.scale(backgroundImage,(900,700))
screen.blit(backgroundImage,(0,0))

treasureImage = pygame.image.load("Treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35,40))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("Enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(35,40))
enemyImage = enemyImage.convert_alpha()

treasureX = 450 - 35/2
treasureY = 50

enemyX = 100
enemyY = 580-10

screen.blit(treasureImage,(treasureX,treasureY))

font = pygame.font.SysFont("comicsans",70)
level = 1

#dictionary = {Key:Value,
#              Key2:Value2}

enemyNames = {0:"Max",1:"Jill",2:"Greg",3:"Diane"}
#enemyNames[0] -> "Max"

frame = pygame.time.Clock()
collisionTreasure = False
collisionEnemy = False
movingRight = True
name = ""
enemies = [(enemyX,enemyY,movingRight)]#(enemyX,enemyY,movingRight)

while finished == False: #While our game is not finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pressedKeys = pygame.key.get_pressed()
                #[...,UP,DOWN,LEFT,SPACE,...]
    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies:
        if enemyX >= 800-35:
            movingRight = False
        elif enemyX <= 100:
            movingRight = True
        if movingRight == True:
            enemyX += 5*level
        else:
            enemyX -= 5*level
        enemies[enemyIndex] = (enemyX,enemyY,movingRight)
        enemyIndex += 1
    if pressedKeys[pygame.K_SPACE] == 1:
        y -= 5 #= y - 5 
    #rectOne = pygame.Rect(x,y,30,30)#x,y,width,height

    color = (0,0,255) #R,G,B
    white = (255,255,255) #R,G,B
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(x,y))

    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies:
        screen.blit(enemyImage,(enemyX,enemyY))
        collisionEnemy,y = checkCollision(x,y,enemyX,enemyY)
        if collisionEnemy == True:
            name = enemyNames[enemyIndex]
            textLose = font.render("You were killed by "+name,True,(255,0,0))
            screen.blit(textLose,(450 - textLose.get_width()/2,350 - textLose.get_height()/2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(30)
        enemyIndex += 1
        
    collisionTreasure,y = checkCollision(x,y,treasureX,treasureY)
    #collisionEnemy,y = checkCollision(x,y,enemyX,enemyY)
    if collisionTreasure == True:
        level += 1                                    #str(1) -> "1"
        enemies.append((enemyX-50*level,enemyY-50*level,False))
        textWin = font.render("You've reached level "+str(level),True,(0,0,0))
        screen.blit(textWin,(450 - textWin.get_width()/2,350 - textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
    #elif collisionEnemy == True:
        
        
    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip()
    frame.tick(30)
    
            
