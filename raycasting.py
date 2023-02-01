import pgzrun
from random import randint
import pygame
from math import pi

import imageio
import time

from objects.obstacle import Obstacle
from objects.source import Source

TITLE = '2D RayCasting'
WIDTH = 800 + 200
HEIGHT = 600 + 200
transparent_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

GIF_DURATION = 5 # seconds
RAYS_STEP = 2 * pi / 180


# Simulation variables
recorder = None
mouse_pos = (WIDTH // 2, HEIGHT // 2)
source = Source(RAYS_STEP)
default_obstacles = [
    Obstacle((-20, -20), (WIDTH + 20, -20)),
    Obstacle((-20, HEIGHT + 20), (WIDTH + 20, HEIGHT + 20)),
    Obstacle((-20, -20), (-20, HEIGHT + 20)),
    Obstacle((WIDTH + 20, -20), (WIDTH + 20, HEIGHT + 20)),
]
obstacles = []


def update():
    if not obstacles:
        generate_random_obstacles()
    
    source.set_pos(mouse_pos)
    
    if recorder:
        frame = pygame.surfarray.array3d(transparent_surface).swapaxes(0,1)
        recorder.append_data(frame)
    
def draw():
    screen.clear()
    transparent_surface.fill('black')
    
    # Rays
    source.draw(
        lambda s, e: pygame.draw.line(transparent_surface, (255, 255, 0, 250), s, e)
        , obstacles)    
    
    # Obstacles
    for obstacle in obstacles:
        obstacle.draw(
            lambda s, e: pygame.draw.line(transparent_surface, (255, 255, 255), s, e, 2)
        )
        

    screen.blit(transparent_surface, (0, 0))
    
    if recorder:
        screen.draw.filled_circle((20, 20), 10, (255, 0, 0))
    else:
        screen.draw.text('PRESS C TO RECORD\n' +
                         'PRESS R TO RESET OBSTACLES', pos=(20, 20), color='gray', fontsize=16)
    
def on_mouse_move(pos):
    global mouse_pos, recorder
    mouse_pos = pos  
    
def on_key_down(key):
    global GIF_DURATION, recorder
    if key == keys.R:
        # reset
        generate_random_obstacles()
    
    if key == keys.C and not recorder:
        # Capture Screen 
        recorder = imageio.get_writer(f'records/simulation_{int(time.time())}.gif', mode='I')
        clock.schedule_unique(stop_record, GIF_DURATION)
        

def stop_record():
    global recorder
    if recorder:
        recorder.close()
    recorder = None               

def generate_random_obstacles(n=8):
    global default_obstacles, obstacles
    obstacles.clear()
    obstacles.extend(default_obstacles)
    for _ in range(n):
        obstacles.append(Obstacle(
            (randint(0, WIDTH), randint(0, HEIGHT)),
            (randint(0, WIDTH), randint(0, HEIGHT))
        ))

pgzrun.go()