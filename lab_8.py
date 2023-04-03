'''import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count = 3




def terminate() :
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey() :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :  # escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies) :
    for b in baddies :
        if playerRect.colliderect(b['rect']) :
            return True
    return False


def drawText(text, font, surface, x, y) :
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

# fonts
font = pygame.font.SysFont(None, 30)

# sounds
gameOverSound = pygame.mixer.Sound('00258.mp3')
pygame.mixer.music.load('00258.mp3')
laugh = pygame.mixer.Sound('00258.mp3')

# images
playerImage = pygame.image.load('image/car1.png')
car3 = pygame.image.load('image/car3.png')
car4 = pygame.image.load('image/car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('image/car2.png')
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('image/left.png')
wallRight = pygame.image.load('image/right.png')

# "Start" screen
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0
if not os.path.exists("data/save.dat") :
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()
while (count > 0) :


    # start of the game
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True :  # the game loop
        score += 1  # increase score

        for event in pygame.event.get() :
            class Coin(pygame.sprite.Sprite):
                def __init__(self, x, y):
                    super().__init__()
                    # self.image = pygame.image.load('coin.png').convert_alpha()
                    self.rect = self.image.get_rect(center=(x, y))


            class Road:
                def __init__(self):
                    # other code here
                    self.coins = []

                def add_coin(self):
                    x = random.randint(0, WINDOWWIDTH)
                    y = random.randint(0, WINDOWHEIGHT)
                    coin = Coin(x, y)
                    self.coins.append(coin)


            class Game:
                def __init__(self):
                    # other code here
                    self.add_coin_event = pygame.USEREVENT + 1
                    pygame.time.set_timer(self.add_coin_event, 3000)  # change this interval as per your preference

                def run(self):
                    # other code here
                    while self.running:
                        # other code here
                        for event in pygame.event.get():
                            # other code here
                            if event.type == self.add_coin_event:
                                self.road.add_coin()
            if event.type == QUIT :
                terminate()

            if event.type == KEYDOWN :
                if event.key == ord('z') :
                    reverseCheat = True
                if event.key == ord('x') :
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a') :
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w') :
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s') :
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP :
                if event.key == ord('z') :
                    reverseCheat = False
                    score = 0
                if event.key == ord('x') :
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE :
                    terminate()

                if event.key == K_LEFT or event.key == ord('a') :
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveRight = False
                if event.key == K_UP or event.key == ord('w') :
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s') :
                    moveDown = False

        # Add new baddies at the top of the screen
        if not reverseCheat and not slowCheat :
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE :
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect' : pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect' : pygame.Rect(0, 0, 126, 600),
                        'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface' : pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect' : pygame.Rect(497, 0, 303, 600),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)

        # Move the player around.
        if moveLeft and playerRect.left > 0 :
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH :
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0 :
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT :
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in baddies :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        for b in baddies[:] :
            if b['rect'].top > WINDOWHEIGHT :
                baddies.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)

        windowSurface.blit(playerImage, playerRect)

        for b in baddies :
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if playerHasHitBaddie(playerRect, baddies) :
            if score > topScore :
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break

        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)
    if (count == 0) :
        laugh.play()
        drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()'''

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()