import pygame
from random import shuffle

pygame.init()


WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualization")

# colors
BG_COL = (35, 35, 35)
DEFAULT_REC_COL = (192, 192, 192)


def main():
    # arr = shuffle(list(range(100)))
    arr = [22, 2, 5, 51, 15, 65, 40, 22, 31, 41, 90, 70, 40, 30, 7, 9, 11]
    rec_width = WIDTH // len(arr)
    rec_length_multiplier = (HEIGHT - 50) / max(arr)
    offset = (WIDTH - len(arr) * rec_width) / 2

    clock = pygame.time.Clock()
    running = True

    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for x, y in enumerate(arr):
            rect = pygame.Rect(
                x * rec_width + offset,
                HEIGHT - y * rec_length_multiplier,
                rec_width - 2,
                y * rec_length_multiplier,
            )
            pygame.draw.rect(SCREEN, DEFAULT_REC_COL, rect)

        pygame.display.update()
        clock.tick(75)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
