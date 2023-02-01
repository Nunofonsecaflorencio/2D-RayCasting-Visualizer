class Obstacle:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, render):
        render(self.start, self.end)