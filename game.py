import pygame

class Game:
    width: int; height: int;
    size: tuple[int, int]
    screen: pygame.surface
    running: bool


    def __init__(self, width = 1280, height = 720):
        pygame.init()
        self.running = True
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        
    
    def debug(self):
        print("Debugging")

    def run(self):
        while running:
            pass
    
    def quit(self):
        running = False
