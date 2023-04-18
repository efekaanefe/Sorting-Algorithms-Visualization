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


def main():
    sort_algorithms = ["selection_sort", "bubble_sort"]
    curr_algo = sort_algorithms[1]

    arr = [random.randint(1, 100) for _ in range(20)]

    rec_width = WIDTH // len(arr)
    rec_length_multiplier = (HEIGHT - 50) / max(arr)
    offset = (WIDTH - len(arr) * rec_width) / 2

    clock = pygame.time.Clock()
    running = True
    is_sorting = True

    sorting_algorithm_generator = bubble_sort(
        arr, rec_width, rec_length_multiplier, offset
    )
    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        different_color_indices = []

        if is_sorting:
            if curr_algo == sort_algorithms[0]:
                output = selection_sort(arr)

            if curr_algo == sort_algorithms[1]:
                try:
                    next(sorting_algorithm_generator)
                except StopIteration:
                    is_sorting = False

            # draw_arr(arr, rec_width, rec_length_multiplier, offset)
            pygame.display.update()
            clock.tick(FPS)
    pygame.quit()
    quit()


def draw_arr(arr, rec_width, rec_length_multiplier, offset):
    for x, y in enumerate(arr):
        rect = pygame.Rect(
            x * rec_width + offset,
            HEIGHT - y * rec_length_multiplier,
            rec_width - 2,
            y * rec_length_multiplier,
        )
        COL = DEFAULT_REC_COL  # if x not in different_color_indices else GREEN
        pygame.draw.rect(SCREEN, COL, rect)

    pygame.display.update()


def bubble_sort(arr, rec_width, rec_length_multiplier, offset):

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_arr(arr, rec_width, rec_length_multiplier, offset)
                yield True
    return arr


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        self.merge_sort(arr, l, mid)
        self.merge_sort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid
    L = [arr[l + i] for i in range(n1)]
    R = [arr[mid + 1 + j] for j in range(n2)]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        self.draw(arr)


def sorting_finished(arr):
    return sorted(arr) == arr


if __name__ == "__main__":
    main()
