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
