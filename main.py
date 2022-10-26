
import sys
import pygame

pygame.init()

# screen size
size = width, height = 1280, 960

# speed for bee
gravity = 2
speed = [0, gravity]
seconds = 0

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

#if bee_rect.height


left_push = True
right_push = True

# MAIN GAME LOOP
while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        # User input controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # gravity -= 30
                if 0 < bee_rect.x > 0:
                    seconds = 0
                    seconds /= 5
                    speed = [speed_value, -6]
                    speed_value /= 2
                else:
                    speed_value = 0

                    seconds = 0
                    seconds /= 5
                    speed = [0, -6]


            if event.key == pygame.K_LEFT and left_push:
                left_push = False
                right_push = True
                bee_surf = pygame.transform.flip(bee_surf, True, False)
            if event.key == pygame.K_RIGHT and right_push and not left_push:
                right_push = False
                left_push = True
                bee_surf = pygame.transform.flip(bee_surf, True, False)

            if event.key == pygame.K_LEFT:
                speed_value = -4
                seconds = 0
                seconds /= 5
                speed = [speed_value, 0 + gravity]

            if event.key == pygame.K_RIGHT:
                speed_value = 4
                seconds = 0
                seconds /= 5
                speed = [3, 0 + gravity]

            if event.key == pygame.K_DOWN:
                #gravity += 20
                speed_value = 0
                speed = [0, 3]

            if event.key == pygame.K_UP:
                if 0 < bee_rect.x > 0:
                    gravity = 0
                    seconds = 0
                    seconds /= 5
                    speed = [speed_value, -6]
                    speed_value /= 2
                else:
                    speed_value = 0
                    gravity = 0
                    seconds = 0
                    seconds /= 5
                    speed = [0, -6]
                #gravity -= 20

    bee_rect = bee_rect.move(speed)

    height_value = bee_rect.y


    # apply gravity to bee
    seconds += 1
    gravity = 2 * seconds /50
    gravity = round(gravity)
    if seconds > 50:
        speed = [0, gravity]
    if seconds > 50 and 0 < bee_rect.x > 0:
        speed = [speed_value, gravity]
    print(bee_rect.x)



    #bee_rect.y = gravity
    #if bee_rect.bottom >= height:
        #bee_rect.bottom = speed[0, 1]

    # boundaries for bee_surf image
    if bee_rect.left < 0: bee_rect.left = 0

    if bee_rect.right > width: bee_rect.right = width
    if bee_rect.top < 0:
        speed[1] = -speed[1]
    if bee_rect.bottom > height:
        gravity = 0
        speed = [0,0]

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
