from pygame.math import Vector2
from math import cos, sin

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        
        self.closest = None
    
    def cast(self, obstacle):
        direction = Vector2(cos(self.angle), sin(self.angle))
        posPlusdir = self.pos + direction
        
        x1, y1, x2, y2 = *obstacle.start, *obstacle.end
        x3, y3, x4, y4 = self.pos.x, self.pos.y, posPlusdir.x, posPlusdir.y
        
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None
        
        t = ( (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4) ) / denominator
        u = ( (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2) ) / denominator
        
        if 0 < t < 1 and u > 0:
            # Intersects!
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            
            return Vector2(x, y)
        
        return None    
    
    def draw(self, render_line, obstacles):
        closest_point = None
        closest_distance = float('inf')
        
        for obstacle in obstacles:
            point = self.cast(obstacle)
            
            if point:
                distance = self.pos.distance_squared_to(point)
                if distance < closest_distance:
                    closest_point = point
                    closest_distance = distance
            
        if closest_point:
            render_line(tuple(self.pos), tuple(closest_point))    