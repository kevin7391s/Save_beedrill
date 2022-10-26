
import sys
import pygame

pygame.init()

# screen size
size = width, height = 640, 480

# speed for bee
gravity = 3
speed = [0, gravity]

# variable for moving clouds
x = 5
y = -500

game_active = True

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# define bugspray image
spray_surface = pygame.image.load("assets/bugspray.png").convert()
spray_surface = pygame.transform.scale(spray_surface, (320,400))
spray_rect = spray_surface.get_rect(bottom = height)

# define clouds image
cloud_surface = pygame.image.load("assets/clouds.png")
cloud_surface = pygame.transform.scale(cloud_surface, (850, 300))
cloud_rect = cloud_surface.get_rect()

# define screen background
bg_surface = pygame.image.load("assets/gamebackground.jpg")
bg_surface = pygame.transform.scale(bg_surface, (640,480))

# define bee_surface image
bee_surface = pygame.image.load("assets/bee.png")
bee_surface = pygame.transform.scale(bee_surface, (100,100))
bee_rect = bee_surface.get_rect()


left_push = True
right_push = True

# MAIN GAME LOOP
while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        # User input controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed = [1, -3]
            if event.key == pygame.K_LEFT and left_push:
                left_push = False
                right_push = True
                bee_surface = pygame.transform.flip(bee_surface, True, False)
            if event.key == pygame.K_LEFT:
                speed = [-2, 0]
            if event.key == pygame.K_RIGHT and right_push and not left_push:
                right_push = False
                left_push = True
                bee_surface = pygame.transform.flip(bee_surface, True, False)
            if event.key == pygame.K_RIGHT:
                speed = [2, 0]
            if event.key == pygame.K_DOWN:
                speed = [0,2]
            if event.key == pygame.K_UP:
                speed = [0,-2]

    bee_rect = bee_rect.move(speed)

    # boundaries for bee_surface image
    if bee_rect.left < 0 or bee_rect.right > width:
        speed[0] = -speed[0]
    if bee_rect.top < 0:
        speed[1] = -speed[1]
    if bee_rect.bottom > height:
        speed = [0,0]

    # controls game speed
    clock.tick(60)

    # control spray movement

    # displays everything on screen
    screen.blit(bg_surface, (0,0))

    screen.blit(cloud_surface, cloud_rect)
    screen.blit(bee_surface, bee_rect)
    screen.blit(spray_surface, spray_rect)
    pygame.display.update()
    pygame.display.flip()
