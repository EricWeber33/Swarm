import pygame
import random
import enemy
import player


window_width = 800
window_height = 600


def main():
    # pygame control vars
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    surface = pygame.display.get_surface()
    SPAWN = pygame.event.custom_type()
    pygame.time.set_timer(SPAWN, 3000)  # set timer
    game_over = False  # boolean for whether player has lost

    # seed random
    random.seed()

    # vars for a nest
    nest_radius = 25
    nest_offset = 50
    nest_color = (50, 50, 50)

    p = player.Player(pygame.mouse.get_pos(), surface)
    enemies = []  # list of all enemies of the player

    while not game_over:
        # get events
        events = pygame.event.get()

        for event in events:
            # quit event
            if event.type == pygame.QUIT:
                print("User exited")
                game_over = True
            # key events
            if event.type == pygame.KEYDOWN:
                # esc key event
                if event.key == pygame.K_ESCAPE:
                    print("uUser exited")
                    game_over = True

            # game events
            # spawn enemy event
            if event.type == SPAWN:
                # spawn new enemy randomly at one of the 4 nests
                random_x = random.randint(0, 1)
                random_y = random.randint(0, 1)
                if random_x == 0:
                    if random_y == 0:
                        e = enemy.Enemy((nest_offset, nest_offset), surface)
                        enemies.append(e)
                    else:
                        e = enemy.Enemy((nest_offset, window_height - nest_offset), surface)
                        enemies.append(e)
                else:
                    if random_y == 0:
                        e = enemy.Enemy((window_width - nest_offset, nest_offset), surface)
                        enemies.append(e)
                    else:
                        e = enemy.Enemy((window_width - nest_offset, window_height - nest_offset), surface)
                        enemies.append(e)

        window.fill((0, 0, 0))  # fill window
        # draw all nests
        pygame.draw.circle(surface, nest_color, (nest_offset, nest_offset), nest_radius)
        pygame.draw.circle(surface, nest_color, (window_width - nest_offset, nest_offset), nest_radius)
        pygame.draw.circle(surface, nest_color, (nest_offset, window_height - nest_offset), nest_radius)
        pygame.draw.circle(surface, nest_color, (window_width - nest_offset, window_height - nest_offset), nest_radius)

        # update player
        p.move(pygame.mouse.get_pos())
        p.draw()

        # for all enemies
        for e in enemies:
            e.move()
            e.draw()

            # if player is colliding with enemy game is over
            if p.collide(e):
                game_over = True

        pygame.display.update()  # updates window
        clock.tick(60)
    return 0


if __name__ == '__main__':
    main()
