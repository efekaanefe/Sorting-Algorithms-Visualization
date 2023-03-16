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
        "isChanged": True,
        "arr": arr,
        "smallest_index": smallest_index,
        "bigger_index": bigger_index,
    }
