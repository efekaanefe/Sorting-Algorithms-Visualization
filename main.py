import pygame
import random
from sorting_algorithms import selection_sort, bubble_sort

pygame.init()

FPS = 24
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualization")

# colors
BG_COL = (35, 35, 35)
DEFAULT_REC_COL = (192, 192, 192)
RED = (196, 0, 0)
GREEN = (0, 196, 0)


def main():
    # todo improve stopping sorting solution
    sort_algorithms = ["selection_sort", "bubble_sort"]
    curr_algo = sort_algorithms[1]

    arr = [random.randint(1, 100) for _ in range(50)]
    # arr = [22, 2, 5, 51, 15, 65, 40, 29, 22, 31, 41, 90, 70, 40, 30, 7, 9, 11]

    rec_width = WIDTH // len(arr)
    rec_length_multiplier = (HEIGHT - 50) / max(arr)
    offset = (WIDTH - len(arr) * rec_width) / 2

    clock = pygame.time.Clock()
    running = True
    is_sorting = True

    if curr_algo == sort_algorithms[0]:
        start_index = 0
    elif curr_algo == sort_algorithms[1]:
        i = 0
        change_happened = True

    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        different_color_indices = []

        if sorting_finished(arr):
            is_sorting = False

        if is_sorting:
            if curr_algo == sort_algorithms[0]:
                if start_index < len(arr):
                    output = selection_sort(arr, start_index)
                    arr = output["arr"]
                    different_color_indices.append(output["smallest_index"])
                    different_color_indices.append(output["bigger_index"])
                    # if different_color_indices[0] == different_color_indices[1]:
                    #     is_sorting = False
                    # else:
                    #     start_index += 1
                    start_index += 1
            if curr_algo == sort_algorithms[1]:
                if change_happened:
                    output = bubble_sort(arr, i)
                    arr = output["arr"]
                    different_color_indices.append(output["first_index"])
                    different_color_indices.append(output["second_index"])
                    change_happened = output["change_happened"]
                    i += 1
                else:
                    i = 0
                    change_happened = True
                # print(i)
        print("Sorting: ", is_sorting, random.randint(0, 100))

        for x, y in enumerate(arr):
            rect = pygame.Rect(
                x * rec_width + offset,
                HEIGHT - y * rec_length_multiplier,
                rec_width - 2,
                y * rec_length_multiplier,
            )
            COL = DEFAULT_REC_COL if x not in different_color_indices else GREEN
            pygame.draw.rect(SCREEN, COL, rect)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def sorting_finished(arr):
    return sorted(arr) == arr


if __name__ == "__main__":
    main()
