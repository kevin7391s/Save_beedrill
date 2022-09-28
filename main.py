
import sys
import pygame

pygame.init()

size = width, height = 640, 480
gravity = 2
speed = [0,gravity]
black = 0, 0, 0

bg_surface = pygame.image.load("assets/gamebackground.jpg")
smaller_image = pygame.transform.scale(bg_surface, (640,480))


game_active = True
ball_movement = 0

screen = pygame.display.set_mode(size)


ball = pygame.image.load("assets/bee.png")
ball = pygame.transform.scale(ball, (100,100))
ballrect = ball.get_rect()

clock = pygame.time.Clock()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed = [1, -3]


    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ballrect.bottom > height:
        speed = [0,0]

    ballrect.centery += ball_movement

    clock.tick(60)
    screen.fill(black)
    screen.blit(smaller_image, (0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()



