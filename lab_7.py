#3 task
import pygame
pygame.init()
W = 500
H = 400

s = pygame.display.set_mode((W, H))
x = W // 2
y = H // 2
speed = 20

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
FPS = 60
clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_DOWN:
                y += speed
            elif event.key == pygame.K_UP:
                y -= speed

    s.fill(white)
    pygame.draw.circle(s, red, (x, y), 25)
    pygame.display.update()
    clock.tick(FPS)
#1 task
import pygame
import os
from datetime import datetime

pygame.init()

SIZE = [500, 500]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Clock")

clock = pygame.image.load(os.path.abspath("images/clock.png")).convert_alpha()
long_arrow = pygame.image.load(os.path.abspath("images/arrow.png")).convert_alpha()
long_arrow = pygame.transform.rotate(long_arrow, 0)
secondsAngle = 0
minutesAngle = 0
hoursAngle = 0
running = True
dt = datetime.now()


def getSecondsArrow(angle, clock_rect, surface):
    m = pygame.transform.scale(long_arrow, (30, 180))
    arrRect = m.get_rect()
    surface.blit(m, (surface.get_rect().width / 2 - arrRect.width / 2, 0))

    surface = pygame.transform.rotate(surface, -angle)
    backRec = surface.get_rect()

    backRec.center = clock_rect.center

    screen.blit(surface, backRec)


def getMinutesArrow(angle, clock_rect, surface):
    m = pygame.transform.scale(long_arrow, (30, 150))
    arrRect = m.get_rect()
    surface.blit(m, (surface.get_rect().width / 2 - arrRect.width / 2, 25))

    surface = pygame.transform.rotate(surface, -angle)
    backRec = surface.get_rect()

    backRec.center = clock_rect.center

    screen.blit(surface, backRec)


while running:
    pygame.time.Clock().tick(1)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    dt = datetime.now()

    secondsAngle = dt.second * 6
    minutesAngle = dt.minute * 6
    hoursAngle = dt.hour * 10

    # Draw an image
    # clock
    clock = pygame.transform.scale(clock, (400, 400))
    clock_rec = clock.get_rect()
    clock_rec.center = screen.get_rect().center
    screen.blit(clock, clock_rec)

    # seconds
    secSurface = pygame.Surface((60, 320), pygame.SRCALPHA)

    getSecondsArrow(secondsAngle, clock_rec, secSurface)

    # minutes
    minSurface = pygame.Surface((60, 320), pygame.SRCALPHA)
    getMinutesArrow(minutesAngle, clock_rec, minSurface)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
#2 task
import pygame
import os

pygame.init()
SIZE = [500, 500]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Player")

playlist = [
    os.path.abspath("pythonProject/1575509633_nf-paid-my-dues.mp3")
]

running = True


class Player:
    def __init__(self, currSong=0, isPlaying=True):
        self.currSong = currSong
        self.isPlaying = isPlaying

    def startNewSong(self, path: str):
        pygame.mixer.music.load("1575509633_nf-paid-my-dues.mp3")
        pygame.mixer.music.play()

    def unPause(self):
        pygame.mixer.music.unpause()
        self.isPlaying = True

    def pause(self):
        pygame.mixer.music.pause()
        self.isPlaying = False

    def forward(self):
        if self.currSong < len(playlist) - 1:
            self.currSong += 1
        self.startNewSong(playlist[self.currSong])

    def backward(self):
        if self.currSong == 0:
            self.currSong = 0
        else:
            self.currSong -= 1
        self.startNewSong(playlist[self.currSong])

    def drawPlayButton(self):
        playButton = pygame.image.load(os.path.abspath("playbutton.jpg"))
        playButton = pygame.transform.scale(playButton, (100, 100))
        return playButton

    def drawForwardAndBackwardBtns(self):
        forward = pygame.image.load(os.path.abspath("forwardbutton.jpg"))
        backward = pygame.image.load(os.path.abspath("backbutton.jpg"))
        forward = pygame.transform.scale(forward, (100, 100))
        backward = pygame.transform.scale(backward, (100, 100))
        return backward, forward


player = Player(0, True)
player.startNewSong(playlist[0])

backwardBtn, forwardBtn = player.drawForwardAndBackwardBtns()
playBtn = player.drawPlayButton()
font = pygame.font.SysFont("Arial", 16)

while running:
    pygame.time.Clock().tick(10)

    screen.fill((255, 255, 255))
    playBtnC = screen.blit(playBtn, ((screen.get_width() / 2 - 50), 300))
    backwardBtnC = screen.blit(backwardBtn, ((screen.get_width() / 2 - 50 - 100 - 50), 300))
    forwardBtnC = screen.blit(forwardBtn, ((screen.get_width() / 2 - 50 + 100 + 50), 300))

    songTitle = font.render(playlist[player.currSong].replace("/Users/zulqa/pythonProject"
                                                               "", ""), True, (0, 0, 0))
    screen.blit(songTitle, ((screen.get_width() / 2 - songTitle.get_width() // 2), 100))

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.isPlaying:
                    player.pause()
                else:
                    player.unPause()
            if event.key == pygame.K_RIGHT:
                player.forward()
            if event.key == pygame.K_LEFT:
                player.backward()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if playBtnC.collidepoint(pos):
                if player.isPlaying:
                    player.pause()
                else:
                    player.unPause()
            if forwardBtnC.collidepoint(pos):
                player.forward()
            if backwardBtnC.collidepoint(pos):
                player.backward()

pygame.quit()
