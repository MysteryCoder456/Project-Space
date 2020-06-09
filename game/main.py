import pygame


class Game:
    def __init__(self, w, h):
        self.width, self.height = w, h
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Project Space")
        self.background = pygame.Color("black")

    def update(self, dt):
        pass

    def render(self, window):
        window.fill(self.background)
        pygame.draw.rect(window, (255, 255, 255), (100, 100, 500, 500))
        pygame.display.update()
