import pygame
from game.main import Game


def main():
    pygame.init()
    g = Game(1024, 768)

    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        g.update(clock.get_time())
        g.render(g.win)


if __name__ == "__main__":
    main()
