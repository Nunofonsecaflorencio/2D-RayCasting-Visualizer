from pygame.math import Vector2
from math import pi
from .ray import Ray

class Source:
    def __init__(self, step):
        self.pos = Vector2()
        self.create_rays(step)
    
    def create_rays(self, step):
        self.rays = []
        angle = 0
        while angle < 2 * pi:
            self.rays.append(Ray(self.pos, angle))
            angle += step    
        
    def set_pos(self, pos):
        self.pos.x = pos[0]
        self.pos.y = pos[1]
        
    def draw(self, render_line, obstacles):
        for ray in self.rays:
            ray.draw(render_line, obstacles)