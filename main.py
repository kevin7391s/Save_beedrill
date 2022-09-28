
import sys
import pygame

pygame.init()

# screen size
size = width, height = 640, 480

# speed for bee
gravity = 2
speed = [0, gravity]

# variable for moving clouds
x = 5
y = -500

game_active = True


# define clouds image
cloud_surface = pygame.image.load("assets/clouds.png")
cloud_surface = pygame.transform.scale(cloud_surface, (850, 300))
cloudrect = cloud_surface.get_rect()

second_cloud_surface = pygame.image.load("assets/clouds.png")
second_cloud_surface = pygame.transform.scale(cloud_surface, (850, 300))


# define screen background
bg_surface = pygame.image.load("assets/gamebackground.jpg")
smaller_image = pygame.transform.scale(bg_surface, (640,480))


# define bee image
ball = pygame.image.load("assets/bee.png")
ball = pygame.transform.scale(ball, (100,100))
ballrect = ball.get_rect()



screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
left_push = True

# MAIN GAME LOOP
while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        # User input controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed = [0, -3]
            if event.key == pygame.K_LEFT and left_push:
                left_push = False
                ball = pygame.transform.flip(ball, True, False)
            if event.key == pygame.K_LEFT:
                speed = [-2, 0]






    ballrect = ballrect.move(speed)

    # boundaries for bee image
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ballrect.bottom > height:
        speed = [0,0]


    # controls game speed
    clock.tick(60)

    # displays everything on screen
    screen.blit(smaller_image, (0,0))
    x += .5
    if x == 850:
        x = -850
    y += .5
    if y == 850:
        y = -850
    screen.blit(cloud_surface, (x, 0), cloudrect)
    screen.blit(second_cloud_surface, (y, 0))
    screen.blit(ball, ballrect)
    pygame.display.update()
    pygame.display.flip()





