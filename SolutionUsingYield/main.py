import pygame
import random
import time

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


class DrawInfo:
    def __init__(
        self, rec_width, rec_length_multiplier, offset, different_color_indices=[]
    ):
        self.rec_width = rec_width
        self.rec_length_multiplier = rec_length_multiplier
        self.offset = offset
        self.different_color_indices = different_color_indices


def main():
    i = 1
    sort_algorithms = [selection_sort, bubble_sort, merge_sort]
    curr_algo = sort_algorithms[i]

    arr = [random.randint(1, 100) for _ in range(50)]

    rec_width = WIDTH // len(arr)
    rec_length_multiplier = (HEIGHT - 50) / max(arr)
    offset = (WIDTH - len(arr) * rec_width) / 2

    clock = pygame.time.Clock()
    running = True
    is_sorting = True
    sorting_algorithm_generator = curr_algo(
        arr, DrawInfo(rec_width, rec_length_multiplier, offset)
    )
    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        different_color_indices = []

        if is_sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                is_sorting = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def draw_arr(arr, draw_info):
    rec_width = draw_info.rec_width
    rec_length_multiplier = draw_info.rec_length_multiplier
    offset = draw_info.offset
    different_color_indices = draw_info.different_color_indices
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


def selection_sort(arr, draw_info):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_info.different_color_indices = [i, min_idx]
        draw_arr(arr, draw_info)
        yield True
    return arr


def bubble_sort(arr, draw_info):

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_info.different_color_indices = [j, j + 1]
                draw_arr(arr, draw_info)
                yield True
    return arr


def merge_sort(arr, draw_info):
    length = len(arr)
    if length == 1:
        return arr
    else:
        right_arr = arr[length // 2 :]
        left_arr = arr[: length // 2]

        # recursion
        merge_sort(left_arr, draw_info)
        merge_sort(right_arr, draw_info)

        # merge
        i = 0  # left_arr idx
        j = 0  # righ_arr idc
        k = 0  # 	merged arr idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            draw_arr(arr, draw_info)
            yield True
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            draw_arr(arr, draw_info)
            yield True
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            draw_arr(arr, draw_info)
            yield True
    return arr


def sorting_finished(arr):
    return sorted(arr) == arr


if __name__ == "__main__":
    main()
