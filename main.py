import sys

import pygame
import locals as loc
from terrain import ter


def cord_to_screen_cord(cord: tuple[int, int, int], tot_layers) -> (float, float):
    """ Returns the coordinates on screen of the image"""
    return (loc.X_VEC * cord[0] + loc.Z_VEC * cord[1] + loc.Y_VEC * (tot_layers - cord[2])) * loc.IMG_SIZE + loc.OFFSET


def main():
    """ base of the project"""
    pygame.init()
    display = pygame.display.set_mode((900, 900))
    clock = pygame.time.Clock()

    images = {
        loc.BLOCK: pygame.transform.scale(
            pygame.image.load("resources/block.png"), (loc.IMG_SIZE, loc.IMG_SIZE)
        ).convert_alpha(),
        loc.H_BLOCK: pygame.transform.scale(
            pygame.image.load("resources/h_block.png"), (loc.IMG_SIZE, loc.IMG_SIZE)
        ).convert_alpha()
    }

    running = True
    while running:
        [sys.exit() for event in pygame.event.get() if event.type == pygame.QUIT]

        display.fill((100, 100, 100))
        for y, plane in enumerate(ter):
            for z, line in enumerate(plane):
                for x, el in enumerate(line):
                    if el in images:
                        display.blit(
                            images[el],
                            images[el].get_rect(topleft=cord_to_screen_cord((x, z, y), len(ter)))
                        )

        pygame.display.flip()
        clock.tick(loc.MAX_FPS)
        pygame.display.set_caption(str(clock.get_fps()))


if __name__ == "__main__":
    main()
