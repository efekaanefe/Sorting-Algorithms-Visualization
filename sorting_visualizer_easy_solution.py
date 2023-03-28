import pygame
import random
import time

pygame.init()

FPS = 5
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualization")

# colors
BG_COL = (35, 35, 35)
DEFAULT_REC_COL = (192, 192, 192)
RED = (196, 0, 0)
GREEN = (0, 196, 0)


class SortVisualizer:
    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name

    def visualize(self, arr):
        if self.algorithm_name == "bubble_sort":
            self.bubble_sort(arr)
        elif self.algorithm_name == "merge_sort":
            self.merge_sort(arr, 0, len(arr) - 1)
        elif self.algorithm_name == "selection_sort":
            self.selection_sort(arr)
        else:
            print("Invalid algorithm name")

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.draw(arr)

    def merge_sort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.merge_sort(arr, l, mid)
            self.merge_sort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
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
            self.draw(arr)
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            self.draw(arr)
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            self.draw(arr)

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.draw(arr)

    def draw(self, arr):
        rec_width = WIDTH // len(arr)
        rec_length_multiplier = (HEIGHT - 50) / max(arr)
        offset = (WIDTH - len(arr) * rec_width) / 2

        for x, y in enumerate(arr):
            rect = pygame.Rect(
                x * rec_width + offset,
                HEIGHT - y * rec_length_multiplier,
                rec_width - 2,
                y * rec_length_multiplier,
            )
            # COL = DEFAULT_REC_COL if x not in different_color_indices else GREEN
            COL = DEFAULT_REC_COL
            pygame.draw.rect(SCREEN, COL, rect)

        pygame.display.update()
        time.sleep(1)


def main():
    arr = [random.randint(0, 100) for _ in range(20)]

    clock = pygame.time.Clock()
    running = True
    is_sorting = True

    while running:
        SCREEN.fill(BG_COL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        merge_sort_visualizer = SortVisualizer("selection_sort")
        merge_sort_visualizer.visualize(arr.copy())

        clock.tick(FPS)

    # merge_sort_visualizer = SortVisualizer("merge_sort")
    # merge_sort_visualizer.visualize(arr.copy())
    # time.sleep(1)

    # bubble_sort_visualizer = SortVisualizer("bubble_sort")
    # bubble_sort_visualizer.visualize(arr.copy())
    # time.sleep(1)

    # selection_sort_visualizer = SortVisualizer("selection_sort")
    # selection_sort_visualizer.visualize(arr.copy())


if __name__ == "__main__":
    main()
