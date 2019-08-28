# VERSION 1.1 - FINISHED
# 1. Add planet-black hole collisions - DONE
# 2. Add blue circle that always follows cursor - DONE
# 3. Change gravity physics - DONE

# VERSION 1.2 - FINISHED
# 1. Change gravity physics. Planets will now slow down if they are too close to a black hole. - DONE
# 2. Add gravity between planets. - DONE
# 3. Add collision between planets. - DONE

# VERSION 1.3
# 1. Improve collision algorithm. - DONE
# 2. Add realism to simulation - DONE
# 3. Make ISMO smaller - DONE

# VERSION 1.3.1
# 1. Minor tweaks in physics. - DONE


from random import randint
from uni_vars import *
from planet import Planet
from black_hole import BlackHole
import pygame

pygame.init()


def start():
    global running, clock, planets, black_holes, has_run, ox, oy
    running = True
    clock = pygame.time.Clock()
    planets = []
    black_holes = [BlackHole((width / 2, height / 2), 0, 0, 20, False, True)]
    has_run = False
    ox = 0
    oy = 0


def logic():
    global start_pos, has_run
    keys = pygame.key.get_pressed()
    m = pygame.mouse

    if m.get_pressed()[0]:
        if not has_run:
            global start_pos, ox, oy, new_pos
            start_pos = m.get_pos()
            ox = start_pos[0]
            oy = start_pos[1]
            has_run = True

    elif has_run:
        div = 50
        new_pos = m.get_pos()
        dx = ox - new_pos[0]
        dy = oy - new_pos[1]
        new_dir = math.atan2(dy, dx)
        new_speed = dist(ox, oy, new_pos[0], new_pos[1]) / div
        radius = randint(10, 20)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))

        new_planet = Planet((ox, oy), new_dir, new_speed, radius, color)
        planets.append(new_planet)

        has_run = False

    for p1 in planets:
        for p2 in planets:
            if p1 != p2:
                gravity(p1, p2)
                resolve_collision_circle(p1, p2)

        for bh in black_holes:
            gravity(bh, p1, bh.repulsive)

            d = dist(p1.x, p1.y, bh.x, bh.y)

            if d <= bh.imso:
                p1.apply_friction(friction)

            if bh.collision(p1):
                planets.remove(p1)

    for planet in planets:
        planet.update()

    for black_hole in black_holes:
        black_hole.update()


def render():
    win.fill(background)

    for planet in planets:
        planet.render()

    for black_hole in black_holes:
        black_hole.render()

    mouse = pygame.mouse.get_pos()
    r = 10

    pygame.draw.ellipse(win, (81, 175, 247), (mouse[0] - r, mouse[1] - r, r * 2, r * 2))

    pygame.display.update()


'''!!! no touching code below !!!'''


def main():
    global running

    start()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        logic()
        render()


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
