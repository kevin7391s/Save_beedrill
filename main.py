
import sys
import pygame

pygame.init()

# screen size
size = width, height = 1280, 960

# speed for bee
gravity = 2
speed = [0, 0]

# variable for moving clouds
x = 5
y = -500

game_active = True

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# define bugspray
spray_surf = pygame.image.load("assets/bugspray.png").convert_alpha()
spray_surf = pygame.transform.scale(spray_surf, (80, 300))
spray_rect = spray_surf.get_rect(bottom = height, left = width)

# define clouds
cloud_surf = pygame.image.load("assets/clouds.png")
cloud_surf = pygame.transform.scale(cloud_surf, (width, height/2))
cloud_rect = cloud_surf.get_rect()

# define screen background
bg_surf = pygame.image.load("assets/gamebackground.jpg")
bg_surf = pygame.transform.scale(bg_surf, size)

# define bee
bee_surf = pygame.image.load("assets/bee.png")
bee_surf = pygame.transform.scale(bee_surf, (150,100))
bee_rect = bee_surf.get_rect()


left_push = True
right_push = True

# MAIN GAME LOOP
while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        # User input controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity -= 3
                speed = [1, gravity]
            if event.key == pygame.K_LEFT and left_push:
                left_push = False
                right_push = True
                bee_surf = pygame.transform.flip(bee_surf, True, False)
            if event.key == pygame.K_LEFT:
                speed = [-2, gravity]
            if event.key == pygame.K_RIGHT and right_push and not left_push:
                right_push = False
                left_push = True
                bee_surf = pygame.transform.flip(bee_surf, True, False)
            if event.key == pygame.K_RIGHT:
                speed = [2, gravity]
            if event.key == pygame.K_DOWN:
                gravity += 2
                speed = [0, gravity]
            if event.key == pygame.K_UP:
                gravity -= 2
                speed = [0, gravity]

    bee_rect = bee_rect.move(speed)

    # apply gravity to bee
    gravity +=1
    bee_rect.y = gravity
    if bee_rect.bottom >= height: bee_rect.bottom = height

    # boundaries for bee_surf image
    if bee_rect.left < 0: bee_rect.left = 0

    if bee_rect.right > width: bee_rect.right = width
    # if bee_rect.top < 0:
    #     speed[1] = -speed[1]
    # if bee_rect.bottom > height:
    #     speed = [0,0]

    # controls game speed
    clock.tick(60)

    # control spray movement

    if spray_rect.right <= 0:
        spray_rect.left = width
    else:
        spray_rect.left -= 5

    # displays everything on screen
    screen.blit(bg_surf, (0,0))

    screen.blit(cloud_surf, cloud_rect)
    screen.blit(bee_surf, bee_rect)
    screen.blit(spray_surf, spray_rect)
    pygame.display.update()
    pygame.display.flip()
