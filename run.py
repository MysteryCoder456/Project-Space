import pygame
from game.main import Game


def main():
    pygame.init()
    g = Game(1024, 768)
    clock = pygame.time.Clock()
    fps = 60

    while True:
        dt = clock.tick(fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                g.mouse_down(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                g.mouse_up(event.pos)

        g.update(dt)
        g.render(g.win)


if __name__ == "__main__":
    main()
