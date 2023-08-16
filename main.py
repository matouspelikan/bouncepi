import numpy as np
import time
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF)

# Initialize Pygame mixer
pygame.mixer.init()
sound = pygame.mixer.Sound('hit.wav')  # Load a sound file

box_x = 150
box2_x = 300

direction = 1
direction2 = 1

box_speed = 1
box_width = 50
wall_left = 0
wall_right = display[0] - box_width


wall_hit_count = 0  # Initialize wall hit counter

font = pygame.font.Font(None, 36)

def draw_box(x, hit):
    color = (255, 255, 255)
    if hit:
        color = (255, 10, 10)
    pygame.draw.rect(pygame.display.get_surface(), color, (x, 100, box_width, 50))

def main():
    global box_x, box2_x, direction, direction2, wall_hit_count

    clock = pygame.time.Clock()


    X = np.float64(100)

    v = np.float64(0)
    v = np.longdouble(0)
    v2 = np.float64(10)
    v2 = np.longdouble(10)

    time_ = np.float64(0)
    increment = np.float64(0.0001)

    m = np.float64(1)
    m2 = np.float64(1000000)
    

    current_time = time.time()
    last_time = current_time
    frame_elapsed = np.float64(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            quit()

        current_time = time.time()
        elapsed = current_time - last_time
        # print(elapsed)
        last_time = current_time
        frame_elapsed += elapsed






            



        hit = False
        if box_x + box_width >= box2_x:
            hit = True
            # print((direction, direction2, v, v2))

            wall_hit_count += 1
            sound.play()

            direction *= -1
            direction2 *= -1

            vN = v*((m-m2)/(m+m2)) + v2*((2*m2)/(m+m2))
            v2N = v*((2*m)/(m+m2)) + v2*((m2-m)/(m+m2))

            v = vN
            v2 = v2N

            # print((v, v2))

            # print((direction, direction2, v, v2))

        time_ += increment
        delta = increment * v
        delta2 = increment * v2


        if v2 > 0:  # Moving left
            box2_x -= delta2
            if box2_x <= wall_left:
                hit = True
                box2_x = wall_left
                direction2 = -1
                v2 *= -1
                sound.play()  # Play the sound
                wall_hit_count += 1  # Increment wall hit count
        else:  # Moving right
            box2_x -= delta2
            if box2_x >= wall_right:
                hit = True
                box2_x = wall_right
                direction2 = 1
                v2 *= -1
                sound.play()
                wall_hit_count += 1


        if v > 0:  # Moving left
            box_x -= delta
            if box_x <= wall_left:
                hit = True
                box_x = wall_left
                direction = -1
                v *= -1
                sound.play()  # Play the sound
                wall_hit_count += 1  # Increment wall hit count
        else:  # Moving right
            box_x -= delta
            if box_x >= wall_right:
                hit = True
                box_x = wall_right
                direction = 1
                v *= -1
                sound.play()
                wall_hit_count += 1

        
        if frame_elapsed >= 1.0/60 or hit:
            frame_elapsed = 0

            display_surface = pygame.display.get_surface()
            display_surface.fill((0, 0, 0))


            draw_box(box_x, hit)
            draw_box(box2_x, False)

        
            wall_hit_text = font.render(f'Wall Hits: {wall_hit_count}', True, (255, 255, 255))
            display_surface.blit(wall_hit_text, (display[0] // 2 - wall_hit_text.get_width() // 2, display[1] - 50))

            pygame.display.flip()
            # clock.tick(60) 

if __name__ == "__main__":
    main()
