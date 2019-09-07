import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

screenSize = screenWidth, screenHeight = 200, 200
screen = pygame.display.set_mode(screenSize)
screen.fill(white)

pygame.draw.rect(screen, black,((50,50),(50,50)))

run = True
clock = pygame.time.Clock()
dt = 0
while run:
    dt += clock.tick(15)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    if dt >= 5000:
        run = False
    pygame.display.update()
