import random
import time
import matplotlib.pyplot as plt


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
                    self.plot(arr)

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
            self.plot(arr)
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            self.plot(arr)
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            self.plot(arr)

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.plot(arr)

    def plot(self, arr):
        plt.clf()
        plt.bar(range(len(arr)), arr)
        plt.draw()
        plt.pause(0.001)


def main():
    arr = [random.randint(0, 100) for _ in range(20)]
    plt.ion()
    plt.show()
    merge_sort_visualizer = SortVisualizer("merge_sort")
    merge_sort_visualizer.visualize(arr.copy())
    time.sleep(1)
    bubble_sort_visualizer = SortVisualizer("bubble_sort")
    bubble_sort_visualizer.visualize(arr.copy())
    time.sleep(1)
    selection_sort_visualizer = SortVisualizer("selection_sort")
    selection_sort_visualizer.visualize(arr.copy())
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
