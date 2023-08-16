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

box_x = 100
box2_x = 300

direction = 1
direction2 = 1

box_speed = 1
box_width = 50
wall_left = 0
wall_right = display[0] - box_width


wall_hit_count = 0  # Initialize wall hit counter

font = pygame.font.Font(None, 36)

def draw_box(x):
    pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (x, 100, box_width, 50))

def main():
    global box_x, box2_x, direction, direction2, wall_hit_count

    clock = pygame.time.Clock()


    X = np.float64(100)

    velocity = np.float64(50)

    time_ = np.float64(0)
    increment = np.float64(0.001)
    

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




        time_ += increment
        delta = increment * velocity
            




        if box_x + box_width >= box2_x:
            direction *= -1
            direction2 *= -1


        if direction2 == 1:  # Moving left
            box2_x -= delta
            if box2_x <= wall_left:
                box2_x = wall_left
                direction2 = -1
                sound.play()  # Play the sound
                wall_hit_count += 1  # Increment wall hit count
        else:  # Moving right
            box2_x += delta
            if box2_x >= wall_right:
                box2_x = wall_right
                direction2 = 1
                sound.play()
                wall_hit_count += 1


        if direction == 1:  # Moving left
            box_x -= delta
            if box_x <= wall_left:
                box_x = wall_left
                direction = -1
                sound.play()  # Play the sound
                wall_hit_count += 1  # Increment wall hit count
        else:  # Moving right
            box_x += delta
            if box_x >= wall_right:
                box_x = wall_right
                direction = 1
                sound.play()
                wall_hit_count += 1

        
        if frame_elapsed >= 1.0/60:
            frame_elapsed = 0

            display_surface = pygame.display.get_surface()
            display_surface.fill((0, 0, 0))

            draw_box(box_x)
            draw_box(box2_x)

        
            wall_hit_text = font.render(f'Wall Hits: {wall_hit_count}  box_x: {box_x:.2f} time: {time_:.2f} realtime: {current_time}', True, (255, 255, 255))
            display_surface.blit(wall_hit_text, (display[0] // 2 - wall_hit_text.get_width() // 2, display[1] - 50))

            pygame.display.flip()
            
        clock.tick(60)    

if __name__ == "__main__":
    main()
