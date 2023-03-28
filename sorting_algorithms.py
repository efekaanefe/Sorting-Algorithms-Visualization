def selection_sort(arr, start_index):
    smallest_index = start_index
    bigger_index = smallest_index
    for i in range(start_index + 1, len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    arr[start_index], arr[smallest_index] = (
        arr[smallest_index],
        arr[start_index],
    )
    return {
        "arr": arr,
        "smallest_index": smallest_index,
        "bigger_index": bigger_index,
    }


def bubble_sort(arr, i):

    while i < len(arr) - 1:
        first = arr[i]
        second = arr[i + 1]
        if second < first:
            arr[i], arr[i + 1] = second, first
            # change_happened = True
            return {
                "arr": arr,
                "change_happened": True,
                "first_index": i,
                "second_index": i + 1,
            }
        i += 1
    return {
        "arr": arr,
        "change_happened": False,
        "first_index": None,
        "second_index": None,
    }
