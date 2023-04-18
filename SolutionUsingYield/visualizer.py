class Visualizer:
    def __init__(arr):
        pass

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

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
