import pygame
from random import shuffle

pygame.init()


WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualization")

# colors
BG_COL = (35, 35, 35)
DEFAULT_REC_COL = (192, 192, 192)


def main():
    # arr = shuffle(list(range(0, 100)))
    arr = [22, 2, 5, 51, 15, 65, 40, 22, 31, 41, 90, 70, 40, 30]
    rec_width = WIDTH / len(arr)
    rec_length_multiplier = HEIGHT / max(arr)

    clock = pygame.time.Clock()
    running = True

    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for x, y in enumerate(arr):
            rect = pygame.Rect(
                x * rec_width,
                HEIGHT - y * rec_length_multiplier,
                rec_width - 2,
                y * rec_length_multiplier,
            )
            pygame.draw.rect(SCREEN, DEFAULT_REC_COL, rect)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
