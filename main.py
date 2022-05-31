import sys

import pygame
import locals as loc
from terrain import ter


def cord_to_screen_cord(cord: tuple[int, int, int] or list[float, float, float], tot_layers) -> (float, float):
    """ Returns the coordinates on screen of the image"""
    return (loc.X_VEC * cord[0] + loc.Z_VEC * cord[1] + loc.Y_VEC * (tot_layers - cord[2])) * loc.IMG_SIZE + loc.OFFSET


def main():
    """ base of the project"""
    pygame.init()
    display = pygame.display.set_mode((900, 900))
    clock = pygame.time.Clock()

    block_images = {
        loc.BLOCK: pygame.transform.scale(
            pygame.image.load("resources/block.png"), (loc.IMG_SIZE, loc.IMG_SIZE)
        ).convert_alpha(),
        loc.H_BLOCK: pygame.transform.scale(
            pygame.image.load("resources/h_block.png"), (loc.IMG_SIZE, loc.IMG_SIZE)
        ).convert_alpha()
    }

    sprite_image = pygame.transform.scale(
            pygame.image.load("resources/ball.png"), (loc.IMG_SIZE, loc.IMG_SIZE)
        ).convert_alpha()

    sliding = ""
    tot_slided = 0
    player_pos: list[int, int, int] = [2, 2, 1]  # For x, z and y respectivly

    def can_go(direction: str) -> bool:
        """ tells the number of tiles the player has (if it can) move in a direction"""
        vec = pygame.Vector2(
            1 if direction == "E" else -1 if direction == "W" else 0,
            1 if direction == "N" else -1 if direction == "S" else 0
        )

    running = True
    while running:
        [sys.exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        pressed_keys = pygame.key.get_pressed()

        was_sprite_displayed = False

        display.fill((100, 100, 100))
        for y, plane in enumerate(ter):
            for z, line in enumerate(plane):
                for x, el in enumerate(line):
                    if el in block_images:
                        display.blit(
                            block_images[el],
                            block_images[el].get_rect(topleft=cord_to_screen_cord((x, z, y), len(ter)))
                        )
                    if [x, z, y] == player_pos:
                        display.blit(
                            sprite_image,
                            sprite_image.get_rect(
                                topleft=cord_to_screen_cord((x, z, y), len(ter)) + loc.Y_PLAYER_VEC * loc.IMG_SIZE
                            )
                        )
                        was_sprite_displayed = True
        if not was_sprite_displayed:
            display.blit(
                sprite_image,
                sprite_image.get_rect(
                    topleft=cord_to_screen_cord(player_pos, len(ter)) + loc.Y_PLAYER_VEC * loc.IMG_SIZE
                )
            )

        if (pressed_keys[pygame.K_w] and not sliding) or (sliding == "N" and tot_slided < 1):
            player_pos[1] -= 0.1
            tot_slided = round(tot_slided + 0.1, 1)
            sliding = "N"

        if (pressed_keys[pygame.K_s] and not sliding) or (sliding == "S" and tot_slided < 1):
            player_pos[1] += 0.1
            tot_slided = round(tot_slided + 0.1, 1)
            sliding = "S"

        if (pressed_keys[pygame.K_d] and not sliding) or (sliding == "E" and tot_slided < 1):
            player_pos[0] += 0.1
            tot_slided = round(tot_slided + 0.1, 1)
            sliding = "E"

        if (pressed_keys[pygame.K_a] and not sliding) or (sliding == "W" and tot_slided < 1):
            player_pos[0] -= 0.1
            tot_slided = round(tot_slided + 0.1, 1)
            sliding = "W"

        if tot_slided == 1:
            sliding = ""
            tot_slided = 0

        pygame.display.flip()
        clock.tick(loc.MAX_FPS)
        pygame.display.set_caption(str(clock.get_fps()))


if __name__ == "__main__":
    main()
