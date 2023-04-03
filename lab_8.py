#paint
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
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
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
#racer
#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("data/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")
 
class Enemy(pygame.sprite.Sprite):
      def init(self):
        super().init() 
        self.image = pygame.image.load("data/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def init(self):
        super().init() 
        self.image = pygame.image.load("data/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('data/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
    #snake
    import pygame
import random
import time
res=800
size=50

x,y=random.randrange(0,res,size),random.randrange(0,res,size)
apple=random.randrange(0,res,size),random.randrange(0,res,size)
dris = {'W': True, 'S': True, 'A': True, 'D': True}
length=1
snake=[(x,y)] 
dx,dy=0,0
pygame.init()
screen=pygame.display.set_mode((res,res))
clock=pygame.time.Clock()
score=0
fps=5
game_over=False
pygame.mixer.init()  # initialize the mixer module
score_sound = pygame.mixer.Sound('data/smb_coin.wav')  # load the sound effect file
while not game_over:
    screen.fill(pygame.Color(0,154,255))
    [(pygame.draw.rect(screen,pygame.Color('green'), (i,j,size,size))) for i,j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size, size))
    
    x+=dx*size
    y+=dy*size
    snake.append((x,y))
    snake=snake[-length:]

    if snake[-1]==apple:
        apple=random.randrange(0,res,size), random.randrange(0,res,size)
        length+=1
        fps+=1
        score+=1
        score_sound.play()  # play the sound effect
    if x < 0 or x > res - size or y < 0 or y > res - size:
        game_over=True
    if len(snake) != len(set(snake)):
        game_over=True
    
    pygame.display.flip()
    clock.tick(fps)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

    key=pygame.key.get_pressed()
    if key[pygame.K_w] and dris['W']:
        dris = {'W': True, 'S': False, 'A': True, 'D': True}
        dx, dy = 0, -1
    if key[pygame.K_s] and dris['S']:
        dx, dy = 0, 1
        dris = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dris['A']:
        dx, dy = -1, 0
        dris = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dris['D']:
        dx, dy = 1, 0
        dris = {'W': True, 'S': True, 'A': False, 'D': True}

#...previous code...

if game_over:
    screen.fill(pygame.Color(0,154,255))
    font_go=pygame.font.SysFont('Times New Roman', 60)
    text_go=font_go.render('Game Over', True, pygame.Color('white'))
    screen.blit(text_go, (res/2 - text_go.get_width()/2, res/2 - text_go.get_height()/2))
    font_score=pygame.font.SysFont('Arial', 30)
    text_score=font_score.render('Final Score: ' + str(score), True, pygame.Color('white'))
    screen.blit(text_score, (res/2 - text_score.get_width()/2, res/2 + text_score.get_height()/2))
    pygame.mixer.init()
    game_over_sound = pygame.mixer.Sound('data/smb_gameover.wav')

    pygame.display.flip()
    game_over_sound.play()
    # Wait for 3 seconds before closing the game window
    time.sleep(3)

# End the Pygame module
pygame.quit()
