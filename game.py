import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
x = 10
y = 10

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y-=5
    if pressed[pygame.K_s]:
        y+=5
    if pressed[pygame.K_a]:
        x-=5
    if pressed[pygame.K_d]:
        x+=5
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
