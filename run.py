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
            if event.type == pygame.MOUSEBUTTONDOWN:
                g.mouse_down(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                g.mouse_up(event.pos)

        g.update(clock.get_time() / 1000)
        g.render(g.win)


if __name__ == "__main__":
    main()
